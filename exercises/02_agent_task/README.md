# Exercise 2: Assign Tasks to an Agent

## What You'll Learn

In this exercise, you'll learn how to:

- Create a **Task** with a clear description
- Define **expected output** for a task
- Assign a task to an agent
- Execute a task through a Crew
- Run tasks with structured inputs

## The Task

Complete the TODOs in `agent_with_task.py`:

1. **Create a Research Task** with:
   - A clear `description` of what the agent should do
   - An `expected_output` that defines what you want to receive

2. **Create a one-agent Crew** containing the researcher and the task

3. **Run the Crew** with an input topic

## How to Run

From the repository root, run:

```bash
python exercises/02_agent_task/agent_with_task.py
```

The agent will research the topic: *"Artificial Intelligence"*

## Expected Output

You should see:

1. Verbose logs showing the agent working on the task
2. A structured response based on the task description and expected output

## Key Differences from Exercise 1

- **Exercise 1**: A direct question is passed to an agent
- **Exercise 2**: A Task defines what the agent should do, and a Crew executes that Task

## Key Idea

A **Task** describes the work. A **Crew** is the mechanism that executes and orchestrates tasks with agents.

## Next Steps

Once this exercise works, move to **Exercise 3** to give agents tools.
