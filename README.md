# AI Agents - Reply Code Challenge 2026

This repository contains the full learning path and challenge materials for the **Reply Code Challenge 2025 — AI Agents** track.

---

## 📁 Repository Structure

```
.
├── .gitignore
├── README.md                        ← You are here
├── .venv/                           ← Root virtual environment (optional)
│
├── 00_AI_Agents_Learning/           ← Tutorial notebooks (start here)
│   ├── .env                         ← Your API credentials
│   ├── .venv/                       ← Learning section virtual environment
│   ├── README.md
│   ├── Notebooks/
│   │   ├── 00_AI_Agents.ipynb
│   │   ├── 01_00_AI_Agents_Tools.ipynb
│   │   ├── 02_Multi_Agents.ipynb
│   │   └── 03_Agent_Resource_Management.ipynb
│   └── TXT/                         ← Original instructions used to build notebooks
│
├── 01_AI_Agents_Training/           ← Training exercises
│   └── README.md
│
└── 02_AI_Agents_Challenge/          ← The actual challenge solution
    └── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10–3.13 (avoid 3.14 — Langfuse compatibility issues)
- An [OpenRouter](https://openrouter.ai) API key (free)
- Langfuse credentials provided by the challenge organisers

### Quick Start

```bash
# 1. Clone the repo
git clone <this-repo-url>
cd AI_Agents_Reply_Challenge

# 2. Enter the learning section
cd 00_AI_Agents_Learning

# 3. Activate the virtual environment
source .venv/bin/activate

# 4. Fill in your credentials
nano .env   # or use your preferred editor

# 5. Launch Jupyter
jupyter notebook Notebooks/
```

---

## 📚 Learning Path

The `00_AI_Agents_Learning` section contains **four progressive tutorials**:

| #   | Notebook                 | Concepts                                     |
| --- | ------------------------ | -------------------------------------------- |
| 01  | Basic Agent Creation     | LangChain, OpenRouter, system prompts        |
| 02  | Tools & Function Calling | `@tool` decorator, automatic tool selection  |
| 03  | Multi-Agent Systems      | Orchestrator pattern, "Agents as Tools"      |
| 04  | Resource Management      | Langfuse tracing, session IDs, cost tracking |

See [`00_AI_Agents_Learning/README.md`](00_AI_Agents_Learning/README.md) for full setup and usage instructions.

---

## 🔧 Tech Stack

| Library                                                                         | Purpose                                        |
| ------------------------------------------------------------------------------- | ---------------------------------------------- |
| [LangChain](https://python.langchain.com/)                                      | Agent framework and tool abstractions          |
| [LangGraph](https://langchain-ai.github.io/langgraph/)                          | ReAct agent execution engine                   |
| [langchain-openai](https://python.langchain.com/docs/integrations/chat/openai/) | OpenAI-compatible model connector              |
| [OpenRouter](https://openrouter.ai/)                                            | Unified LLM API gateway                        |
| [Langfuse](https://langfuse.com/)                                               | Observability: token tracking, cost monitoring |
| [ulid-py](https://github.com/mdomke/python-ulid)                                | Unique session ID generation                   |
| [python-dotenv](https://github.com/theskumar/python-dotenv)                     | `.env` file loading                            |

---

## 🔒 Security

- **Never commit your `.env` file.** It is excluded by `.gitignore`.
- API keys and Langfuse credentials must be kept private.
- The `.venv` directories are also excluded from version control.
