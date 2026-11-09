# Seminal Academic Papers & Citations

A curated bibliography of foundational peer-reviewed research papers in neural code generation, repository-level retrieval, interactive agent-computer interfaces, and developer productivity studies.

---

## 1. Benchmarks & Real-World Evaluation

- **SWE-bench: Can Language Models Resolve Real-World GitHub Issues?**  
  *Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, Karthik Narasimhan.* (ICLR 2024)  
  Introduced the benchmark evaluating LLMs on 2,294 real-world GitHub issues across popular Python repositories.  
  [[ArXiv](https://arxiv.org/abs/2310.06770)] | [[Code](https://github.com/princeton-nlp/SWE-bench)]

- **Evaluating Large Language Models Trained on Code**  
  *Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, et al.* (OpenAI Technical Report 2021)  
  Introduced Codex and the **HumanEval** benchmark, defining functional correctness via automated unit tests ($pass@k$).  
  [[ArXiv](https://arxiv.org/abs/2107.03374)]

- **Program Synthesis with Large Language Models**  
  *Jacob Austin, Augustus Odena, Maxwell Nye, Maarten Bosma, Henryk Michalewski, David Dohan, Ellen Jiang, Carrie Cai, Michael Terry, Quoc Le, Charles Sutton.* (2021)  
  Formulated the **MBPP** (Mostly Basic Python Problems) dataset for programming evaluation.  
  [[ArXiv](https://arxiv.org/abs/2108.07732)]

- **Can It Edit? Evaluating the Ability of Large Language Models to Solve Code Editing Tasks**  
  *Federico Cassano, Luisa Bentivogli, et al.* (2024)  
  Evaluated LLMs on diff-based code editing vs. scratch code generation.  
  [[ArXiv](https://arxiv.org/abs/2406.01254)]

---

## 2. Repository-Level Context & Retrieval

- **RepoCoder: Repository-Level Code Completion Through Iterative Retrieval and Generation**  
  *Fengji Zhang, Bei Chen, Yue Zhang, Jacky Liu, Jian-Guang Lou.* (EMNLP 2023)  
  Proposed an iterative retrieval-generation framework combining similarity retrieval with generation-conditioned queries.  
  [[ArXiv](https://arxiv.org/abs/2303.12570)]

- **CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion**  
  *Yangruibo Ding, Zhiruo Wang, Weishi Wang, Shafiq Joty.* (NeurIPS 2023)  
  Standardized cross-file dependency benchmarking across Python, Java, C#, and TypeScript.  
  [[ArXiv](https://arxiv.org/abs/2310.19379)]

---

## 3. Agentic Loops & Self-Correction

- **SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering**  
  *John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, Ofir Press.* (2024)  
  Designed the Agent-Computer Interface (ACI) giving LLMs specialized file-viewing, directory-searching, and test execution tools.  
  [[ArXiv](https://arxiv.org/abs/2405.15793)] | [[Code](https://github.com/princeton-nlp/SWE-agent)]

- **InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback**  
  *John Yang, Akshat Shrivastava, Karthik Narasimhan, et al.* (ICML 2023)  
  Formalized interactive coding as a Reinforcement Learning POMDP environment.  
  [[ArXiv](https://arxiv.org/abs/2306.14898)]

- **Self-Debugging: Teaching Language Models to Debug and Self-Refine**  
  *Xinyun Chen, Maxwell Lin, Nathanael Schärli, Denny Zhou.* (ICML 2023)  
  Demonstrated that models improve accuracy through runtime execution feedback and explanation generation.  
  [[ArXiv](https://arxiv.org/abs/2304.05128)]

---

## 4. Open Foundation Models for Code

- **Qwen2.5-Coder Technical Report**  
  *Binyuan Hui, Jian Yang, Zeyu Cui, Jiaxi Yang, Dayiheng Liu, Lei Zhang, Tianyu Liu, Baosong Zhang, Bowen Yu, Kai Dang, et al.* (2024)  
  Detailed the architecture, synthetic data pipelines, and multi-stage pre-training of the 0.5B–32B code models.  
  [[ArXiv](https://arxiv.org/abs/2409.12186)]

- **DeepSeek-Coder: When the Large Language Model Meets Programming**  
  *Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang, Guanting Chen, Xiao Bi, Y. Wu, Y.K. Li, et al.* (2024)  
  Pre-trained on 2 trillion code tokens using Fill-in-the-Middle (FIM) and project-level context.  
  [[ArXiv](https://arxiv.org/abs/2401.14196)]

- **CodeLlama: Open Foundation Models for Code**  
  *Baptiste Rozière, Jonas Gehring, Fabian Gloeckle, Sten Sootla, Itai Gat, Xiaoqing Ellen Tan, Yossi Adi, Jingyu Liu, Tal Remez, Jérémy Rapin, et al.* (2023)  
  Specialized Llama 2 with infilling capability and long-context (100k) adaptation.  
  [[ArXiv](https://arxiv.org/abs/2308.12950)]

---

## 5. Developer Productivity Studies

- **The Impact of AI on Developer Productivity: Evidence from GitHub Copilot**  
  *Sida Peng, Eirini Kalliamvakou, Peter Cihon, Mert Demirer.* (2023)  
  Controlled trial showing developers completed tasks 55.8% faster with AI assistance.  
  [[ArXiv](https://arxiv.org/abs/2302.06590)]

---

## 6. BibTeX Citations

```bibtex
@inproceedings{jimenez2024swebench,
  title     = {SWE-bench: Can Language Models Resolve Real-World GitHub Issues?},
  author    = {Jimenez, Carlos E. and Yang, John and Wettig, Alexander and Yao, Shunyu and Pei, Kexin and Press, Ofir and Narasimhan, Karthik},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2024}
}

@article{chen2021codex,
  title     = {Evaluating Large Language Models Trained on Code},
  author    = {Chen, Mark and Tworek, Jerry and Jun, Heewoo and Yuan, Qiming and de Oliveira Pinto, Henrique Ponde and Kaplan, Jared and Edwards, Harri and Burda, Yuri and Joseph, Nicholas and Brockman, Greg and others},
  journal   = {arXiv preprint arXiv:2107.03374},
  year      = {2021}
}

@inproceedings{zhang2023repocoder,
  title     = {RepoCoder: Repository-Level Code Completion Through Iterative Retrieval and Generation},
  author    = {Zhang, Fengji and Chen, Bei and Zhang, Yue and Liu, Jacky and Lou, Jian-Guang},
  booktitle = {Empirical Methods in Natural Language Processing (EMNLP)},
  year      = {2023}
}

@article{yang2024sweagent,
  title     = {SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering},
  author    = {Yang, John and Jimenez, Carlos E. and Wettig, Alexander and Lieret, Kilian and Yao, Shunyu and Narasimhan, Karthik and Press, Ofir},
  journal   = {arXiv preprint arXiv:2405.15793},
  year      = {2024}
}

@article{hui2024qwen25coder,
  title     = {Qwen2.5-Coder Technical Report},
  author    = {Hui, Binyuan and Yang, Jian and Cui, Zeyu and Yang, Jiaxi and Liu, Dayiheng and Zhang, Lei and Liu, Tianyu and Zhang, Baosong and Yu, Bowen and Dang, Kai and others},
  journal   = {arXiv preprint arXiv:2409.12186},
  year      = {2024}
}

@misc{sajjadi2026awesomecoding,
  title        = {Awesome AI Coding Tools: A Curated Taxonomy of Agents, Architectures, and Research},
  author       = {Sajjadi, Mahmoud},
  year         = {2026},
  howpublished = {\url{https://github.com/mahmoudsajjadi/awesome-ai-coding-tools}}
}
```
