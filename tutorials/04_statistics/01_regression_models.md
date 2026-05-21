# Lesson 04: Statistical Modeling

## Overview
Python splits statistics into two worlds: **Inference** (Statsmodels) and **Prediction** (Scikit-learn).

## 1. Statsmodels: Linear Regression (The `lm` equivalent)
`statsmodels` provides a formula interface that allows you to specify models just like you do in R.

```python
import statsmodels.formula.api as smf
import pandas as pd
import seaborn as sns

# Load data
df = sns.load_dataset("mpg")

# Define the formula: mpg explained by displacement and weight
# In R: model <- lm(mpg ~ displacement + weight, data = df)
model = smf.ols(formula="mpg ~ displacement + weight", data=df).fit()

# View the full statistical report
print(model.summary())

# Access specific results
print(f"R-squared: {model.rsquared:.3f}")
print(f"Coefficients:\n{model.params}")
```

## 2. GLM: Logistic Regression (The `glm` equivalent)
```python
# In R: glm(outcome ~ x1 + x2, family = binomial, data = df)
logit_model = smf.logit(formula="survived ~ age + fare", data=sns.load_dataset("titanic")).fit()
print(logit_model.summary())
```

## 3. Scikit-learn: The ML approach to Regression
In scikit-learn, you care about the model's ability to predict on new data, not the p-values of the coefficients.

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# 1. Prepare data (sklearn needs numeric arrays, no formulas)
X = df[['displacement', 'weight']].dropna()
y = df.loc[X.index, 'mpg']

# 2. Split into training and testing sets (Validation!)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Fit the model
reg = LinearRegression()
reg.fit(X_train, y_train)

# 4. Make predictions and evaluate
y_pred = reg.predict(X_test)
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.2f}")
print(f"R2 Score: {r2_score(y_test, y_pred):.2f}")
```

---

## 🏆 Challenge Exercise: The Model Showdown
1.  Using the `diamonds` dataset (from `seaborn` or `plotnine.data`):
2.  Fit a linear model using **Statsmodels** where `price` is explained by `carat`, `depth`, and `table`.
3.  Identify which variables are statistically significant at the 0.05 level.
4.  Fit the same model using **Scikit-learn** and report the Root Mean Squared Error (RMSE) on a 20% test set.
5.  **Bonus:** Add an interaction term to the Statsmodels formula (e.g., `carat * depth`) and see how it affects the R-squared.

---
[⬅️ Previous](../03_visualization/01_static_plots.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](../05_interactive/01_plotly_basics.md)
