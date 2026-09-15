# Exercise 2: Assign Tasks to an Agent

## What You'll Learn

In this exercise, you'll learn how to:

- Create a **Task** with a clear description
- Define **expected output** for a task
- Assign a task to an agent
- Run tasks with structured inputs

## The Task

Complete the TODOs in `agent_with_task.py`:

1. **Create a Research Task** with:
   - A clear `description` of what the agent should do
   - An `expected_output` that defines what you want to receive

2. **Run the task** using the agent with an input topic

## How to Run

### Execute the Exercise

```bash
python agent_with_task.py
```

The agent will research the topic: *"Artificial Intelligence"*

## Expected Output

You should see:

1. Verbose logs showing the agent working on the task
2. A structured response about AI based on the expected output format

## Key Differences from Exercise 1

- **Exercise 1**: Direct question passed to `kickoff()`
- **Exercise 2**: Structured task with description and expected output

## Next Steps

Once this exercise works, move to **Exercise 3** to give agents tools.
