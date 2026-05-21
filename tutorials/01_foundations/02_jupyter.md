# Jupyter Notebooks: The RStudio Alternative

## Overview
For R users, RStudio is the de facto IDE. In the Python world, **Jupyter Notebooks** (or JupyterLab) are the standard for interactive data analysis, similar to RMarkdown or Quarto documents.

## 1. The Anatomy of a Notebook
*   **Cells:** Notebooks are made of cells.
    *   **Code Cells:** Where you write and execute Python code. Press `Shift + Enter` to run.
    *   **Markdown Cells:** Where you write documentation, just like in RMarkdown. Use `#`, `##`, `**bold**`, etc.
*   **Kernels:** The "brain" of the notebook. It's the Python process running your code. 
    *   If you get stuck in an infinite loop, click **Kernel -> Interrupt**.
    *   To clear all variables and start fresh, click **Kernel -> Restart**.

## 2. Magic Commands (Magics)
Magics are special commands that are not valid Python but are understood by the Jupyter environment.
*   `%matplotlib inline`: Ensures plots show up inside the notebook (usually default now).
*   `%timeit`: Measures the execution time of a single line.
*   `%%time`: Measures the execution time of an entire cell.
*   `%pwd`: Print working directory.
*   `%ls`: List files in the current directory.

```python
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
