"""Read-only permission-scoped Markdown evidence retrieval. No external dependencies."""
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
import re

@dataclass(frozen=True)
class Principal:
    subject: str
    tenant: str
    allowed_collections: frozenset[str]

@dataclass(frozen=True)
class Collection:
    name: str
    tenant: str
    root: Path

class AccessDenied(PermissionError):
    pass

def retrieve(principal: Principal, collection: Collection, query: str, limit: int = 10):
    if not principal.subject or not principal.tenant or not collection.tenant:
        raise AccessDenied("invalid identity")
    if principal.tenant != collection.tenant or collection.name not in principal.allowed_collections:
        raise AccessDenied("collection not authorized")
    if not 1 <= limit <= 50:
        raise ValueError("invalid limit")
    terms = re.findall(r"[\w-]+", query.casefold())[:12]
    if not terms:
        return []
    root = collection.root.resolve(strict=True)
    if not root.is_dir():
        raise ValueError("collection root must be directory")
    results = []
    for path in sorted(root.rglob("*.md")):
        if path.is_symlink() or not path.is_file():
            continue
        resolved = path.resolve()
        if not resolved.is_relative_to(root):
            continue
        try:
            data = path.read_bytes()
            lines = data.decode("utf-8").splitlines()
        except (OSError, UnicodeError):
            continue
        digest = sha256(data).hexdigest()
        for lineno, line in enumerate(lines, 1):
            score = sum(line.casefold().count(term) for term in terms)
            if score:
                results.append({"collection": collection.name,
                                "path": resolved.relative_to(root).as_posix(),
                                "line": lineno, "score": score, "excerpt": line[:300],
                                "sha256": digest, "status": "untrusted_source"})
    return sorted(results, key=lambda x: (-x["score"], x["path"], x["line"]))[:limit]
