from crewai import Agent, LLM
from crewai_tools import FileReadTool


llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)


# A simple local tool for reading the workshop data file
tool = FileReadTool(file_path="data/sample_data.txt")


researcher = Agent(
    role="Data Analyst",
    goal="Read the provided data and answer questions about it",
    backstory="You are a careful analyst who works with simple datasets.",
    tools=[tool],
    llm=llm,
    verbose=True
)


# TODO: Change the question and observe how the agent uses its tool.
result = researcher.kickoff(
    "Read the data file and identify the product with the highest sales."
)

print("\n--- Agent Response ---")
print(result)
