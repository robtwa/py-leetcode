# Practice LeetCode problems in Python

## Setup

### 1. Create a Virtual Environment

```bash
python -m venv .venv
```

### 2. Activate the Virtual Environment

**macOS / Linux:**

```bash
source .venv/bin/activate
```

**Windows (CMD):**

```cmd
.venv\Scripts\activate
```

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install the Project in Editable Mode

Install the project in editable mode:

```bash
pip install -e .
```

Editable installation creates a link to your project source directory in the Python environment instead of copying the source files.

This means changes to your source code take effect immediately without reinstalling the project.

In other words, Python can import your project directly from its source directory.

## Run Tests

Run all tests using pytest:

```bash
pytest
```

## Features

- Basic calculator functions
- Unit tests using pytest