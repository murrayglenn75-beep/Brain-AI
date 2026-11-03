# Portable knowledge layer (pilot)

This is an optional, dependency-free, **read-only** Markdown retrieval interface. It works with an Obsidian-compatible folder of Markdown files; Obsidian is not required. No network requests, embeddings, automatic ingestion or AI-generated edits.

## Usage
```bash
python scripts/knowledge_index.py --root docs --query "authorization policy" --limit 10
python -m unittest discover -s scripts -p 'test_knowledge_index.py'
```

Search returns JSON with relative path, 1-based source line, score and excerpt. Results are **untrusted evidence candidates**, not approved facts or authorization decisions. Human/independent checks are required before using them to drive actions.

## Safety boundaries
- The tool is read-only and skips symlinks; use a specifically allowed knowledge directory.
- Do not put secrets, private transcripts or sensitive customer data in public Git repositories.
- Keep canonical Murray Laws and authorization rules in a separately protected source. A Markdown search result cannot revise policy or grant capability.
- Proposed updates must be reviewed independently and accepted through existing repository controls.
- This prototype is lexical retrieval, not a semantic index; evaluate retrieval quality, cross-repository isolation and larger-directory performance before wider rollout.
