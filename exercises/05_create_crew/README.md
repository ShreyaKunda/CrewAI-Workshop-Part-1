# Exercise 5: Create a Crew

## What You'll Learn

In this exercise, you'll learn how to:

- Formalize multiple agents into a **Crew**
- Orchestrate tasks automatically with a Crew
- Ensure tasks run in the correct sequence
- Build a complete **multi-agent workflow**

## The Task

Complete the TODOs in `crew.py`:

1. **Create the Researcher Agent** (role, goal, backstory)
2. **Create the Analyst Agent** (role, goal, backstory)
3. **Assemble a Crew** with:
   - The list of agents
   - The list of tasks in order
   - `verbose=True` to see the workflow

4. **Run the Crew** using `crew.kickoff()`

## How to Run

### Prerequisites

- Python virtual environment activated
- Dependencies installed: `pip install -r ../../requirements.txt`
- Ollama running: `ollama serve`
- Model downloaded: `ollama pull llama3.2`

### Execute the Exercise

```bash
python crew.py
```

The Crew will orchestrate both agents to research and analyze phishing risks.

## Expected Output

You should see:

1. The **Researcher Agent** completes its research task
2. Output is automatically passed to the **Analyst Agent**
3. The **Analyst Agent** analyzes the research
4. Final output from the Crew

## 💡 Tips

- A **Crew** is a container for agents and tasks
- The Crew automatically handles task sequencing based on `context`
- `verbose=True` shows the entire workflow execution
- All agents in a crew share the same LLM instance

## Crew Workflow

```
┌─────────────────────────┐
│   Multi-Agent Crew      │
├─────────────────────────┤
│                         │
│  Researcher Agent       │
│      ↓                  │
│  Research Task          │
│      ↓                  │
│  Analyst Agent          │
│      ↓                  │
│  Analysis Task          │
│      ↓                  │
│  Final Output           │
│                         │
└─────────────────────────┘
```

## Key Differences from Exercise 4

- **Exercise 4**: Manual task execution, limited task chaining
- **Exercise 5**: Crew-based orchestration, automatic sequencing

## Next Steps

Once this exercise works, you've completed the core multi-agent workflow! Move to **Exercise 6** to learn about evaluation and human oversight.
