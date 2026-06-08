# Block 1
import statsmodels.formula.api as smf
import pandas as pd
import seaborn as sns

# Load data
df = sns.load_dataset("mpg")

# Define the formula: mpg explained by displacement and weight
model = smf.ols(formula="mpg ~ displacement + weight", data=df).fit()

# Block 2
import polars as pl
import seaborn as sns

# Load data and convert to Polars
df_pl = pl.from_pandas(sns.load_dataset("mpg"))

# Statsmodels requires Pandas, so we convert back for the fit
model = smf.ols(formula="mpg ~ displacement + weight", data=df_pl.to_pandas()).fit()

# Block 3
# View the full statistical report
print(model.summary())

# Access specific results
print(f"R-squared: {model.rsquared:.3f}")
print(f"Coefficients:\n{model.params}")

# Block 4
# In R: glm(outcome ~ x1 + x2, family = binomial, data = df)
logit_model = smf.logit(formula="survived ~ age + fare", data=sns.load_dataset("titanic")).fit()
print(logit_model.summary())

# Block 5
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# 1. Prepare data (sklearn needs numeric arrays, no formulas)
X = df[['displacement', 'weight']].dropna()
y = df.loc[X.index, 'mpg']

# 2. Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Block 6
import polars as pl
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 1. Prepare data
# We select columns and drop nulls
df_clean = df_pl.select(['displacement', 'weight', 'mpg']).drop_nulls()
X = df_clean.select(['displacement', 'weight'])
y = df_clean.select('mpg')

# 2. Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X.to_numpy(), y.to_numpy(), test_size=0.2, random_state=42)

# Block 7
# 3. Fit the model
reg = LinearRegression()
reg.fit(X_train, y_train)

# 4. Make predictions and evaluate
y_pred = reg.predict(X_test)
print(f"Mean Squared Error: {mean_squared_error(y_test, y_pred):.2f}")
print(f"R2 Score: {r2_score(y_test, y_pred):.2f}")

