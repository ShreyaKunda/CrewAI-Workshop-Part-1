# Exercise 1: Create Your First AI Agent

## What You'll Learn

In this exercise, you'll create your first AI agent using CrewAI. You'll understand:

- How to define an agent's **role**
- How to set an agent's **goal**
- How to create a **backstory** that gives context to the agent
- How to connect to Ollama for local LLM access
- How to run an agent with `kickoff()`

## The Task

Complete the TODOs in `agent.py`:

1. **Create a Researcher Agent** with:
   - A meaningful `role` (e.g., "AI Researcher")
   - A clear `goal` (e.g., "Explain AI concepts clearly")
   - A descriptive `backstory` (e.g., "You are an expert in explaining complex topics")

## How to Run

### Prerequisites

- Python virtual environment activated
- Dependencies installed: `pip install -r ../../requirements.txt`
- Ollama running: `ollama serve`
- Model downloaded: `ollama pull llama3.2`

### Execute the Exercise

```bash
python agent.py
```

The agent will respond to: *"Explain what Artificial Intelligence is in simple terms."*

## Expected Output

You should see:

1. Verbose logs showing the agent's thinking process
2. A clear, simple explanation of AI from the agent

## 💡 Tips

- The `verbose=True` setting shows the agent's internal reasoning
- A good backstory helps the agent understand its context and respond better
- The agent will use the local Ollama model without any API keys

## Next Steps

Once this exercise works, move to **Exercise 2** to learn how to assign tasks to agents.
