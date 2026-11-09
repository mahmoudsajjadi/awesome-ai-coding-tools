# Hardware & VRAM Sizing Guide for Local AI Coding

A practical sizing and mathematical configuration guide for running open-weight coding models privately on local hardware without cloud API fees.

---

## 1. Exact VRAM Calculation Formula

To accurately size local models and avoid Out-Of-Memory (OOM) crashes during generation, VRAM allocation is calculated from three components: **Model Weight Footprint**, **Active Key-Value (KV) Cache**, and **CUDA Runtime & Framework Overhead**.

### Mathematical Model

$$\text{Total VRAM Required} = \text{VRAM}_{\text{weight}} + \text{VRAM}_{\text{kv}} + \text{VRAM}_{\text{overhead}}$$

Where:

1. **Model Weights VRAM ($\text{VRAM}_{\text{weight}}$):**
   $$\text{VRAM}_{\text{weight}} = \frac{\text{Parameters} \times \text{Bits per Weight}}{8 \times 10^9} \text{ GB}$$
   * *Example:* A 14.7B parameter model quantized at Q4_K_M (~4.5 bits/weight effective with scales) requires $\approx \frac{14.7 \times 10^9 \times 4.5}{8 \times 10^9} \approx 8.27 \text{ GB}$ (file/weight size $\approx 9.0 \text{ GB}$).
   * Quantization bit depths:
     - **Q4_K_M:** ~4.5 bits/weight
     - **Q5_K_M:** ~5.5 bits/weight
     - **Q8_0:** ~8.5 bits/weight
     - **FP16:** 16.0 bits/weight

2. **Active KV Cache VRAM ($\text{VRAM}_{\text{kv}}$):**
   $$\text{VRAM}_{\text{kv}} = \frac{2 \times \text{Layers} \times \text{KV Heads} \times \text{Head Dimension} \times \text{Precision Bytes} \times \text{Context Length} \times \text{Batch Size}}{10^9} \text{ GB}$$
   * The multiplier $2$ accounts for Key and Value tensors.
   * Modern coding models utilize **Grouped-Query Attention (GQA)**, reducing KV heads (e.g., 4 or 8 KV heads vs. 28–40 Query heads).
   * Precision: 2 bytes for standard FP16 KV cache; 1 byte for FP8/Q8 KV cache.
   * Batch size for interactive coding agents: $1$.

3. **CUDA Runtime & Framework Overhead ($\text{VRAM}_{\text{overhead}}$):**
   $$\text{VRAM}_{\text{overhead}} \approx 0.20 \times (\text{VRAM}_{\text{weight}} + \text{VRAM}_{\text{kv}})$$
   * Accounts for CUDA context initialization (~0.5–1.2 GB), PyTorch/llama.cpp memory arena fragmentation, and scratchpad activations during attention projection.

---

## 2. Hardware Tier Recommendations & Quantization Matrix

All recommendations below are verified for local developer agent workflows (such as Aider, Continue.dev, or OpenCode). Sizing numbers are estimates based on standard GQA KV cache with FP16 cache precision.

