## Exercise 5: Create a Crew

### What You'll Learn

In this exercise, you'll learn how to:

* Formalize multiple agents into a Crew
* Orchestrate tasks automatically with a Crew
* Pass outputs between agents using task context
* Ensure tasks run in the correct sequence
* Build a complete multi-agent workflow

### The Task

Complete the TODOs in `crew.py`:

Create the Researcher Agent (role, goal, backstory)

Create the Analyst Agent (role, goal, backstory)

Create the Security Advisor Agent (role, goal, backstory)

Assemble a Crew with:

* The list of agents
* The list of tasks in order
* `verbose=True` to see the workflow

Connect the tasks using `context` so that:

* The Analyst receives the Researcher's output
* The Security Advisor receives the Analyst's output

Run the Crew using `crew.kickoff()`

### How to Run

Execute the Exercise

```bash
python crew.py
```

The Crew will orchestrate the three agents to research, analyze, and recommend actions for phishing risks.

### Expected Output

You should see:

* The Researcher Agent completes its research task
* Output is passed to the Analyst Agent
* The Analyst Agent analyzes the research
* Output is passed to the Security Advisor
* The Security Advisor provides recommendations
* Final output from the Crew

### Crew Workflow

```text
┌─────────────────────────┐
│   Multi-Agent Crew      │
├─────────────────────────┤
│                         │
│  Researcher Agent       │
│      ↓                  │
│  Research Task          │
│      ↓                  │
│  Threat Analyst         │
│      ↓                  │
│  Analysis Task          │
│      ↓                  │
│  Security Advisor       │
│      ↓                  │
│  Recommendation Task    │
│      ↓                  │
│  Final Output           │
│                         │
└─────────────────────────┘
```

### Key Differences from Exercise 4

Exercise 4: Manual task execution and passing output between agents

Exercise 5: Crew-based orchestration, task context, and automatic sequencing
