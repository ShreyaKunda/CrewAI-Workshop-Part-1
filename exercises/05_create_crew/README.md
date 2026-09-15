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


