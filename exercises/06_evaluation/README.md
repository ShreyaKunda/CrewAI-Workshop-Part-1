# Exercise 6: Quick Evaluation

## What You'll Learn

In this exercise, you'll learn to:

- Evaluate agent outputs critically
- Identify **hallucinations** (AI-generated false information)
- Assess **task completion** accuracy
- Understand the importance of **human oversight**
- Design workflows with validation and review

## Key Evaluation Questions

Before considering an agent workflow successful, ask these questions:

### 1. Did the agent give the correct answer?

- AI-generated output is **not automatically correct**
- Verify facts against reliable sources
- Check for logical consistency

### 2. Did the agent follow the task?

- Compare actual output with the `expected_output` defined in the task
- Did it address all parts of the task description?
- Is the format/structure what was requested?

### 3. Did the agent hallucinate?

**Hallucination** = When an AI system generates information that is:
- **Incorrect** (factually wrong)
- **Unsupported** (not based on available data)
- **Made up** (invented details)

### 4. Did the second agent trust the first agent too much?

In a multi-agent system, errors cascade:

```
Researcher
    ↓
Incorrect information
    ↓
Analyst
    ↓
Incorrect conclusion
```

**More agents ≠ Better results**

### 5. How can we improve the workflow?

Possible approaches:

- ✅ Better task descriptions
- ✅ Better expected outputs
- ✅ Validation steps
- ✅ Multiple sources
- ✅ Structured outputs
- ✅ Human review gates
- ✅ Automated evaluation

## How to Run

### Prerequisites

- Complete Exercises 1-5 first
- Python virtual environment activated
- Dependencies installed: `pip install -r ../../requirements.txt`
- Ollama running: `ollama serve`

### Execute and Evaluate

1. Run Exercise 5 (Create a Crew):

```bash
cd ../05_create_crew
python crew.py
```

2. **Carefully review the output**:
   - Is the research factually accurate?
   - Is the analysis based on the research?
   - Are there any obvious errors or made-up details?
   - Would you trust this information for a real decision?

## Discussion Questions

### 💭 Critical Thinking

**If an AI agent is making decisions inside a real software or cybersecurity workflow, where should a human be involved?**

Consider:
- Security decisions affecting infrastructure
- Data analysis for compliance
- Risk assessments for vulnerabilities
- Incident response recommendations

### Key Insight

> **The goal is NOT to remove humans from every workflow.**
>
> **The goal is to determine where AI can assist effectively and where human oversight is necessary.**

## Validation Checklist

For each agent output, verify:

- [ ] **Accuracy**: Facts are correct
- [ ] **Completeness**: All aspects of the task were addressed
- [ ] **Consistency**: No contradictions within the output
- [ ] **Source**: Can you verify where the information came from?
- [ ] **Hallucinations**: Are there invented details?
- [ ] **Bias**: Is the response balanced or one-sided?
- [ ] **Trustworthiness**: Would you rely on this for important decisions?

## Real-World Application

### Example: Security Incident Response

❌ **Bad**: Agent makes blocking decisions without human review
✅ **Good**: Agent analyzes logs → alerts human analyst → human approves action

### Example: Code Review

❌ **Bad**: Agent merges code automatically
✅ **Good**: Agent suggests improvements → human reviews → human approves merge

## Next Steps

Congratulations! You've completed the workshop. You now understand:

1. ✅ How to create AI agents
2. ✅ How to assign tasks to agents
3. ✅ How to give agents tools
4. ✅ How to build multi-agent workflows
5. ✅ How to evaluate agent outputs

Use these skills responsibly! 🚀
