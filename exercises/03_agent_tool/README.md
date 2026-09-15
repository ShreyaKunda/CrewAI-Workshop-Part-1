# Exercise 3: Give an Agent a Tool

## What You'll Learn

In this exercise, you'll learn how to:

- Equip an agent with **tools**
- Use the **FileReadTool** to analyze local data
- Let agents access external resources to answer questions
- See how tools make agents more capable and accurate

## The Task

Complete the TODO in `agent_with_tool.py`:

1. **Change the question** and observe how the agent uses its file-reading tool
2. Try different questions about the `data/sample_data.txt` file

## How to Run

### Prerequisites

- Python virtual environment activated
- Dependencies installed: `pip install -r ../../requirements.txt`
- Ollama running: `ollama serve`
- Model downloaded: `ollama pull llama3.2`
- Sample data file exists: `data/sample_data.txt`

### Execute the Exercise

```bash
python agent_with_tool.py
```

The agent will analyze the product sales data from `data/sample_data.txt`.

## Expected Output

You should see:

1. Verbose logs showing the agent deciding to use the FileReadTool
2. The tool reading the file contents
3. The agent analyzing the data and answering your question

## Sample Data

The tool has access to this data:

```
Product,Sales
Laptop,120
Phone,250
Tablet,80
Monitor,150
Keyboard,200
Mouse,175
```

## 💡 Tips

- Tools extend what agents can do beyond just generating text
- The `FileReadTool` is from `crewai-tools` library
- Agents decide **when** to use a tool based on the task
- Without the tool, the agent couldn't access the actual data

## Try These Questions

1. "What's the product with the highest sales?"
2. "Which products have sales above 150?"
3. "Calculate the average sales across all products."
4. "Rank products by sales from highest to lowest."

## Next Steps

Once this exercise works, move to **Exercise 4** to create multiple specialized agents.
