from crewai import Agent, LLM
from crewai_tools import FileReadTool


llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)


# A simple local tool for reading the workshop data file
@tool("Read sample data")
def read_sample_data() -> str:
    """Read the sample dataset provided for the workshop."""
    with open("data/sample_data.txt", "r", encoding="utf-8") as file:
        return file.read()


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
