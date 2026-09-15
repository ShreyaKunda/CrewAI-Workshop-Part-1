from crewai import Agent, Task, LLM


llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)


researcher = Agent(
    role="Researcher",
    goal="Research a topic and provide accurate information",
    backstory="You are a researcher who explains technical topics clearly.",
    llm=llm,
    verbose=True
)


research_task = Task(
    description="""
    Research the topic: {topic}

    Explain:
    1. What it is
    2. Why it is important
    3. One real-world example
    """,
    expected_output="""
    A short explanation containing:
    - Definition
    - Importance
    - Real-world example
    """,
    agent=researcher
)


result = researcher.kickoff(
    "Research Artificial Intelligence. Explain what it is, why it is important, and give one real-world example."
)

print("\n--- Task Result ---")
print(result)
