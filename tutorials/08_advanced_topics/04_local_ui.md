# Building Local User Interfaces

## Overview
In R, you have **Shiny**. In Python, for analysts and researchers, the absolute best tool for building a quick UI is **Streamlit**. It allows you to turn a script into a web app in minutes without knowing HTML/CSS.

## 1. The Streamlit Mental Model
Streamlit apps are just Python scripts that run from top to bottom. Every time a user interacts with a widget (like a slider), the script reruns.

```python
import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("My Research Dashboard")

# 1. User Input
name = st.text_input("Enter your name", "Analyst")
st.write(f"Hello, {name}!")

# 2. Interactive Widget
n_points = st.slider("Select number of points", 10, 1000, 100)

# 3. Dynamic Calculation
data = pd.DataFrame({
    'x': np.random.randn(n_points),
    'y': np.random.randn(n_points)
})

# 4. Displaying Data/Plots
st.subheader("Random Data Scatter")
st.scatter_chart(data)

if st.checkbox("Show Raw Data"):
    st.write(data)
```

## 2. Running your App
Unlike a normal Python script, you run Streamlit from the command line:
```bash
streamlit run my_app.py
```

## 3. Traditional Desktop UIs
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
[⬅️ Previous](03_apis.md) | [🏠 Table of Contents](../../README.md)
