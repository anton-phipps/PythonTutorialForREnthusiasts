# Block 1
import pandas as pd
import polars as pl
import numpy as np
from sklearn.model_selection import train_test_split

# Sample data
data = {
    'hp': [110, 175, 245, 62, 95, 123, 180, 205, 60, 113],
    'wt': [2.62, 3.21, 3.44, 2.14, 3.15, 2.77, 3.57, 3.85, 2.32, 3.01],
    'qsec': [16.46, 17.02, 15.84, 18.61, 19.44, 17.02, 15.5, 15.41, 18.9, 17.4],
    'mpg': [21, 21, 14, 22, 19, 18, 14, 13, 24, 18]
}
df = pd.DataFrame(data)
df_pl = pl.DataFrame(data)

X = df[['hp', 'wt', 'qsec']]
y = df['mpg']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# For Polars examples
X_train_pl = pl.from_pandas(X_train)
y_train_pl = pl.from_pandas(y_train.to_frame())

# Block 2
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

# Block 3
from sklearn.linear_model import LinearRegression

X = df[['hp']] # Features must be a 2D array/DataFrame
y = df['mpg']

model = LinearRegression().fit(X, y)
print(f"Intercept: {model.intercept_}, Coef: {model.coef_[0]}")

# Block 4
import polars as pl
from sklearn.linear_model import LinearRegression

X = df_pl.select('hp')
y = df_pl.select('mpg')

# Convert to numpy for sklearn
model = LinearRegression().fit(X.to_numpy(), y.to_numpy())
print(f"Intercept: {model.intercept_}, Coef: {model.coef_[0]}")

# Block 5
X = df[['hp', 'wt', 'qsec']]
model = LinearRegression().fit(X, y)

# Print all coefficients
for name, coef in zip(X.columns, model.coef_.flatten()):
    print(f"{name}: {coef.item():.4f}")

# Block 6
X = df_pl.select(['hp', 'wt', 'qsec'])
model = LinearRegression().fit(X.to_numpy(), y.to_numpy())

# Print all coefficients
for name, coef in zip(X.columns, model.coef_.flatten()):
    print(f"{name}: {coef.item():.4f}")

# Block 7
from sklearn.ensemble import RandomForestRegressor

# n_estimators is the number of trees (default is 100)
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Feature Importance: Which variables mattered most?
importances = rf.feature_importances_

# Block 8
from sklearn.ensemble import RandomForestRegressor

# sklearn works best with numpy arrays from Polars
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train_pl.to_numpy(), y_train_pl.to_numpy())

# Feature Importance
importances = rf.feature_importances_

# Block 9
from xgboost import XGBRegressor

xgb = XGBRegressor(n_estimators=100, learning_rate=0.1)
xgb.fit(X_train, y_train)

# Block 10
from xgboost import XGBRegressor

# XGBoost also accepts numpy arrays
xgb = XGBRegressor(n_estimators=100, learning_rate=0.1)
xgb.fit(X_train_pl.to_numpy(), y_train_pl.to_numpy())

