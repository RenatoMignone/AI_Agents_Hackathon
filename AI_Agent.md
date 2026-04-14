# AI_Agent.md - Entry Point for AI Agents

This file is the primary context document for an AI agent working on the Reply Code Challenge 2026 (AI Agents track).
Read this file first. For deeper context on any section, read the README.md inside the relevant subfolder.
Do not read all subfolders at once - load only what you need to avoid unnecessary token consumption.

---

## What this challenge is

The Reply Code Challenge 2026 is a timed competitive programming event focused on building AI agent systems.

Challenge day: April 16th, 2026, 15:30 to 21:30 (6 hours).
Theme: Monitor. Adapt. Defend.

The problem domain is citizen welfare and behavioral anomaly detection.
A monitoring system tracks citizens over time using GPS location data, health event logs, and biometric indices.
The task is to identify which citizens are exhibiting anomalous behavior patterns that deviate from their established baseline.

The solution must be an agentic AI system where the LLM is the core decision-maker and orchestrator.
Purely deterministic or rule-based solutions are disqualified.
Every submission requires a Langfuse session ID for cost tracking and validation.

Discord clarification (challenge-day scoring, shared by organizers):
- Scoring is multi-criteria and weighted, not single-metric.
- Detection quality includes both count-based accuracy and economic accuracy.
- System performance includes cost, latency, and agent architecture quality.
- Metrics are benchmarked against an optimal reference; outperforming benchmark may earn bonus credit.
- More complex datasets carry higher maximum points.

---

## Repository overview

This repository contains three top-level sections, each with its own README.md:

```
AI_Agents_Reply_Challenge/
  AI_Agent.md                  - This file (entry point for AI agents)
  README.md                    - Human-oriented overview of the repo
  .gitignore                   - Excludes .env, .venv, build artifacts
  .venv/                       - Optional root virtual environment

  .scripts/                    - Environment setup scripts
    requirements.txt           - All Python dependencies for the entire project
    check_setup.py             - Verifies imports and .env credentials (run via 'make check')
    utils.py                   - Shared data loader utility for parsing dataset schemas

  00_AI_Agents_Learning/       - Tutorial notebooks, learn the stack before building
    README.md                  - Setup instructions, notebook order, credential configuration
    .venv/                     - Local virtual environment for the learning section
    Notebooks/                 - Four Jupyter notebooks, run in order
    TXT/                       - Original instructions used to generate the notebooks

  01_AI_Agents_Training/       - Sandbox training environment and practice materials
    README.md                  - Problem domain, dataset structure, submission interface description
    GUIDE.md                   - Step-by-step workflow for building and submitting sandbox solutions
    00_Sandbox_Sample_Material/ - Official materials from the organizers
      Sandbox_2026_V3.pdf      - Full problem statement (required reading before coding)
      Submission_Tracking.md   - Log of all submissions with scores and session IDs
      Public_Levels/           - Training datasets for levels 1, 2, 3
    01_Sandbox_Implementations/ - Where your sandbox solution code lives
    resources/                 - Screenshots of the challenge submission interface

  02_AI_Agents_Challenge/      - The actual challenge solution for April 16th
    README.md                  - Overview of this folder's contents
    00_How_It_Works/           - Official rules, scoring, and API integration reference
      README.md                - Competition rules, timeline, datasets, scoring, prizes
      submission_guide.md      - Challenge-day submission workflow, pitfalls, quick commands
      challenge_day_checklist.md - 60-second go/no-go checklist before final submit
      api_guidelines.md        - Langfuse integration code, env setup, best practices
      model_whitelist.md       - All ~200 whitelisted OpenRouter model IDs in a lookup table
    01_Implementation/         - Your actual challenge solution code goes here
      README.md                - (placeholder, fill as you build)
```

---

## How to navigate this repository as an AI agent

Start here (this file) to understand the overall context.

Then load only the README.md of the subfolder that is relevant to your current task:

- To set up the environment: run `make` from the repo root, then `cp .env.example .env` and fill in credentials, then `make check`
- If you are learning the stack or setting up dependencies: read 00_AI_Agents_Learning/README.md
- If you are building or testing a sandbox solution: read 01_AI_Agents_Training/README.md, then 01_AI_Agents_Training/GUIDE.md
- If you are preparing for or working on the real challenge: read 02_AI_Agents_Challenge/00_How_It_Works/README.md
- For challenge-day submission workflow and pitfalls: read 02_AI_Agents_Challenge/00_How_It_Works/submission_guide.md
- For final pre-submit go/no-go checks: read 02_AI_Agents_Challenge/00_How_It_Works/challenge_day_checklist.md
- If you need the Langfuse integration code: read 02_AI_Agents_Challenge/00_How_It_Works/api_guidelines.md
- If you need a model ID for ChatOpenAI: read 02_AI_Agents_Challenge/00_How_It_Works/model_whitelist.md

