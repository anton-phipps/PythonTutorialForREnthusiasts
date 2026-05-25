# Lesson 00: Environment & Package Management

## Overview
For R users, the transition to Python often feels like moving from a well-manicured garden (CRAN/RStudio) to the wild west. In R, `install.packages()` is usually all you need. In Python, you have multiple ways to manage libraries and "environments."

## 1. Why Environments Matter
In R, you typically have one global library (or one per R version). In Python, projects often require different versions of the same library. To avoid "DLL Hell," we use **Virtual Environments**.

### The R Way vs. The Python Way
| Feature | R | Python |
| --- | --- | --- |
| **Package Repository** | CRAN | PyPI (Python Package Index) |
| **Installation** | `install.packages("dplyr")` | `pip install pandas` |
| **Loading** | `library(dplyr)` | `import pandas as pd` |
| **Isolation** | `renv` (Optional) | `venv`, `conda`, `uv` (Essential) |

## 2. Modern Environment Tools
There are many tools, but for a research analyst, we recommend one of these three:

### Option A: `uv` (Recommended for Speed)
`uv` is an extremely fast Python package manager written in Rust. It feels the most like the modern R experience.
*   **Create Environment:** `uv venv`
*   **Install Package:** `uv pip install pandas plotnine`
*   **Sync:** `uv pip compile requirements.in -o requirements.txt`

### Option B: `Conda` / `Miniconda` (Standard for Science)
Very popular in the data science world because it handles non-Python dependencies (like C++ libraries) easily.
*   **Create Environment:** `conda create -n my_project python=3.11`
*   **Activate:** `conda activate my_project`
*   **Install:** `conda install pandas`

### Option C: `venv` + `pip` (Built-in)
The "standard" way that comes with Python.
*   **Create:** `python -m venv .venv`
*   **Activate (Windows):** `.venv\Scripts\activate`
*   **Activate (Mac/Linux):** `source .venv/bin/activate`

## 3. Package Management Best Practices
1.  **Never install to the global Python:** Always use an environment.
2.  **`requirements.txt`:** This is your `DESCRIPTION` file equivalent. It lists what your project needs.
    *   Generate: `pip freeze > requirements.txt`
    *   Install from: `pip install -r requirements.txt`
3.  **Import Conventions:**
    ```python
    import pandas as pd       # Standard alias
    import numpy as np        # Standard alias
    import polars as pl       # Standard alias
    import matplotlib.pyplot as plt
    ```

## 4. Quarto: The RMarkdown Successor
If you love RMarkdown, you don't have to give it up! **Quarto** works perfectly with Python. You can use the same `.qmd` format, but use the `python` engine instead of `r`.

(Note: In a `.qmd` file, code chunks use `{python}` instead of `{r}`)

```yaml
---
title: "Python Analysis"
format: html
---
```

```python
import pandas as pd
df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
df.head()
```

---

## 🏆 Challenge Exercise: Fresh Start
1.  **Task:** Create a new virtual environment using `venv` or `uv`.
2.  **Installation:** Install `pandas`, `polars`, and `plotnine`.
3.  **Verification:** Start a Python interpreter and try to `import pandas as pd`. If it works, you're ready!

---
[🏠 Table of Contents](../../README.md) | [Next ➡️](01_introduction.md)
