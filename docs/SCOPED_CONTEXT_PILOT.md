# Shared context layer pilot

This pilot adds a read-only, permission-scoped Markdown evidence interface with exact line numbers and SHA-256 source file hashes. It is **not** a complete authenticated service or a production MCP server.

Run local tests: `cd scripts && python -m unittest -v test_context_layer.py`.

Security: tenant and collection scopes are enforced before reading. The caller MUST obtain Principal from independently authenticated session context; accepting a model-supplied Principal would defeat authorization. Results are untrusted data, not policy, instructions or proof of authorization. No automatic writing, outbound calls, embeddings, remote sync, or private voice storage.

Known limitations: simple lexical scoring, no native PDF extraction, no document-level ACLs, no audit persistence, no authenticated service integration, and no secure multi-user isolation across arbitrary OS processes. Do not point at confidential directories or mount one shared filesystem across mutually untrusted tenants. The Murray Laws remain in a separately protected constitutional source.

Follow-up: AAK identity/authorization integration, adversarial retrieval evaluation, redact sensitive excerpts and add source version validation, and then optional local dictation via a vetted voice connector. No voice cloning or recording by default.

References: shared-context research entry (2026-11-07); https://github.com/murrayglenn75-beep/Brain-AI/pull/12.
