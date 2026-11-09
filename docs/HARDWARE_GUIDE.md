# Hardware & VRAM Sizing Guide for Local AI Coding

A practical sizing and configuration guide for running open-weight coding foundation models privately on local hardware without cloud API fees.

---

## 1. Physical GPU VRAM to Model Sizing Matrix

Match your physical GPU hardware to the largest model that fits fully in VRAM for zero-offload token generation:

| Available VRAM | Target Hardware | Recommended Coding Model | Model Footprint | Active Context | 1-Click Terminal Command |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **8 GB VRAM** | RTX 4060, RTX 3070, Apple M1/M2/M3 (16GB RAM) | **Qwen 2.5 Coder 7B** (Q4_K_M) | ~4.7 GB | 16K | `ollama run qwen2.5-coder:7b` |
| **12 GB VRAM** | RTX 4070, RTX 3060 12GB | **Qwen 2.5 Coder 14B** (Q4_K_M) | ~9.0 GB | 32K | `ollama run qwen2.5-coder:14b` |
| **16 GB VRAM** | RTX 4080, RTX 5080, RTX 4060 Ti 16GB | **Devstral Small 2 (24B)** (Q4_K_M) | ~15.0 GB | 384K | `ollama run devstral-small-2:24b` |
| **24 GB VRAM** | RTX 3090, RTX 4090, Apple M-Max (32GB+) | **Qwen3-Coder 30B (MoE)** *(Repo-Scale)*<br/>**Qwen 2.5 Coder 32B** *(Single-File SOTA)* | ~19.0 GB<br/>~20.0 GB | 256K<br/>32K | `ollama run qwen3-coder:30b`<br/>`ollama run qwen2.5-coder:32b` |

---

## 2. Quantization and Memory Footprint

| Model Size | Quantization | Minimum VRAM / Unified RAM | Recommended GPU | Typical Tokens/Sec |
| :--- | :---: | :---: | :--- | :---: |
| **0.5B - 1.5B** | FP16 / Q8 | 2 GB - 4 GB | Any modern laptop (CPU/GPU) | 60 - 120 |
| **7B** | Q4_K_M | 6 GB | RTX 3060 / 4060 (8GB) | 35 - 55 |
| **7B** | Q8_0 | 10 GB | RTX 3080 / 4070 (12GB) | 30 - 45 |
| **14B** | Q4_K_M | 10 GB - 12 GB | RTX 3080 / 4070 / Apple M2 (16GB) | 25 - 40 |
| **14B** | FP16 | 30 GB | RTX 3090 / 4090 / Apple M2 Max | 20 - 35 |
| **32B** | Q4_K_M | 20 GB - 24 GB | RTX 3090 / 4090 (24GB) or Mac (32GB+) | 15 - 28 |
| **32B** | Q8_0 | 36 GB | 2x RTX 3090 / Mac Studio (64GB) | 12 - 22 |

---

## 3. Step-by-Step Local Offline Setup Recipe

Run a full-featured coding agent entirely locally with zero cloud API subscriptions:

```bash
# 1. Install and start Ollama
curl -fsSL https://ollama.com/install.sh | sh

# 2. Pull the 14B parameter coding model
ollama run qwen2.5-coder:14b

# 3. Install Aider in your Python environment
pip install aider-chat

# 4. Launch Aider in your git repository using your local model
cd /path/to/your/project
aider --model ollama/qwen2.5-coder:14b
```

---

## 4. Hardware Recommendations by Budget

- **Budget ($0):** Run `qwen2.5-coder:7b` via Ollama on existing 8GB or 16GB laptop RAM (CPU inference at 8–15 tok/s).
- **Pro Developer ($1,000 - $1,800):** Single RTX 4070 Ti Super (16GB) or Apple M3 Mac (36GB) running `qwen2.5-coder:14b` at interactive speeds (25–40 tok/s).
- **Research / High Throughput:** Dual RTX 3090 (48GB total VRAM) or Apple M2/M3 Ultra (64GB–128GB) running unquantized 32B models or MoE configurations.
