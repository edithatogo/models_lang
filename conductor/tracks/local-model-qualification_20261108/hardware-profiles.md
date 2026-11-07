# Deployment and evaluation matrix (candidate configurations)

**Status: planning matrix, not hardware qualification.** Device capacity, supported backends, licences and context length must be measured on the exact model revision, engine revision and quantisation. Weight memory alone omits KV cache, runtime overhead, other processes and concurrency. MLX is a framework; Apple Metal and NVIDIA CUDA are accelerator stacks.

| Host | Architecture | Device/backend | Candidates for initial smoke tests | Hard gate |
| --- | --- | --- | --- | --- |
| Windows | x86_64 | RTX 4060 8 GB / CUDA; Ollama, llama.cpp, WSL2 | LFM3-1.7B, d1-2B, Qwen3.5-4B; 9B quantised only if fully resident at test context | Verify VRAM and context; fail rather than silently CPU-offload for a GPU-only profile |
| Windows | x86_64 | RTX 4060 Ti 16 GB / CUDA | MiMo-V2.6-Distill-Qwen-9B, LFM2.5-8B-A1B; LFM2.5-24B-A2B candidate | Residency, quantisation and actual supported kernels |
| Windows | arm64 | Snapdragon CPU, Vulkan/NPU when supported | Small models and backend capability probes | Do not assume GPU/NPU model support from generic ARM64 compatibility |
| Linux | x86_64 | NVIDIA CUDA 24–32 GB | Qwen3.8-27B Q4, LFM2.5-24B-A2B Q4 where compatible | Prefill throughput and actual context memory; compare retrieval |
| Linux | x86_64 | NVIDIA CUDA 48–96 GB | Qwen3-Coder-Next, 27B/31B general reasoning and several smaller specialists | Total MoE weights, multi-GPU/serving constraints |
| Linux | arm64 | CPU; NVIDIA CUDA on supported devices | Small models plus target-specific model/backend tests | Record exact SoC, driver and accelerator variant |
| macOS | arm64 | Apple Silicon Metal/MLX; 16 GB unified | LFM3-1.7B, d1-2B, Qwen3.5-4B; 9B optional | OS memory headroom, swap and native decision-type support |
| macOS | arm64 | Apple Silicon Metal/MLX; 32–64 GB unified | 9B, LFM2.5-24B-A2B, Qwen3.8-27B with appropriate quantisation | Unified memory budget and supported model implementation |
| macOS | arm64 | Apple Silicon Metal/MLX; 96–128 GB+ unified | 27B/31B models; Qwen3-Coder-Next if full model fits | Sustained bandwidth, long-context cache and concurrency |
| Any | x86_64/arm64 | CPU-only, llama.cpp/OpenVINO as supported | Baseline 1B–9B quantised | Throughput and latency; do not claim interactive feasibility by fit alone |

## Required comparisons

- Separate **prefill**, **generation**, **decision scoring** and **end-to-end task** latency. d1 decision classification may not be equivalent to generative JSON classification; benchmark both.
- Compare native Transformers, GGUF/llama.cpp, MLX and quantised variants without assuming feature parity (particularly d1's answer types).
- Compare long-context full-record processing against retrieval + reranking at the same budget; include distant-evidence and contradictory-context tasks.
- Record no-egress execution, third-party inference fallbacks, model and runtime licences, exact commit IDs, weight checksums and a downgrade/rollback method.
- Disallow a 'supported' status until actual execution demonstrates the required modality, tool schema, context and accuracy on an accessible device. Mark absent hardware `unverified`, not `passed`.

The benchmark engine should use reusable existing frameworks where fit for purpose (e.g. llama.cpp or vLLM serving, pytest for task cases, standard metrics libraries and established LM evaluation harnesses); do not write a new inference backend.
