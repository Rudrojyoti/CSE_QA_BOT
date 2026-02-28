```
 ██████╗███████╗███████╗      ██████╗  █████╗
██╔════╝██╔════╝██╔════╝     ██╔═══██╗██╔══██╗
██║     ███████╗█████╗       ██║   ██║███████║
██║     ╚════██║██╔══╝       ██║▄▄ ██║██╔══██║
╚██████╗███████║███████╗     ╚██████╔╝██║  ██║
 ╚═════╝╚══════╝╚══════╝      ╚══▀▀═╝ ╚═╝  ╚═╝
         AI Computer Science Tutor
```

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-Phi3:mini-74AA9C?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Privacy](https://img.shields.io/badge/100%25-Local%20%26%20Private-green?style=for-the-badge)

**Your offline, privacy-first CS tutor — powered by local AI, no API keys, no data leaks.**

[🚀 Quick Start](#-quick-start) · [⚙️ Configuration](#️-configuration) · [🛣️ Roadmap](#️-roadmap) · [🤝 Contributing](#-contributing)

</div>

---

## TL;DR

> Ask CS questions by subject, get expert-level answers instantly — fully local, no cloud, no cost.

---

## 🎯 Live Demo & Architecture

> 🖥️ **Demo:** _Coming soon — GIF walkthrough placeholder_

```
┌─────────────────────────────────────────────────┐
│                   USER BROWSER                  │
│           Streamlit Frontend (:8501)            │
│    [Subject Selector] → [Question Input Box]    │
└──────────────────┬──────────────────────────────┘
                   │ HTTP POST /ask
┌──────────────────▼──────────────────────────────┐
│             Flask Backend (:5000)               │
│   Injects subject-aware system prompt           │
│   Validates + routes request                    │
└──────────────────┬──────────────────────────────┘
                   │ Ollama API (localhost:11434)
┌──────────────────▼──────────────────────────────┐
│           Ollama · Phi3:mini Model              │
│   Runs entirely on your machine — 100% private  │
└─────────────────────────────────────────────────┘
```

---

## 📸 Screenshots

| Subject Selector | Q&A Interface | Answer View |
|:---:|:---:|:---:|
| `[screenshot-subjects.png]` | `[screenshot-qa.png]` | `[screenshot-answer.png]` |

> 📌 Replace placeholders with actual screenshots after first run.

---

## 🚀 Quick Start

<details>
<summary><strong>1. Clone the repository</strong></summary>

```bash
git clone https://github.com/your-username/cse-qa.git
cd cse-qa
```
</details>

<details>
<summary><strong>2. Install dependencies</strong></summary>

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

`requirements.txt` includes: `flask`, `streamlit`, `requests`, `python-dotenv`
</details>

<details>
<summary><strong>3. Start Ollama + pull the model</strong></summary>

```bash
# Install Ollama → https://ollama.com/download
ollama pull phi3:mini
ollama serve                    # Runs on localhost:11434
```
</details>

<details>
<summary><strong>4. Launch both services</strong></summary>

```bash
# Terminal 1 — Flask backend
python app.py

# Terminal 2 — Streamlit frontend
streamlit run frontend.py
```

Then open **http://localhost:8501** 🎉
</details>

---

## ⚙️ Configuration

**Change the AI model:**
```python
# app.py
MODEL_NAME = "phi3:mini"        # swap for llama3, mistral, gemma, etc.
```

**Add a new CS subject:**
```python
# prompts.py
SUBJECTS["Distributed Systems"] = """
You are an expert in distributed systems. Explain concepts like CAP theorem,
consensus algorithms, and fault tolerance clearly with real-world examples.
"""
```

**Environment variables (`.env`):**
```env
FLASK_PORT=5000
OLLAMA_HOST=http://localhost:11434
DEBUG=false
```

---

## 📂 Project Structure

```
cse-qa/
├── app.py              # Flask API — /ask endpoint
├── frontend.py         # Streamlit UI
├── prompts.py          # Subject-specific system prompts
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🧠 Prompt Engineering Deep-Dive

CSE-QA uses **subject-scoped system prompts** to ground the model in a specific CS domain before answering.

```python
# prompts.py — simplified example
SUBJECTS = {
    "Algorithms": "You are an expert algorithms tutor. Focus on time/space complexity, \
                   proofs, and intuitive explanations. Use pseudocode examples.",
    "Operating Systems": "You are an OS expert. Cover processes, scheduling, memory \
                          management, and concurrency. Use analogies for clarity.",
    "Networks": "You are a networking specialist. Explain protocols, the OSI model, \
                 TCP/IP, and common vulnerabilities with practical examples.",
}

def build_prompt(subject, question):
    system = SUBJECTS.get(subject, "You are a helpful CS tutor.")
    return {"role": "system", "content": system}, \
           {"role": "user",   "content": question}
```

**Why it works:** Phi3:mini responds dramatically better when given a tight role definition. Subject prompts reduce hallucination and increase domain accuracy by keeping the model's attention anchored to a specific knowledge area.

---

## 🛣️ Roadmap

- [ ] 🌐 Multi-language support (Spanish, French, Hindi)
- [ ] 📚 RAG integration — index course notes & textbooks
- [ ] 🔐 User authentication + study session history
- [ ] 📊 Analytics dashboard (popular questions, weak topics)
- [ ] 🧪 Auto-generated practice problems per subject
- [ ] 🐳 Docker Compose for one-command setup

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

```bash
# Fork → clone → branch
git checkout -b feature/your-feature-name

# Make changes, then
git commit -m "feat: describe your change"
git push origin feature/your-feature-name
# Open a Pull Request
```

Please follow [Conventional Commits](https://www.conventionalcommits.org/) and keep PRs focused. Open an issue first for large changes.

---

## 📜 License

MIT © 2024 — free to use, modify, and distribute. See [`LICENSE`](./LICENSE) for details.

---

<div align="center">

Built with ❤️ for CS students everywhere · 100% local · 0% cloud · ∞ learning

⭐ Star this repo if CSE-QA helped you ace an exam!

</div>
