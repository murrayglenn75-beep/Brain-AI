"""Local read-only search for Markdown notes."""
import argparse
import json
from pathlib import Path

def search(root, query, limit=10):
    root = Path(root).resolve()
    terms = query.lower().split()
    if not terms or not root.is_dir():
        return []
    found = []
    for path in sorted(root.rglob("*.md")):
        if path.is_symlink() or not path.is_file():
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            score = sum(line.lower().count(word) for word in terms)
            if score:
                found.append({"path": path.relative_to(root).as_posix(), "line": number,
                              "score": score, "excerpt": line[:400]})
    return sorted(found, key=lambda x: (-x["score"], x["path"], x["line"]))[:limit]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True)
    parser.add_argument("--query", required=True)
    parser.add_argument("--limit", type=int, default=10)
    options = parser.parse_args()
    print(json.dumps({"results": search(options.root, options.query, options.limit)}, indent=2))
