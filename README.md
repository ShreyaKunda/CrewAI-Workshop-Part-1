# CrewAI + Ollama Agentic AI Workshop

A beginner-friendly, hands-on workshop for building AI agents and multi-agent workflows using **CrewAI** and **Ollama**.

## 🎯 Workshop Goal

By the end of Part 1, you will be able to:

- Create an AI agent
- Define an agent's role, goal and backstory
- Assign tasks to an agent
- Give an agent a tool
- Create specialized agents
- Pass information between agents
- Build a multi-agent Crew
- Understand basic agent evaluation and human oversight

## 🛠️ Technologies

- Python
- CrewAI
- Ollama
- Local LLM

No paid API key is required.

## 🚀 Setup

### 1. Clone the repository

```bash
git clone https://github.com/ShreyaKunda/CrewAI-Workshop-Part-1.git
cd CrewAI-Workshop-Part-1
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Download Ollama from https://ollama.com and verify:

```bash
ollama --version
```

### 5. Download a model

For example:

```bash
ollama pull llama3.2
```

Check available models:

```bash
ollama list
```

## 🧪 Workshop Exercises

| Exercise | What you learn |
|---|---|
| 1. Create Your First AI Agent | Role, goal, backstory and agent execution |
| 2. Assign Tasks to an Agent | Task description and expected output |
| 3. Give an Agent a Tool | File/data analysis using a tool |
| 4. Build Two Specialized Agents | Passing one agent's output to another |
| 5. Create a Crew | Basic multi-agent workflow |
| 6. Quick Evaluation | Hallucinations, evaluation and human oversight |

## 📁 Repository Structure

```text
CrewAI-Workshop-Part-1/
│
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── exercises/
│   ├── 01_first_agent.py
│   ├── 02_agent_task.py
│   ├── 03_agent_tool.py
│   ├── 04_specialized_agents.py
│   ├── 05_create_crew.py
│   └── 06_evaluation.md
│
├── data/
│   └── sample_data.txt
│
└── solutions/
    ├── 01_first_agent.py
    ├── 02_agent_task.py
    ├── 03_agent_tool.py
    ├── 04_specialized_agents.py
    └── 05_create_crew.py
```

## 💡 Workshop Philosophy

The exercises are intentionally small. The goal is to understand the fundamental building blocks of Agentic AI rather than build a production application.

```text
Agent
  +
Task
  +
Tools
  +
Other Agents
  =
Multi-Agent Workflow
```

## ⚠️ Important

AI agents can produce incorrect or incomplete information. Always review important outputs and use human oversight where appropriate.
