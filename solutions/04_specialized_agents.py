from crewai import Agent, Task, LLM


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
    goal="Analyse research and identify the most important security risks",
    backstory="You are a cybersecurity analyst who turns research into useful insights.",
    llm=llm,
    verbose=True
)


research_task = Task(
    description="Research the major risks associated with phishing attacks.",
    expected_output="A concise research summary about phishing risks.",
    agent=researcher
)


analysis_task = Task(
    description="Analyse the research and identify the three most important risks.",
    expected_output="Three key risks with short explanations.",
    agent=analyst,
    context=[research_task]
)


# Execute the workflow sequentially.
research_result = researcher.kickoff(
    "Research the major risks associated with phishing attacks."
)

analysis_result = analyst.kickoff(
    f"Analyse the following research and identify the three most important risks:\n\n{research_result}"
)

print("\n--- Research Result ---")
print(research_result)

print("\n--- Analysis Result ---")
print(analysis_result)
