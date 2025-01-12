## Run Locally

Clone the project

```bash
  git clone https://github.com/ShubhamKaudewar/In_Memory_Search_Engine
```

Go to the project directory

```bash
  cd In_Memory_Search_Engine
```

Install [uv](https://docs.astral.sh/uv)

```bash
  #If python is already installed
  pip install uv 
  
  #For MacOS and Linux
  curl -LsSf https://astral.sh/uv/install.sh | sh 
  
  #For Window using powershell
  powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Check python version

```bash
  python --version
```

Create virtualenv and Install python 3.13 using uv if not installed

```bash
  uv venv --python 3.13
```

Create virtualenv

```bash
  uv venv
```

Activate virtualenv

```bash
  .\.venv\Scripts\activate #Windows CMD
  source venv/Scripts/activate #Bash
```

Install dependencies from pyproject.toml file

```bash
  uv pip install -r pyproject.toml
```

Start Engine

```bash
  python main.py
```

## Approach, design, decisions, and challenges faced.

- **Approach:** Using Graph concept i.e.HashMap Table to store keyword to associated document_id for search operation. Using MD5 hash to hexdecimal to check for duplicate entries

- **Design:** Inbuilt memory for storing document, hash to documentId and index keywords. Using strategy and abstract base class design pattern for Input and search query

- **Decisions:** Using threading to keep thread alive until action provided is CLOSE

- **Challenges Faced:** Unable to think for Basic Ranking algorithm

## Sample log

```bash
Input action: insert
provide documents: e.g. 'I am Indian,I am developer'
provide documents: I am Indian,I am developer
Input action: search
provide keywords: e.g. 'I,am'
provide keywords: developer
provide operation: [AND, OR, NOT]
provide operation: not
[1736699846217]
Input action: close
Closing database!
```

