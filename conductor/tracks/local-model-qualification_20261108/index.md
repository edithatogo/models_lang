# Model, hardware and task qualification — 8 November 2026

**Status: planned.** This plan is not a claim that model weights were downloaded, runtime adapters were executed, clinical tests passed or any model is approved. Primary ownership: `models_lang`; consumers own their own decisions and deployment gates.

## Intended result

A reproducible *task × model × exact revision × quantisation × runtime × OS/architecture × accelerator* qualification matrix, reusable by coding agents, medicolegal analysis, clinical extraction, health-policy research and clinical safety work. Model selection must be evidence-led; fine-tuning is an experimental option, never the default.

## Existing starting points

- `training/fine-tuning`: Intel/OpenVINO/ONNX LoRA smoke pipeline and experimental Liquid checkpoints.
- `training/mem0`: LFM2-ColBERT retrieval sidecar and triplet experiments.
- HF models: `edithatogo/qwen3-4b-hermes-lora`, `edithatogo/qwen3-4b-hermes-lora-peft-converted`, `edithatogo/lfm2.5-1.2b-intel-lora`, `edithatogo/ollama-colbert-local-artifacts`.
- HF synthetic training dataset: `edithatogo/qwen3-hermes-strict-toolcall-synthetic-v4`; HF dataset registry: `edithatogo/dataset-estate-registry` (remains canonical).
- Maintain exact model/checkpoint metadata from model cards; `catalog/candidates.json` records discovery, not qualification.

## Phases and coding-agent acceptance

1. **C1: Reconcile.** Inspect existing training scripts, benchmark assets, upstream evaluation libraries and licences; preserve historical checkpoint IDs and avoid refactoring working paths. Create/update a lockable HF model catalogue: model ID, source revision SHA, architecture, modality, licence/usage restrictions, expected weight residency, quantisation and eligible tasks. Mark all unverified properties `unknown`.
   - Accept: automated catalogue schema validation, upstream URL/revision proof, no default model without matching evidence, licence gate for Liquid and gated MedGemma.
2. **C2: Hardware discovery.** Detect Windows x64 and ARM64, Linux x64 and ARM64, macOS ARM64; NVIDIA CUDA (RTX 4060/4060 Ti variants recorded by exact GPU and VRAM), Apple Metal/MLX, Intel OpenVINO and CPU. Separate OS/ISA, physical memory, GPU memory, unified-memory budget, bandwidth and driver/kernel versions. Use maintained runtime capabilities from llama.cpp/Ollama/MLX/Transformers/vLLM where available. Do not conflate MLX with a device.
   - Accept: full hardware inventory, explicit unsupported/untested states, device-specific smoke tests, no inferred CUDA/Metal kernel support from a Hugging Face model listing.
3. **C3: Evaluation fixtures.** Implement frozen synthetic/public-rights-cleared tasks: exact tool calls and sandbox coding tests; clinical terminology/phenotype extraction; fact/observation/event timeline; source-grounded legal-policy extraction; conflicting evidence; incident contributors; long-context retrieval vs hybrid retrieval and cross-encoders. Add `unknown`/abstain cases and adversarial prompt injection. Divide development and locked holdout by source/case to prevent leakage.
   - Accept: fixture licences/provenance, stable scoring rubric, independent human annotation protocol for consequential judgements.
4. **C4: Reproducible runs.** Implement adapters for native GGUF/llama.cpp/Ollama, CUDA-backed inference, Metal/MLX and OpenVINO only where supported. Exact checkpoint commit and weights hash, runtime/kernel commit, chat template, quantisation, max real context, KV-cache settings, prompt tokens, energy when measurable, memory peak, prefill/output throughput, latency, tool JSON validity, structured score calibration, errors and timeouts must be logged.
   - Accept: emit a `contracts/qualification-result.schema.json`-valid result, run twice with documented nondeterminism and record failures as failures, not skipped successes. No remote inference in local-only tests.
5. **C5: Comparative gates.** Compare Liquid LFM3 and MoE models, Liquid d1 decision models, small Qwen/MiMo coding, Qwen3.8-27B/Gemma 4, coding MoE and gated clinical models only after access/licence review. Measure component-level sensitivity, specificity, recall, F1, calibration/ECE/Brier, source citation accuracy, missed critical facts, chronological/counterfactual errors, abstention and expert agreement. Compare full context, retrieval and hybrid approaches at equal budgets.
   - Accept: independent task metrics with uncertainty intervals, practical Pareto frontier on relevant hardware. No aggregate single-number 'best model' or unsupported clinical suitability claim.
6. **C6: Adapt only if useful.** Compare base model, prompt/structured-output changes, retrieval and LoRA fine-tuning on identical holdout cases. Include training compute/data rights, cross-platform export fidelity, regression and catastrophic-forgetting checks.
   - Accept: promote an adapter only on a prespecified meaningful improvement without breaching safety, licence, latency or cost thresholds. Preserve negative results.
7. **C7: Portable qualification exports.** Publish a versioned non-sensitive manifest with replay commands, dependency/SBOM references, hashes, failure cases and run provenance. Consumer products import a pinned result, not mutable model IDs. Never publish private prompts, patient/practitioner data, confidential incidents or derived sensitive aggregates.
   - Accept: exports validate offline, hash verification, revocation/invalidation policy, and product-specific human approval before clinical use.

## Initial model candidate groups

- Small and decision: `LiquidAI/LFM3-1.7B`, `LiquidAI/d1-2B`, `LiquidAI/d1-Omni-2B`, `LiquidAI/LFM2.5-8B-A1B`, `LiquidAI/LFM2.5-24B-A2B`.
- Baseline/coding: `Qwen/Qwen3.5-4B`, `XiaomiMiMo/MiMo-V2.6-Distill-Qwen-9B`, `Qwen/Qwen3.8-27B`, `Qwen/Qwen3-Coder-Next`.
- General/specialist: `google/gemma-4-31B-it`, `google/medgemma-1.5-4b-it`, `google/medgemma-27b-text-it` (gated medical checkpoints; permission and intended-use assessment mandatory).
- Watch only: SubQ Snap / other API-only models; not eligible for a no-cloud-sensitive-data workload.

## Portfolio ownership (do not duplicate implementation)

`hermes-ollama-pack` owns Hermes endpoint/adapter qualification and coding-agent deployability; `rcagent` owns cognitive-autopsy task constructs and expert judgements; `careops` owns optional operational integration and privacy gates; `atlas-health-policy-anz` owns policy comparison truth; `searchright` owns search/screening validity; `authentext` owns meaning/length/voice preservation; `learningfromharm` owns permitted NZ HDC corpus study design. Consumers return task-level evaluation records without sensitive inputs. Coordinate schema changes by semver; prefer existing dependencies.

## Delivery estimates (agent engineering only)

C1–C2 first reviewable PR 1–2 agent-days; C3–C4 first bounded benchmark in 3–5 agent-days once hardware exists; initial C5 2–4 agent-days plus substantial model download/inference; C6–C7 as justified. Specialist annotations, institutional approvals, prospective validation and journal publication are separate human/calendar gates.
