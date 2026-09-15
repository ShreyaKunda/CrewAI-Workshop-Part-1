from crewai import Agent, Task, Crew, LLM


llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)


researcher = Agent(
    role="Researcher",
    goal="Research a cybersecurity topic",
    backstory="You are a careful cybersecurity researcher.",
    llm=llm,
    verbose=True
)


analyst = Agent(
    role="Cybersecurity Analyst",
    goal="Analyse research and identify important security risks",
    backstory="You are an analytical cybersecurity professional who turns research into useful insights.",
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


crew = Crew(
    agents=[researcher, analyst],
    tasks=[research_task, analysis_task],
    verbose=True
)


result = crew.kickoff()

print("\n--- Final Crew Output ---")
print(result)
