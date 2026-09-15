from crewai import Agent, Task, LLM


llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)


# TODO 1: Create a Researcher agent.
researcher = Agent(
    role="Researcher",
    goal="Research a cybersecurity topic",
    backstory="You are a careful cybersecurity researcher.",
    llm=llm,
    verbose=True
)


# TODO 2: Create a specialized Analyst agent.
analyst = Agent(
    role="TODO",
    goal="TODO",
    backstory="TODO",
    llm=llm,
    verbose=True
)


research_task = Task(
    description="Research the major risks associated with phishing attacks.",
    expected_output="A concise research summary about phishing risks.",
    agent=researcher
)


# TODO 3: Create an analysis task that receives the research task output.
analysis_task = Task(
    description="TODO",
    expected_output="TODO",
    agent=analyst,
    context=[research_task]
)


# TODO 4: Run both tasks together as a simple workflow.
result = researcher.kickoff(
    "Research the major risks associated with phishing attacks."
)

print("\n--- Research Result ---")
print(result)

print("\nNow pass the research output to the Analyst task.")
