# Lesson 07: Interactive Visuals with Plotly

## Overview
Plotly is the industry standard for interactive charts in both R and Python. The Python implementation, **Plotly Express (px)**, is particularly elegant for rapid exploration.

## 1. High-Level Plots with Plotly Express
Plotly Express functions are designed to work directly with Pandas DataFrames.

```python
import plotly.express as px

# Load the Gapminder dataset
df = px.data.gapminder()

# Create an interactive bubble chart
fig = px.scatter(df, x="gdpPercap", y="lifeExp", 
                 size="pop", color="continent", 
                 hover_name="country", 
                 log_x=True, size_max=60)

# Show the figure
fig.show()
```

## 2. Faceting and Multi-dimension Plots
Just like `facet_wrap` in ggplot, Plotly can handle subplots easily.

```python
# Facet by continent and color by year
fig = px.scatter(df, x="gdpPercap", y="lifeExp", 
                 facet_col="continent", 
                 color="year",
                 log_x=True)
fig.show()
```

## 3. Customizing the Figure Layout
You can modify the figure object after it has been created using `.update_layout()`.

```python
fig.update_layout(
    title="Customized Plotly Figure",
    xaxis_title="GDP per Capita (USD)",
    yaxis_title="Life Expectancy (Years)",
    template="plotly_dark" # Try 'ggplot2', 'seaborn', or 'none'
)
fig.show()
```

## 4. Exporting Interactive Plots
You can save your interactive plots as standalone HTML files to share with colleagues.
```python
fig.write_html("interactive_plot.html")
```

---

## 🏆 Challenge Exercise: The Animated Exploration
1.  Using the `gapminder` dataset from `px.data`:
2.  Create an interactive scatter plot of `gdpPercap` vs `lifeExp`.
3.  Add an **animation** by setting `animation_frame="year"` and `animation_group="country"`.
4.  Set the `hover_name` to "country" so you can identify each bubble.
5.  **Bonus:** Change the color palette to something custom and add a range slider to the x-axis.

---
[⬅️ Previous](../04_statistics/01_regression_models.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](../06_bayesian/01_pymc_intro.md)
