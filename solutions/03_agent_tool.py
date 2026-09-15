from crewai import Agent, LLM
from crewai_tools import FileReadTool


llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)


tool = FileReadTool(file_path="data/sample_data.txt")


analyst = Agent(
    role="Data Analyst",
    goal="Read the provided data and answer questions about it",
    backstory="You are a careful analyst who works with simple datasets.",
    tools=[tool],
    llm=llm,
    verbose=True
)


result = analyst.kickoff(
    "Read data/sample_data.txt and identify the product with the highest sales."
)

print("\n--- Agent Response ---")
print(result)
