# Lesson 03: Data Visualization

## Overview
In R, `ggplot2` is built on the "Grammar of Graphics." Python offers several libraries that either mirror this approach or provide high-level abstractions for common statistical charts.

## 1. Plotnine: The literal `ggplot2` port
If you want to keep using the same syntax you know and love, **Plotnine** is your best friend.

```python
from plotnine import ggplot, aes, geom_point, geom_smooth, facet_wrap, theme_minimal
from plotnine.data import mpg

(ggplot(mpg, aes(x='displ', y='hwy', color='class'))
 + geom_point(size=3, alpha=0.7)
 + geom_smooth(method='lm', se=False)
 + facet_wrap('~drv')
 + theme_minimal()
 + labs(title="Engine Displacement vs Highway MPG",
        x="Displacement (L)", y="Highway MPG"))
```
*   **Pro-tip:** Note the parentheses `(...)` around the whole plot. This is a common Python pattern to allow multi-line expressions without using backslashes.

## 2. Seaborn: Beautiful Statistical Plots
**Seaborn** is designed for high-level data exploration. It handles complex tasks like plotting averages with confidence intervals automatically.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Set the style
sns.set_theme(style="whitegrid")

# Create a categorical boxplot with 'hue' (like color in ggplot)
tips = sns.load_dataset("tips")
sns.boxplot(data=tips, x="day", y="total_bill", hue="smoker", palette="Set2")

plt.title("Bill Distribution by Day and Smoking Status")
plt.show()
```

## 3. Matplotlib: The Powerhouse Foundation
Everything in Python visualization eventually leads back to **Matplotlib**. It is the most flexible but also the most complex.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot([1, 2, 3], [10, 20, 15], marker='o', linestyle='--', color='red')
ax.set_title("Base Matplotlib Customization")
ax.set_xlabel("Time")
ax.set_ylabel("Metric")
plt.show()
```

---

## 🏆 Challenge Exercise: The Multi-Plot Comparison
1.  Using the `mpg` dataset from `plotnine.data` or `seaborn`:
2.  Create a **Plotnine** scatter plot of `cty` (city mpg) vs `hwy` (highway mpg) colored by `cyl`.
3.  Create a **Seaborn** violin plot showing the distribution of `hwy` for each `class` of car.
4.  **Bonus:** Combine two Matplotlib subplots into one figure—one showing a histogram of `mpg` and the other showing a boxplot.

---
[⬅️ Previous](../02_wrangling/02_datetime.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](../04_statistics/01_regression_models.md)
