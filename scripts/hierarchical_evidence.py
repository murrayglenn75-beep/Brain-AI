"""Section-aware retrieval on top of independently scoped Markdown retrieval.

The caller must supply an authenticated Principal, not model-generated identity.
No network access, embeddings, or execution of source instructions.
"""
from pathlib import Path
import re
from context_layer import Principal, Collection, retrieve

def retrieve_sections(principal: Principal, collection: Collection, query: str, limit: int = 10):
    if not 1 <= limit <= 50:
        raise ValueError("invalid limit")
    # Do not read an unauthorized collection even for heading discovery.
    hits = retrieve(principal, collection, query, limit=50)
    results = []
    for hit in hits:
        path = collection.root.resolve(strict=True) / hit["path"]
        if path.is_symlink() or not path.resolve().is_relative_to(collection.root.resolve(strict=True)):
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeError):
            continue
        headings = [(i, len(line) - len(line.lstrip("#")), line.lstrip("#").strip())
                    for i, line in enumerate(lines, 1) if re.match(r"^#{1,6}\\s", line)]
        prior = [x for x in headings if x[0] <= hit["line"]]
        section = prior[-1] if prior else (1, 0, "(document)")
        end = len(lines)
        if section[1]:
            for index, depth, _ in headings:
                if index > section[0] and depth <= section[1]:
                    end = index - 1
                    break
        results.append({**hit, "section_title": section[2],
                        "section_start": section[0], "section_end": end})
    return results[:limit]
