# Lesson 15: Building Local User Interfaces

## Overview
In R, you have **Shiny**. In Python, for analysts and researchers, you have two main paths: **Streamlit** for speed, and **Shiny for Python** for familiar reactivity.

## 1. Streamlit: The Speed Demon
Streamlit allows you to turn a script into a web app in minutes. Its mental model is simple: the script reruns from top to bottom every time something changes.

```python
import streamlit as st
import pandas as pd
import numpy as np

st.title("My Research Dashboard")
n_points = st.slider("Select number of points", 10, 1000, 100)

data = pd.DataFrame({'x': np.random.randn(n_points), 'y': np.random.randn(n_points)})
st.scatter_chart(data)
```

## 2. Shiny for Python: The Familiar Choice
If you have complex apps with many dependencies (where you only want *part* of the UI to update), **Shiny for Python** is the answer. It uses the same "Reactive" logic you used in R.

**Comparison for R Users:**
*   **Streamlit:** Feels like a linear script. Very easy, but can be slow if your data is massive (because it reruns everything).
*   **Shiny for Python:** Feels exactly like R Shiny (UI + Server). Harder to learn, but much more powerful for complex apps.

| Feature | Streamlit | Shiny for Python |
| --- | --- | --- |
| **Learning Curve** | Extremely Low | Moderate (if you know R Shiny) |
| **Layout Control** | Simple/Opinionated | Full/Flexible |
| **Reactivity** | Full-script rerun | Reactive Graph (fine-grained) |
| **Best For** | Quick Prototypes | Production Dashboards |

## 3. Running your App
*   **Streamlit:** `streamlit run app.py`
*   **Shiny:** `shiny run --reload app.py`

## 4. Traditional Desktop UIs
If you need a standalone `.exe` or a more traditional windowed application, look into:
*   **Tkinter:** Built-in to Python. Good for very simple windows.
*   **CustomTkinter:** A modern skin for Tkinter.
*   **PyQt / PySide:** The heavyweights. Used for professional software (like VLC or Photoshop).

---

## 🏆 Challenge Exercise: The Data Filter App
1.  Create a file named `filter_app.py`.
2.  Use Streamlit to create an app that:
    *   Asks the user to upload a CSV file (`st.file_uploader`).
    *   Displays the first 5 rows of the data.
    *   Allows the user to select a column from the data (`st.selectbox`).
    *   Displays a histogram of that column using `st.bar_chart` or `st.plotly_chart`.
3.  **Bonus:** Add a button that, when clicked, calculates and displays the summary statistics of the entire file.

---
[⬅️ Previous](03_apis.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](../09_version_control/01_git_basics.md)
