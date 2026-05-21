# Connecting to Databases

## Overview
In R, you use `DBI` and `dbplyr`. In Python, the standard is **SQLAlchemy** (the core engine) and **Pandas** (the interface).

## 1. Setting up the Connection
Python can connect to almost any database (SQLAlchemy, PostgreSQL, MySQL, SQLite, etc.).

```python
import pandas as pd
from sqlalchemy import create_engine

# SQLite (Local file)
# In R: con <- dbConnect(RSQLite::SQLite(), "my_db.sqlite")
engine = create_engine('sqlite:///my_db.sqlite')

# PostgreSQL
# engine = create_engine('postgresql://user:password@localhost:5432/my_db')
```

## 2. Reading Data
You can read directly from a SQL query into a Pandas DataFrame.

```python
query = "SELECT * FROM observations WHERE year > 2020"

# In R: df <- dbGetQuery(con, query)
df = pd.read_sql(query, engine)

print(df.head())
```

## 3. Writing Data
You can also push DataFrames back to the database.

```python
# In R: dbWriteTable(con, "new_results", df)
df.to_sql('new_results', engine, if_exists='replace', index=False)
```

## 4. The "dbplyr" Equivalent: SQLAlchemy ORM
If you want to avoid writing raw SQL strings, SQLAlchemy provides an "Object-Relational Mapper" (ORM) or a "Core" expression language that feels more like R's `dbplyr`.

---

## 🏆 Challenge Exercise: The Database Roundtrip
1.  Create a local SQLite database named `challenge.db`.
2.  Create a Pandas DataFrame with some dummy research data (e.g., `id`, `value`).
3.  Write this DataFrame to a table called `experiment_data`.
4.  Write a SQL query to select only the rows where `value > 10` and read them into a new DataFrame.
5.  **Bonus:** Try to use the `con` parameter in `pd.read_sql` instead of just the engine.

---
[⬅️ Previous](01_advanced_features.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](03_apis.md)
