# Lesson 02: Jupyter Notebooks & VS Code

## Overview
For R users, RStudio is the de facto IDE. In the Python world, you have two primary choices for interactive analysis: **JupyterLab** (the web-based evolution of notebooks) and **VS Code** (a powerful general-purpose IDE).

## 1. JupyterLab: The Web Standard
JupyterLab is the modern interface for Jupyter Notebooks. It allows you to have multiple notebooks, text files, and terminals open in one tab.

*   **Cells:** Notebooks are made of cells.
    *   **Code Cells:** Where you write and execute Python code. Press `Shift + Enter` to run.
    *   **Markdown Cells:** Where you write documentation.
*   **Kernels:** The Python process running your code. Use **Kernel -> Restart** if things get messy.

## 2. VS Code: The "RStudio" Experience
Many R users find that **VS Code** with the **Python** and **Jupyter** extensions feels the most like RStudio.

### Why use VS Code?
1.  **Variable Explorer:** Just like RStudio's "Environment" pane, VS Code has a built-in variable explorer for notebooks.
2.  **Integrated Terminal:** Easily run shell commands or script files.
3.  **Extensions:** Add support for Git, SQL, Docker, and even R!
4.  **Copilot:** Excellent AI-assisted coding integration.

### Setup for R Users:
1.  Install VS Code.
2.  Go to the Extensions view (`Ctrl+Shift+X`) and install the **Python** and **Jupyter** extensions from Microsoft.
3.  Open a `.ipynb` file or create a new one.

---

## 3. Magic Commands (Magics)

Magics are special commands that are not valid Python but are understood by the Jupyter environment.
*   `%matplotlib inline`: Ensures plots show up inside the notebook (usually default now).
*   `%timeit`: Measures the execution time of a single line.
*   `%%time`: Measures the execution time of an entire cell.
*   `%pwd`: Print working directory.
*   `%ls`: List files in the current directory.

```ipython
# Example of %timeit
%timeit [x**2 for x in range(1000)]
```

## 3. Keyboard Shortcuts (The "Analyst's Speedrun")
Jupyter has two modes: **Command Mode** (Blue border) and **Edit Mode** (Green border).
*   `Esc`: Enter Command Mode.
*   `Enter`: Enter Edit Mode.
*   `A`: Insert cell **A**bove.
*   `B`: Insert cell **B**elow.
*   `D, D`: **D**elete cell.
*   `M`: Change cell to **M**arkdown.
*   `Y`: Change cell to **C**ode.

---

## 🏆 Challenge Exercise: My First Notebook
1.  Open a Jupyter Notebook (or use a service like Google Colab).
2.  Create a Markdown cell with a title and a brief description of a research question.
3.  Create a Code cell that defines a variable `data = [1, 2, 3, 4, 5]`.
4.  Create another Code cell that uses `%timeit` to see how long it takes to sum that data.
5.  **Bonus:** Try to insert a cell above your current one using only keyboard shortcuts.

---
[⬅️ Previous](01_introduction.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](../02_wrangling/01_rosetta_stone.md)
