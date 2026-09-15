# Exercise 3: Give an Agent a Tool

## What You'll Learn

In this exercise, you'll learn how to:

- Equip an agent with a **tool**
- Build a simple custom tool for reading local data
- Let an agent access information that is not contained in its prompt
- See how tools extend what an agent can do

## The Task

Complete the TODO in `agent_with_tool.py`:

1. Review the `read_sample_data` tool
2. **Change the question** and observe how the agent uses its file-reading tool
3. Try different questions about the `data/sample_data.txt` file

## How to Run

From the repository root, run:

```bash
python exercises/03_agent_tool/agent_with_tool.py
```

The agent will access the product sales data from `data/sample_data.txt` through its custom tool.

## Expected Output

You should see:

1. Verbose logs showing the agent deciding to use its tool
2. The tool reading the file contents
3. The agent analyzing the data and answering your question

## Sample Data

The tool has access to this data:

```text
Product,Sales
Laptop,120
Phone,250
Tablet,80
Monitor,150
Keyboard,200
Mouse,175
```

## Try These Questions

1. "What's the product with the highest sales?"
2. "Which products have sales above 150?"
3. "Calculate the average sales across all products."
4. "Rank products by sales from highest to lowest."

## Key Idea

An agent can reason using its LLM, but a **tool gives it an additional capability**. Here, the tool gives the agent access to a local file.

## Next Steps

Once this exercise works, move to **Exercise 4** to create multiple specialized agents.
