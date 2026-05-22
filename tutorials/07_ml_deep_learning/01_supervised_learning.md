# Lesson 09: Supervised Learning & Pipelines

## 1. Pipelines: The `tidymodels` Equivalent
In R, `tidymodels` uses `recipes` and `workflows`. In Python, we use **Pipelines** to bundle preprocessing and modeling together. This prevents "data leakage" and makes your code cleaner.

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

# Define the pipeline: Scaling -> Modeling
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestRegressor(n_estimators=100))
])

# Fit the entire pipeline
pipeline.fit(X_train, y_train)

# Predict using the pipeline (scaling happens automatically!)
y_pred = pipeline.predict(X_test)
```

---

## 2. Simple & Multiple Linear Regression
While we covered `statsmodels` for inference, `scikit-learn` is used when your primary goal is **prediction accuracy**.

### Simple Regression (One Predictor)
**R:** `lm(mpg ~ hp, data = df)`

### Python (Pandas)
```python
from sklearn.linear_model import LinearRegression

X = df[['hp']] # Features must be a 2D array/DataFrame
y = df['mpg']

model = LinearRegression().fit(X, y)
print(f"Intercept: {model.intercept_}, Coef: {model.coef_[0]}")
```

### Python (Polars)
```python
import polars as pl
from sklearn.linear_model import LinearRegression

X = df_pl.select('hp')
y = df_pl.select('mpg')

# Convert to numpy for sklearn
model = LinearRegression().fit(X.to_numpy(), y.to_numpy())
print(f"Intercept: {model.intercept_}, Coef: {model.coef_[0]}")
```

### Multiple Regression (Many Predictors)
**R:** `lm(mpg ~ hp + wt + qsec, data = df)`

### Python (Pandas)
```python
X = df[['hp', 'wt', 'qsec']]
model = LinearRegression().fit(X, y)

# Print all coefficients
for name, coef in zip(X.columns, model.coef_):
    print(f"{name}: {coef:.4f}")
```

### Python (Polars)
```python
X = df_pl.select(['hp', 'wt', 'qsec'])
model = LinearRegression().fit(X.to_numpy(), y.to_numpy())

# Print all coefficients
for name, coef in zip(X.columns, model.coef_):
    print(f"{name}: {coef:.4f}")
```

---

## 2. Tree-Based Methods
Tree-based models are the "workhorses" of tabular data. They don't assume linearity and can capture complex interactions automatically.

### Decision Trees (The Base)
A single tree that splits data into branches.
*   **R:** `rpart::rpart(y ~ ., data = train)`
*   **Python:** `from sklearn.tree import DecisionTreeRegressor`

### Random Forest (The Ensemble)
A "forest" of many decision trees that vote on the outcome. This reduces overfitting.
*   **R:** `randomForest::randomForest(y ~ ., data = train)`

### Python (Pandas)
```python
from sklearn.ensemble import RandomForestRegressor

# n_estimators is the number of trees (default is 100)
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Feature Importance: Which variables mattered most?
importances = rf.feature_importances_
```

### Python (Polars)
```python
from sklearn.ensemble import RandomForestRegressor

# sklearn works best with numpy arrays from Polars
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train.to_numpy(), y_train.to_numpy())

# Feature Importance
importances = rf.feature_importances_
```

### Gradient Boosting (XGBoost / LightGBM)
Trees are built sequentially, each one trying to correct the errors of the previous one. This is currently the state-of-the-art for most tabular datasets.
*   **R:** `xgboost::xgboost(data = X, label = y)`

### Python (Pandas)
```python
from xgboost import XGBRegressor

xgb = XGBRegressor(n_estimators=100, learning_rate=0.1)
xgb.fit(X_train, y_train)
```

### Python (Polars)
```python
from xgboost import XGBRegressor

# XGBoost also accepts numpy arrays
xgb = XGBRegressor(n_estimators=100, learning_rate=0.1)
xgb.fit(X_train.to_numpy(), y_train.to_numpy())
```

---

## 3. The "Fit/Predict" Workflow vs. R
One major difference R users notice is that Scikit-learn requires you to **explicitly split your data** into features (X) and target (y), and then into Training and Testing sets.

| Task | R (Base/Tidy) | Python (Scikit-learn) |
| --- | --- | --- |
| Formula | `y ~ x1 + x2` | No formula. Use `X = df[['x1', 'x2']]` |
| Split | `rsample::initial_split(df)` | `train_test_split(X, y, test_size=0.2)` |
| Train | `fit(model, formula, data)` | `model.fit(X_train, y_train)` |
| Predict | `predict(model, new_data)` | `model.predict(X_test)` |

---

## 🏆 Challenge Exercise: The House Price Predictor
1.  **Data:** Use the `diamonds` dataset from `seaborn`.
2.  **Task:** Predict `price` using `carat`, `depth`, `table`, `x`, `y`, and `z`.
3.  **Step 1:** Perform a Simple Linear Regression using only `carat`.
4.  **Step 2:** Perform a Multiple Linear Regression using all numeric features.
5.  **Step 3:** Train a **RandomForestRegressor** and compare the R-squared score on a 20% test set with the linear models.
6.  **Step 4:** Which model performed best? Why do you think that is?

---
[⬅️ Previous](../06_bayesian/01_pymc_intro.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](02_unsupervised_learning.md)
