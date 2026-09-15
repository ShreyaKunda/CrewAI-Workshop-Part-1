# Exercise 4: Build Two Specialized Agents

## What You'll Learn

In this exercise, you'll learn how to:

- Create **multiple agents** with different specializations
- Pass information from one agent to another
- Build a **simple workflow** where agents work sequentially
- Understand how agents can build on each other's work

## The Task

Complete the TODOs in `multi_agent_workflow.py`:

1. **Researcher Agent** (already defined)
   - Researches cybersecurity topics

2. **Create an Analyst Agent** with:
   - A meaningful `role` (e.g., "Security Analyst")
   - A clear `goal` (e.g., "Analyze research and identify key risks")
   - A descriptive `backstory`

3. **Create an Analysis Task** that:
   - Takes the research task output as `context`
   - Analyzes the research findings

4. **Run both tasks** together

## How to Run

### Execute the Exercise

```bash
python multi_agent_workflow.py
```

The agents will research phishing attacks and then analyze the findings.

## Expected Output

You should see:

1. The **Researcher** completes its task
2. The **Analyst** receives the research as context
3. The Analyst produces its own analysis



## Key Concept: Task Dependencies

```
Research Task
     ↓ (output becomes context)
Analysis Task
```

## Potential Issues

⚠️ **Important**: If the Analyst task doesn't run automatically, see Exercise 5 (Create a Crew) for the proper way to orchestrate multiple tasks.

## Next Steps

Once this exercise works, move to **Exercise 5** to formalize this workflow with a Crew.
