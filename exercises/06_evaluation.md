# Exercise 6 — Quick Evaluation

Before considering an agent workflow successful, ask:

## 1. Did the agent give the correct answer?

AI-generated output is not automatically correct.

## 2. Did the agent follow the task?

Compare the actual output with the expected output defined in the task.

## 3. Did the agent hallucinate?

A hallucination occurs when an AI system generates information that is incorrect, unsupported or made up.

## 4. Did the second agent trust the first agent too much?

In a multi-agent system, an error from one agent can be passed to another agent.

```text
Researcher
    ↓
Incorrect information
    ↓
Analyst
    ↓
Incorrect conclusion
```

More agents do not automatically mean better results.

## 5. How can we improve the workflow?

Possible approaches:

- Better task descriptions
- Better expected outputs
- Validation steps
- Multiple sources
- Structured outputs
- Human review
- Automated evaluation

## 💭 Discussion

If an AI agent is making decisions inside a real software or cybersecurity workflow, where should a human be involved?

The goal is not to remove humans from every workflow. The goal is to determine where AI can assist effectively and where human oversight is necessary.
