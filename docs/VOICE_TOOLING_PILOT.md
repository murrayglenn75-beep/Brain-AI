# Optional local voice and evaluated tooling

## Voicebox pilot (not enabled)
1. Inspect official Voicebox source, exact release, MIT license and installed dependencies before running a binary.
2. On a Windows test machine, measure CPU usage, memory, real-time factor and microphone-to-text latency against the available hardware budget. Do not assume voice cloning will run effectively without a GPU.
3. Use opt-in microphone activation with an unmistakable recording indicator, short retention, explicit deletion and no recordings in Git commits.
4. Record and synthesize only the user's voice or voices used with documented consent. No voice imitation of third parties without consent.
5. Transcribed speech is untrusted input. AAK must authorize any tool invocation produced from it. Default the connector to transcription-only, read-only, disabled unless explicitly enabled.
6. Prohibit automatic network transmission and require auditing of network activity; verify that the selected engine actually operates offline before calling it local.
7. Assess accessibility with keyboard alternatives, screen readers and transcription review before executing effects.

## LLM Engineer Toolkit adoption procedure
Treat https://github.com/KalyanKS-NLP/llm-engineer-toolkit as a comparison directory, not a list of approved dependencies.

For any candidate library record:
- Repo URL, immutable release/tag/commit, license, maintainer activity and security history
- Actual supported platform and resource requirements
- Alternatives already present in FORGE/APEX/AAK and feature overlap
- Supply-chain and permission risks, offline/online data egress
- Baseline task quality, cost, p95 latency, memory, failure handling and rollback
- Independent review decision: rejected / pilot / approved / deployed, with test evidence

Never silently install tools, voice models or MCP servers from an external post. Choose the least complex solution that meets acceptance tests.

## Shared-context boundary
The context retrieval prototype returns path, source line, hash and untrusted excerpt. Any future voice or tool adapter must consume context through independently authorized service interfaces, not direct unrestricted file access.
