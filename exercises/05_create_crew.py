from crewai import Agent, Task, Crew, LLM


llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)


# TODO 1: Create the Researcher agent.
researcher = Agent(
    role="Researcher",
    goal="Research a cybersecurity topic",
    backstory="You are a careful cybersecurity researcher.",
    llm=llm,
    verbose=True
)


# TODO 2: Create the Analyst agent.
analyst = Agent(
    role="TODO",
    goal="TODO",
    backstory="TODO",
    llm=llm,
    verbose=True
)


research_task = Task(
    description="Research the major risks associated with phishing attacks.",
    expected_output="A concise research summary.",
    agent=researcher
)


analysis_task = Task(
    description="Analyse the research and identify the three most important risks.",
    expected_output="Three key risks with short explanations.",
    agent=analyst,
    context=[research_task]
)


# TODO 3: Assemble the agents and tasks into a Crew.
crew = Crew(
    agents=[researcher, analyst],
    tasks=[research_task, analysis_task],
    verbose=True
)


# TODO 4: Kick off the Crew.
result = crew.kickoff()

print("\n--- Final Crew Output ---")
print(result)