| Available VRAM / Unified Memory | Target Hardware Class | Recommended Coding Model | Quantization Level | Context Length | Weight Footprint (Est.) | Active KV Cache (Est.) | Total Allocated VRAM (Est.) | Source Model Card | 1-Click Terminal Command | Last Verified |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :---: |
| **8 GB VRAM** | NVIDIA RTX 4060, RTX 3070, Apple M1/M2/M3 (16GB RAM) | **Qwen 2.5 Coder 7B** | Q4_K_M | 16K (16,384) | ~4.7 GB | ~0.4 GB | ~6.1 GB | [Ollama](https://ollama.com/library/qwen2.5-coder:7b) / [HF](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct) | `ollama run qwen2.5-coder:7b` | 2026-11-09 |
| **8 GB VRAM** | NVIDIA RTX 3070, RTX 4060 Ti 8GB | **Qwen 2.5 Coder 7B** | Q5_K_M | 8K (8,192) | ~5.4 GB | ~0.2 GB | ~6.7 GB | [Ollama](https://ollama.com/library/qwen2.5-coder:7b) / [HF](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct) | `ollama run qwen2.5-coder:7b-instruct-q5_K_M` | 2026-11-09 |
| **12 GB VRAM** | NVIDIA RTX 3060 12GB, RTX 4070 | **Qwen 2.5 Coder 14B** | Q4_K_M | 16K (16,384) | ~9.0 GB | ~0.8 GB | ~11.8 GB | [Ollama](https://ollama.com/library/qwen2.5-coder:14b) / [HF](https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct) | `ollama run qwen2.5-coder:14b` | 2026-11-09 |
| **12 GB VRAM** | NVIDIA RTX 4070, Apple M3 (18GB RAM) | **Qwen 2.5 Coder 7B** | Q8_0 | 32K (32,768) | ~7.9 GB | ~0.8 GB | ~10.4 GB | [Ollama](https://ollama.com/library/qwen2.5-coder:7b) / [HF](https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct) | `ollama run qwen2.5-coder:7b-instruct-q8_0` | 2026-11-09 |
| **16 GB VRAM** | NVIDIA RTX 4080, RTX 5080, RTX 4060 Ti 16GB, Apple Mac (24GB RAM) | **Qwen 2.5 Coder 14B** | Q5_K_M | 32K (32,768) | ~10.5 GB | ~1.6 GB | ~14.5 GB | [Ollama](https://ollama.com/library/qwen2.5-coder:14b) / [HF](https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct) | `ollama run qwen2.5-coder:14b-instruct-q5_K_M` | 2026-11-09 |
| **16 GB VRAM** | NVIDIA RTX 4080, RTX 4060 Ti 16GB, Apple M3 (24GB) | **Devstral Small 2 (24B)** | Q4_K_M | 16K (16,384) | ~14.2 GB | ~0.7 GB | ~15.9 GB | [Ollama](https://ollama.com/library/devstral-small-2) / [HF](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512) | `ollama run devstral-small-2:24b` | 2026-11-09 |
| **24 GB VRAM** | NVIDIA RTX 3090, RTX 4090, Apple M-Max (32GB+) | **Qwen 2.5 Coder 32B** | Q4_K_M | 32K (32,768) | ~19.8 GB | ~2.1 GB | ~23.8 GB | [Ollama](https://ollama.com/library/qwen2.5-coder:32b) / [HF](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct) | `ollama run qwen2.5-coder:32b` | 2026-11-09 |
| **24 GB VRAM** | NVIDIA RTX 3090, RTX 4090, Apple M-Max (32GB+) | **Qwen 2.5 Coder 14B** | Q8_0 | 64K (65,536) | ~15.5 GB | ~3.2 GB | ~22.4 GB | [Ollama](https://ollama.com/library/qwen2.5-coder:14b) / [HF](https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct) | `ollama run qwen2.5-coder:14b-instruct-q8_0` | 2026-11-09 |
| **32 GB+ Unified / Multi-GPU** | Dual RTX 3090 (48GB), Apple Mac Studio (64GB/128GB) | **Qwen 2.5 Coder 32B** | Q8_0 | 64K (65,536) | ~34.2 GB | ~4.2 GB | ~46.0 GB | [Ollama](https://ollama.com/library/qwen2.5-coder:32b) / [HF](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct) | `ollama run qwen2.5-coder:32b-instruct-q8_0` | 2026-11-09 |
| **32 GB+ Unified / Multi-GPU** | Apple M2/M3/M4 Ultra (64GB - 128GB Unified) | **DeepSeek-R1-Distill-Qwen-32B** | Q5_K_M | 64K (65,536) | ~23.5 GB | ~4.2 GB | ~33.2 GB | [Ollama](https://ollama.com/library/deepseek-r1:32b) / [HF](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B) | `ollama run deepseek-r1:32b` | 2026-11-09 |

*Note: All footprint and VRAM allocation values are estimates calculated with $20\%$ runtime overhead. Actual consumption may vary by $\pm 5\%$ depending on host driver version, display server overhead, and GGUF quantization metadata variations.*

---

## 3. Step-by-Step Local Offline Setup Recipe

Run an autonomous coding agent entirely locally with zero cloud API keys:

```bash
# 1. Install and start Ollama
curl -fsSL https://ollama.com/install.sh | sh

# 2. Pull the 14B parameter coding model
ollama run qwen2.5-coder:14b

# 3. Install Aider in your Python environment
pip install aider-chat

# 4. Launch Aider in your git repository using your local model
cd /path/to/your/project
aider --model ollama/qwen2.5-coder:14b --architect
```

---

## 4. Hardware Recommendations by Budget

- **Budget ($0):** Run `qwen2.5-coder:7b` via Ollama on existing 8GB or 16GB laptop RAM (CPU inference at 8–15 tok/s).
- **Pro Developer ($1,000 - $1,800):** Single RTX 4070 Ti Super (16GB) or Apple M3 Mac (36GB) running `qwen2.5-coder:14b` at interactive speeds (25–40 tok/s).
- **Research / High Throughput:** Dual RTX 3090 (48GB total VRAM) or Apple M2/M3 Ultra (64GB–128GB) running unquantized 32B models or MoE configurations.
