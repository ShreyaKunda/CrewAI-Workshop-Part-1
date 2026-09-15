from crewai import Agent, LLM
from crewai.tools import tool


@tool("Read sample data")
def read_sample_data() -> str:
    """Read the sample dataset provided for the workshop."""
    with open("data/sample_data.txt", "r", encoding="utf-8") as file:
        return file.read()


llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)

analyst = Agent(
    role="Data Analyst",
    goal="Read the provided data and answer questions about it.",
    backstory="You are a careful analyst who works with simple datasets.",
    tools=[read_sample_data],
    llm=llm,
    verbose=True
)

result = analyst.kickoff(
    "Read the sample data and identify the product with the highest sales."
)

print("\n--- Agent Response ---")
print(result)
