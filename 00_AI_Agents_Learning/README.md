# AI Agents Learning — Reply Code Challenge 2025

This folder contains the **tutorial notebooks** for the Reply Code Challenge AI Agents learning path.  
The notebooks are designed to be read and run **in order**, progressively building from a basic agent all the way to multi-agent orchestration with Langfuse-based cost tracking.

---

## 📂 Contents

| Notebook | Description |
|----------|-------------|
| [`Notebooks/00_AI_Agents.ipynb`](Notebooks/00_AI_Agents.ipynb) | Basic LangChain agent creation via OpenRouter |
| [`Notebooks/01_00_AI_Agents_Tools.ipynb`](Notebooks/01_00_AI_Agents_Tools.ipynb) | Extending agents with custom tools using `@tool` |
| [`Notebooks/02_Multi_Agents.ipynb`](Notebooks/02_Multi_Agents.ipynb) | Multi-agent travel planning with the "Agents as Tools" pattern |
| [`Notebooks/03_Agent_Resource_Management.ipynb`](Notebooks/03_Agent_Resource_Management.ipynb) | Token usage and cost tracking with Langfuse |

---

## ⚡ Local Setup

### 1. Create and activate the virtual environment

A local `.venv` is already initialised in this folder with all required packages.

```bash
# From the 00_AI_Agents_Learning folder:
source .venv/bin/activate
```

If you ever need to recreate it from scratch:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install langchain langchain-openai langgraph python-dotenv langfuse ulid-py jupyter ipykernel
```

### 2. Configure your credentials

Copy your keys into the [`.env`](.env) file in this folder before running any notebook:

```
OPENROUTER_API_KEY=your-api-key-here
LANGFUSE_PUBLIC_KEY=pk-your-public-key-here
LANGFUSE_SECRET_KEY=sk-your-secret-key-here
LANGFUSE_HOST=https://challenges.reply.com/langfuse
TEAM_NAME=your-team-name
```

| Variable | Where to get it |
|----------|----------------|
| `OPENROUTER_API_KEY` | [openrouter.ai](https://openrouter.ai) → Keys → Create Key |
| `LANGFUSE_PUBLIC_KEY` | Provided by the challenge organisers |
| `LANGFUSE_SECRET_KEY` | Provided by the challenge organisers |
| `LANGFUSE_HOST` | `https://challenges.reply.com/langfuse` (fixed) |
| `TEAM_NAME` | Your team name (used to prefix session IDs) |

### 3. Launch Jupyter

```bash
jupyter notebook Notebooks/
```

---

## 📖 Notebook Order

Run the notebooks **in sequence** — each one builds on the previous:

1. **`00_AI_Agents.ipynb`** — Create your first agent with a system prompt via OpenRouter  
2. **`01_00_AI_Agents_Tools.ipynb`** — Add a temperature conversion tool; learn the `@tool` decorator  
3. **`02_Multi_Agents.ipynb`** — Build a travel planner with Logistics + Recommendations specialists  
4. **`03_Agent_Resource_Management.ipynb`** — Integrate Langfuse; track tokens, costs, and latency  

Each notebook includes:
- **Markdown explanation cells** — Concepts, architecture diagrams, and design rationale
- **Executable code cells** — Ready-to-run, self-contained code
- **Inline `%pip install`** — No external `requirements.txt` needed

---

## 🗂 Folder Structure

```
00_AI_Agents_Learning/
├── .env                         # Your credentials (not committed to git)
├── .venv/                       # Local virtual environment
├── README.md                    # This file
├── Notebooks/
│   ├── 00_AI_Agents.ipynb
│   ├── 01_00_AI_Agents_Tools.ipynb
│   ├── 02_Multi_Agents.ipynb
│   └── 03_Agent_Resource_Management.ipynb
└── TXT/                         # Original instructions used to generate notebooks
    ├── 00_AI_Agent.txt
    ├── 01_AI_Agent_Tools.txt
    ├── 02_Multi_Agents.txt
    └── 03_Agent_Resource_Management.txt
```

---

## 🔒 Notes

- The `.env` file **must live in this folder** for `load_dotenv()` to find it automatically.
- The `.venv` directory is local and **should not be committed** (it is in `.gitignore`).
- For the challenge, always use **Langfuse session IDs** to group all resource usage for a single run. Session IDs follow the format `{TEAM_NAME}-{ULID}`.
- All notebooks use `gpt-4o-mini` via OpenRouter as the default model. You can change the `model` parameter to experiment with other models.
