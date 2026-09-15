# CrewAI Workshop — Student Installation Guide

This guide prepares your computer for both Part 1 and Part 2 of the workshop.

The workshop uses:

- Python 3.11
- Git
- Ollama
- `llama3.2` running locally through Ollama
- CrewAI
- A Python virtual environment

No OpenAI, Gemini, Anthropic, or other paid API key is required.

---

# 1. What You Need Before the Workshop

| Requirement | Required | Purpose |
| --- | --- | --- |
| Python 3.11 | Yes | Runs the workshop code |
| Git | Yes | Downloads the workshop repositories |
| Ollama | Yes | Runs the local LLM |
| `llama3.2` | Yes | Model used by the workshop |
| VS Code | Recommended | Code editor |
| Internet connection | Required for setup | Download software, model, and Python packages |

You do **not** need:

- An OpenAI API key
- A Gemini API key
- A paid LLM subscription
- Docker

---

# 2. Recommended Setup

Please use **Python 3.11** for this workshop.

Using the same Python version helps avoid differences between student environments.

If you already have another Python version installed, that is fine. You can install Python 3.11 alongside it.

---

# 3. Install Python 3.11

## Windows

Download Python 3.11 from the official Python website:

https://www.python.org/downloads/

During installation:

1. Start the installer.
2. **Important:** enable **Add python.exe to PATH**.
3. Continue with the installation.
4. Restart your terminal after installation.

Verify it:

```bash
py -3.11 --version
```

You should see something similar to:

```text
Python 3.11.x
```

If `py` is not available, try:

```bash
python --version
```

## macOS / Linux

Check whether Python 3.11 is already installed:

```bash
python3.11 --version
```

If it is not installed, install Python 3.11 using the normal package manager for your operating system or from:

https://www.python.org/downloads/

Then verify again:

```bash
python3.11 --version
```

---

# 4. Install Git

Git is used to clone the workshop repositories.

Check whether Git is already installed:

```bash
git --version
```

If the command is not found, install Git from:

https://git-scm.com/downloads

After installation, restart your terminal and run:

```bash
git --version
```

---

# 5. Install Ollama

Ollama runs the LLM locally on your computer.

Download Ollama from:

https://ollama.com/download

Install it using the normal installer for your operating system.

After installation, open a **new terminal** and check:

```bash
ollama --version
```

You should see an Ollama version number.

If the command is not recognized, restart your terminal or restart Ollama.

---

# 6. Download the Workshop Model

The workshop uses the `llama3.2` model.

Run:

```bash
ollama pull llama3.2
```

This downloads the model to your computer. The download may take some time depending on your internet connection.

Check that it is installed:

```bash
ollama list
```

You should see `llama3.2` in the list.

---

# 7. Test Ollama Before Installing CrewAI

This step is important. Make sure the local model works before troubleshooting Python.

Run:

```bash
ollama run llama3.2
```

Then type:

```text
What is an AI agent?
```

If the model responds, Ollama is working.

Exit the model with:

```text
/bye
```

or press `Ctrl+C`.

---

# 8. Install VS Code

VS Code is recommended for the workshop because you will be editing Python files.

Download it from:

https://code.visualstudio.com/

After installing VS Code, install the **Python** extension from Microsoft.

You can also install the **Python Debugger** extension if VS Code recommends it.

---

# 9. Clone Part 1

Open a terminal and choose a folder where you want to keep the workshop repositories.

Run:

```bash
git clone https://github.com/ShreyaKunda/CrewAI-Workshop-Part-1.git
cd CrewAI-Workshop-Part-1
```

Check the files:

```bash
```

You should see files and folders including:

```text
README.md
INSTALLATION.md
requirements.txt
exercises/
data/
solutions/
```

---

# 10. Create a Virtual Environment

A virtual environment keeps the workshop's Python packages separate from the rest of your computer.

## Windows

From inside the Part 1 repository:

```bash
py -3.11 -m venv .venv
```

Activate it:

### Command Prompt

```bat
.venv\Scripts\activate
```

### PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, your terminal should show something similar to:

```text
(.venv) C:\...\CrewAI-Workshop-Part-1>
```

## macOS / Linux

Create the environment:

```bash
python3.11 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

You should see:

```text
(.venv)
```

at the beginning of your terminal prompt.

---

# 11. Upgrade pip

With the virtual environment activated, run:

```bash
python -m pip install --upgrade pip
```

---

# 12. Install the Workshop Dependencies

The workshop's Python dependency list is in `requirements.txt`.

Run:

```bash
pip install -r requirements.txt
```

The main Python dependency is:

```text
crewai
```

Ollama is **not** installed through pip. It is a separate application running locally on your computer.

---

# 13. Verify the Python Installation

Run:

```bash
python --version
```

Then:

```bash
pip show crewai
```

Finally, test the imports used by the workshop:

```bash
python -c "from crewai import Agent, Task, Crew, LLM; print('CrewAI import successful')"
```

You should see:

```text
CrewAI import successful
```

If you see that message, the Python environment is ready.

---

# 14. Test CrewAI + Ollama Together

Before starting the exercises, make sure Ollama is running and that `llama3.2` is available.

Run:

```bash
ollama list
```

Then, from the activated Python environment, run Exercise 1:

```bash
python exercises/01_first_agent/agent.py
```

The first request may take a little longer because the model needs to load.

You should see CrewAI processing the request and eventually an answer from the agent.

---

# 15. Open the Repository in VS Code

From the repository folder, you can run:

```bash
code .
```

If the `code` command is not available, open VS Code normally and choose:

**File → Open Folder → CrewAI-Workshop-Part-1**

In VS Code, make sure the Python interpreter is the one inside `.venv`.

It should look similar to:

```text
Python 3.11.x ('.venv')
```

---

# 16. Clone Part 2

Part 2 uses the same Python environment and dependencies.

You can clone it separately:

```bash
cd ..
git clone https://github.com/ShreyaKunda/CrewAI-Workshop-Part-2.git
cd CrewAI-Workshop-Part-2
```

You can either create a new virtual environment for Part 2 or reuse the same workshop environment.

For simplicity, if Part 1 is already working, you can reuse the same environment by activating it from the appropriate location.

The Part 2 repository does not need another dependency installation beyond the Part 1 environment.

Run Part 2 with:

```bash
python main.py
```

The completed incident report will be written to:

```text
output/incident_report.md
```

---

# 17. Final Pre-Workshop Checklist

Before the workshop starts, make sure all of these work:

```text
[ ] Python 3.11 installed
[ ] Git installed
[ ] Ollama installed
[ ] llama3.2 downloaded
[ ] ollama run llama3.2 works
[ ] Part 1 repository cloned
[ ] Virtual environment created
[ ] Virtual environment activated
[ ] requirements.txt installed
[ ] CrewAI import test works
[ ] Exercise 1 runs successfully
```

If all of these are working, you are ready for the workshop.

---

# Troubleshooting Guide

## Problem 1: `python` is not recognized

### Windows

Try:

```bash
py -3.11 --version
```

If this works, use `py -3.11` when creating the virtual environment:

```bash
py -3.11 -m venv .venv
```

If neither command works, Python is probably not installed correctly or was not added to PATH.

Restart the terminal after installing Python.

---

## Problem 2: Python version is 3.12, 3.13, or another version

The workshop is standardized on Python 3.11.

On Windows, use:

```bash
py -3.11 -m venv .venv
```

On macOS/Linux:

```bash
python3.11 -m venv .venv
```

Then activate the environment before installing packages.

---

## Problem 3: `git` is not recognized

Install Git from:

https://git-scm.com/downloads

Then restart your terminal and check:

```bash
git --version
```

---

## Problem 4: `ollama` is not recognized

Make sure Ollama is installed.

Then:

1. Close the terminal.
2. Open a new terminal.
3. Run:

```bash
ollama --version
```

On systems where Ollama runs as a desktop application, make sure Ollama is actually running.

---

## Problem 5: `llama3.2` is not found

Run:

```bash
ollama list
```

If it is not listed, run:

```bash
ollama pull llama3.2
```

Then test it:

```bash
ollama run llama3.2
```

---

## Problem 6: Ollama works, but CrewAI cannot connect to it

First test Ollama independently:

```bash
ollama run llama3.2
```

If that works, exit it and check that the Ollama service is running.

Then run the workshop again from the activated virtual environment.

The workshop code expects Ollama at:

```text
http://localhost:11434
```

Do not change this unless the workshop instructor tells you to.

---

## Problem 7: `ModuleNotFoundError: No module named 'crewai'`

This usually means either:

1. CrewAI has not been installed, or
2. Your virtual environment is not activated.

Check for `(.venv)` at the beginning of your terminal.

Then run:

```bash
pip install -r requirements.txt
```

Verify:

```bash
pip show crewai
```

---

## Problem 8: CrewAI is installed but Python still cannot import it

Check which Python is being used:

```bash
python --version
```

Then:

```bash
python -m pip show crewai
```

Using `python -m pip` is useful because it ensures pip belongs to the Python interpreter you are running.

If necessary, reinstall inside the active environment:

```bash
python -m pip install -r requirements.txt
```

---

## Problem 9: PowerShell says scripts are disabled

You may see an error when running:

```powershell
.\.venv\Scripts\Activate.ps1
```

If your system allows it, open PowerShell and run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try activation again:

```powershell
.\.venv\Scripts\Activate.ps1
```

Alternatively, use Command Prompt and activate with:

```bat
.venv\Scripts\activate
```

---

## Problem 10: The model takes a long time to respond

This can be normal when running a local LLM.

The first request may take longer because the model needs to load into memory.

Make sure your computer has enough available RAM and that other heavy applications are closed if necessary.

Do not repeatedly restart the program while Ollama is loading.

---

## Problem 11: `python` works outside VS Code but not inside VS Code

VS Code may be using a different Python interpreter.

In VS Code:

1. Open the Command Palette.
2. Select **Python: Select Interpreter**.
3. Select the Python interpreter inside `.venv`.
4. Open a new terminal.
5. Confirm:

```bash
python --version
```

Then try the exercise again.

---

## Problem 12: I accidentally installed packages globally

Don't worry. Activate the virtual environment and install the requirements there:

```bash
python -m pip install -r requirements.txt
```

The workshop will use the packages from the active `.venv` environment.

---

## Problem 13: I get an error while cloning the repository

First check your internet connection.

Then make sure Git works:

```bash
git --version
```

You can also open the repository in a browser to confirm that it is accessible.

---

## Problem 14: I changed directories and the exercise cannot find a file

Run the exercises from the repository root when possible.

For Part 1:

```bash
cd CrewAI-Workshop-Part-1
```

Then run the exercise from there.

For Part 2:

```bash
cd CrewAI-Workshop-Part-2
python main.py
```

---

## Problem 15: Something still isn't working

Do not immediately reinstall everything.

Collect the following information first:

```bash
python --version
git --version
ollama --version
ollama list
python -m pip show crewai
```

Also note the **exact error message** shown in the terminal.

Send the exact error message to the instructor rather than only saying "it doesn't work". The error message usually tells us which part of the setup is failing.

---

# Quick Reset

If your Python environment becomes confusing, you can recreate it.

## Windows

From the repository root:

```bat
rmdir /s /q .venv
py -3.11 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## macOS / Linux

```bash
rm -rf .venv
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Then verify:

```bash
python -c "from crewai import Agent, Task, Crew, LLM; print('CrewAI import successful')"
```

---

# Important

The most common setup problems are caused by one of these:

1. Python version is not 3.11.
2. The virtual environment is not activated.
3. CrewAI was installed outside the virtual environment.
4. Ollama is not running.
5. `llama3.2` has not been downloaded.
6. The student is running the command from the wrong directory.
7. VS Code is using a different Python interpreter.

Check these seven things before reinstalling anything.
