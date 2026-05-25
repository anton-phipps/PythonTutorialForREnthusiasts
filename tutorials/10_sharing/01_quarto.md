# Lesson 20: Reporting with Quarto

## Overview
For R users, **R Markdown** was the gold standard for reproducible reporting. **Quarto** is the next-generation version of R Markdown that is "language agnostic." It is the best way for a Python analyst to create high-quality PDFs, HTML reports, and Word documents using the same `.qmd` format you already know.

## 1. Why Quarto for Python?
*   **Familiarity:** If you know R Markdown, you already know 90% of Quarto.
*   **Engine Choice:** Quarto can use **Jupyter** or **Knitr** to execute Python code chunks.
*   **One Source, Many Outputs:** Create a blog, a book, a presentation, or a technical report from the same markdown file.

## 2. Anatomy of a Quarto Document
A `.qmd` file looks just like an `.Rmd` file, but with a few modern improvements.

```yaml
---
title: "Quarterly Analysis Report"
author: "Research Analyst"
format: 
  html:
    code-fold: true
    toc: true
execute:
  echo: true
---

## Data Summary
We are using the `penguins` dataset to demonstrate Quarto's capabilities.

```{python}
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("penguins")
df.describe()
```

## Visualization
Quarto handles matplotlib and seaborn plots automatically.

```{python}
#| label: fig-penguins
#| fig-cap: "Body Mass vs. Flipper Length by Species"

sns.scatterplot(data=df, x="flipper_length_mm", y="body_mass_g", hue="species")
plt.show()
```
```

## 3. Rendering your Report
In the terminal, you can render your report to any format:
```bash
# Render to HTML
quarto render report.qmd --to html

# Render to PDF (requires TeX)
quarto render report.qmd --to pdf
```

## 4. R Markdown to Quarto: Key Differences
| Feature | R Markdown | Quarto |
| --- | --- | --- |
| **File Extension** | `.Rmd` | `.qmd` |
| **Code Chunks** | `{r}` | `{python}` or `{r}` |
| **Chunk Options** | Inside `{python, echo=F}` | Using the hashpipe `#| echo: false` |
| **CLI** | `rmarkdown::render()` | `quarto render` |

---

## 🏆 Challenge Exercise: The Reproducible Report
1.  Install the Quarto CLI (if you haven't already).
2.  Create a file named `analysis.qmd`.
3.  Add a YAML header with a title and table of contents.
4.  Write a Python chunk that imports `pandas` and reads a public CSV (e.g., from GitHub).
5.  Use a "hashpipe" comment (`#|`) to hide the code but show the output for one of your charts.
6.  Render the file to HTML and open it in your browser.

---
[⬅️ Previous](../09_version_control/04_advanced_git.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](02_powerbi_fabric.md)
