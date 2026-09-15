# Crew AI Workshop Part 1

A hands-on workshop for building AI agents and multi-agent workflows using **CrewAI** and **Ollama**.

---

# Table of Contents

* [Workshop Goal](#workshop-goal)
* [1. Before You Begin](#1-before-you-begin)

  * [Required Software](#required-software)
  * [Check Your Dependencies](#check-your-dependencies)
  * [Check Python](#check-python)
  * [Check pip](#check-pip)
  * [Check Git](#check-git)
  * [Check Ollama](#check-ollama)
  * [Check Your Ollama Model](#check-your-ollama-model)
* [2. Test Ollama](#2-test-ollama)
* [3. Clone the Repository](#3-clone-the-repository)
* [4. Create a Virtual Environment](#4-create-a-virtual-environment)
* [5. Install the Workshop Dependencies](#5-install-the-workshop-dependencies)
* [6. Run Your First Workshop Exercise](#6-run-your-first-workshop-exercise)

---

# Workshop Goal

By the end of Part 1, you will be able to:

* Create an AI agent
* Define an agent's role, goal, and backstory
* Assign tasks to an agent
* Give an agent a tool
* Create specialized agents
* Pass information between agents
* Build a multi-agent Crew

---

# 1. Before You Begin

Before starting the workshop, make sure the following are installed on your computer. If you have already set everything up, you can skip the installation and setup steps and proceed directly to the exercises.

## Required Software

| Software | Required | Check Command      |
| -------- | -------- | ------------------ |
| Python   | Yes      | `python --version` |
| Git      | Yes      | `git --version`    |
| Ollama   | Yes      | `ollama --version` |

You will also need to pull a model using Ollama.

---

## Check Your Dependencies

Open a terminal and run the following commands one by one.

### Check Python

```bash
python --version
```

You should see something similar to:

```text
Python 3.11.x
```

Python 3.10+ is recommended for the workshop.

If `python` does not work, try:

```bash
python3 --version
```


---

### Check Git

```bash
git --version
```

You should see something similar to:

```text
git version 2.x.x
```

---

### Check Ollama

```bash
ollama --version
```

If Ollama is not installed, download it from:

https://ollama.com

After installing Ollama, restart your terminal and run:

```bash
ollama --version
```

---

### Check Your Ollama Model

Run:

```bash
ollama list
```

You should see `llama3.2` in the list.

If you do not have it, download it using:

```bash
ollama pull llama3.2
```

This may take some time depending on your internet connection.

---

# 2. Test Ollama

Before continuing with the workshop setup, make sure that Ollama is working correctly.

Run:

```bash
ollama run llama3.2
```

You should be able to interact with the model directly from your terminal.

Try asking:

```text
What is an AI agent?
```

If you receive a response, Ollama is working correctly.

To exit the Ollama session, use:

```text
/bye
```

or press:

```text
Ctrl+C
```

If this works, you are ready to continue.

---

# 3. Clone the Repository

Once your dependencies are ready, clone the workshop repository.

Run:

```bash
git clone https://github.com/ShreyaKunda/CrewAI-Workshop-Part-1.git
```

Move into the repository:

```bash
cd CrewAI-Workshop-Part-1
```

You can verify that you are inside the repository by running:

```bash
dir
```

on Windows, or:

```bash
ls
```

on macOS/Linux.

You should see files and folders such as:

```text
README.md
requirements.txt
exercises
data
solutions
```

---

# 4. Create a Virtual Environment

A virtual environment keeps the workshop dependencies separate from other Python projects on your computer.

## Windows

Run:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

After activation, you should see something similar to:

```text
(.venv)
```

at the beginning of your terminal.

## macOS / Linux

Run:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

---

# 5. Install the Workshop Dependencies

Make sure your virtual environment is activated.

Then run:

```bash
pip install -r requirements.txt
```

This installs the Python packages required for the workshop.

You can verify that CrewAI is installed with:

```bash
pip show crewai
```

---

# 6. Run Your First Workshop Exercise

The exercises are located inside:

```text
exercises/
```


If everything is configured correctly, the agent should run using your local Ollama model. You are now ready for the workshop.

---

