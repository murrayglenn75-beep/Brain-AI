# Hierarchical evidence retrieval pilot

PageIndex-inspired **Markdown section navigation** on the existing Brain-AI scoped knowledge prototype. Uses original headings and source line ranges instead of inventing summaries or requiring a vector database. Search results include exact matching line, nearest section, section range, source SHA-256, tenant/collection and untrusted-data flag.

Run from scripts: `python -m unittest -v test_hierarchical_evidence.py test_context_layer.py`.

This is **not PageIndex itself** and is not yet a PDF/table extractor, LLM navigation engine or production RAG system. Source matching remains lexical. It inherits limitations of the scoped context prototype; identity must come from independent authentication and AAK policy enforcement before accessing private records.

Benchmark plan: compare lexical baseline against section-aware output on gold queries for financial reports, footnotes, audit manuals and technical documents. Measure exact-answer evidence recall, false positives, p95 latency, token cost and denial isolation. Do not adopt project-reported FinanceBench accuracy as an internal result. Vane search is a separate opt-in research candidate: it uses network services for live web queries even when inference is local.

Security: never infer tool permissions from retrieved text; validate source hash before downstream claims; keep Murray Laws separately protected.