Do not read the problem statement PDF directly unless you have confirmed you need technical details beyond what is in the markdown files.

---

## Critical facts every submission must satisfy

1. Every submission (training and evaluation) requires a Langfuse session ID entered in the upload modal.
2. Session ID format: {TEAM_NAME}-{ULID}. Generate with generate_session_id() from api_guidelines.md.
3. Output file format: UTF-8 plain text. Content is specified in Sandbox_2026_V3.pdf.
4. Evaluation submissions: one per level, cannot be re-submitted. Also requires a source code zip.
5. Training submissions: unlimited, each shows a score that you can use to iterate.
6. Token budget on challenge day: $40 for datasets 1-3, $120 additional after submitting eval for all of 1-3.
7. No credits in sandbox mode: use only free OpenRouter models during training.
8. The LLM must make decisions. A rule-based wrapper around the LLM with no real reasoning is not valid.
9. Python 3.14 is incompatible with Langfuse. Use Python 3.10 through 3.13.
10. Final challenge scoring is weighted across detection quality and system performance; optimize for both quality and efficiency.
11. Evaluation outputs must be generated from evaluation/submission datasets, not from public training datasets.
12. Ignore __MACOSX extraction artifacts when loading datasets.

---

## Challenge-day rapid context (minimal load)

For fastest startup under token pressure, load only these files first:

1. AI_Agent.md
2. 02_AI_Agents_Challenge/00_How_It_Works/README.md
3. 02_AI_Agents_Challenge/00_How_It_Works/submission_guide.md
4. 02_AI_Agents_Challenge/00_How_It_Works/challenge_day_checklist.md (before final upload)

Then load additional files only if blocked.

---

## Challenge-day execution timeline (recommended)

- T+00 to T+30 min: validate env, run one end-to-end smoke test, verify Session ID and output format.
- T+30 to T+180 min: iterate on datasets 1-3 in training mode; optimize prompt/model config with tracked experiments.
- T+180 to T+300 min: lock architecture and run final generation for evaluation outputs.
- T+300 to T+360 min: perform checklist-based final upload sequence; avoid last-minute architecture changes.

---

## Optimization mandate for future AI agents

During challenge execution, optimize for the weighted scoring criteria communicated by organizers:

1. Detection quality (count-based accuracy and economic accuracy).
2. System performance (cost, latency, agent architecture quality).
3. Benchmark outperformance bonus potential.
4. Dataset difficulty weighting (higher complexity datasets can yield higher points).

Operational policy:

- Do not optimize only for raw detection count metrics.
- Prefer configurations that improve quality-per-cost and quality-per-latency.
- Use compact prompts by default; escalate to richer context only for uncertain cases.
- Keep the architecture explainable and clearly agentic (LLM as core decision-maker).
- Track each experiment with model, prompt version, review mode, score, cost, and latency.

---

## Technology stack

- LangChain: agent framework and tool abstractions
- LangGraph: ReAct agent execution engine
- langchain-openai: OpenAI-compatible model connector for OpenRouter
- OpenRouter: unified LLM API gateway (base_url: https://openrouter.ai/api/v1)
- Langfuse: observability platform (token tracking, cost monitoring, session grouping)
- ulid-py: unique session ID generation
- python-dotenv: .env file loading

Required environment variables - copy `.env.example` to `.env` in the **repository root** and fill in your values:

```bash
make          # creates root .venv and installs all dependencies
cp .env.example .env  # then fill in your real credentials
make check    # verifies the environment is fully working
```

```
OPENROUTER_API_KEY=your-key
LANGFUSE_PUBLIC_KEY=pk-your-key
LANGFUSE_SECRET_KEY=sk-your-key
LANGFUSE_HOST=https://challenges.reply.com/langfuse
TEAM_NAME=your-team-name
```

All scripts and notebooks use load_dotenv(find_dotenv()), which traverses up the directory tree from wherever they run, so the single root .env is found automatically by every subfolder.

Never commit the .env file. It is already listed in .gitignore. The .env.example is safe to commit.
