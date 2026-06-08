# Lesson 13: Connecting to Databases (MSSQL & Microsoft Fabric)

## Overview
For analysts in the Microsoft ecosystem, connecting to **SQL Server (MSSQL)** and **Microsoft Fabric** is a daily task. In R, you likely used `odbc` or `DBI`. In Python, the standard stack is **pyodbc** (the driver) + **SQLAlchemy** (the engine) + **Pandas** (the interface).

### Local Practice (SQLite)
If you don't have access to an MSSQL server right now, you can practice with **SQLite**, which is built into Python.

```python
import pandas as pd
from sqlalchemy import create_engine

# Create a local SQLite database in memory
engine = create_engine('sqlite://')

# Write some data to it
df_iris = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
df_iris.to_sql('iris', engine, index=False)

# Read it back
df_read = pd.read_sql("SELECT * FROM iris", engine)
print(df_read)
```

---

## 1. Connecting to Microsoft SQL Server (MSSQL)
To connect to a traditional SQL Server, you need an ODBC driver installed on your machine (e.g., "ODBC Driver 17 for SQL Server").

### The R vs. Python Connection
**R (DBI/odbc):**
```r
con <- dbConnect(odbc(), 
                 Driver = "ODBC Driver 17 for SQL Server",
                 Server = "my_server", 
                 Database = "my_db", 
                 Trusted_Connection = "yes")
```

### Python (Pandas)
```python
import pandas as pd
from sqlalchemy import create_engine
import urllib

# 1. Create the connection string
params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=my_server;"
    "DATABASE=my_db;"
    "Trusted_Connection=yes;"
)

# 2. Initialize the engine
# Note: This requires the 'pyodbc' library and a system ODBC driver
try:
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
    # df = pd.read_sql("SELECT TOP 10 * FROM my_table", engine)
except ImportError:
    print("pyodbc not installed")
except Exception as e:
    print(f"Could not connect: {e}")
```

### Python (Polars)
```python
import polars as pl

# Polars can use the same SQLAlchemy engine or a connection string (URI)
try:
    uri = f"mssql+pyodbc:///?odbc_connect={params}"
    # df = pl.read_database(query="SELECT TOP 10 * FROM my_table", connection=uri)
except NameError:
    print("params not defined")
```

---

## 2. Connecting to Microsoft Fabric
Microsoft Fabric's SQL endpoints and Lakehouses can be accessed similarly to SQL Server, but they often require **Service Principal** or **Azure AD** authentication.

### Using the SQL Connection String
Fabric provides a SQL connection string for every Lakehouse and Warehouse.

```python
# Connection string from Fabric portal
server = "xxx.datawarehouse.pbidedicated.windows.net"
database = "MyLakehouse"

params = urllib.parse.quote_plus(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    "Authentication=ActiveDirectoryInteractive;" # Triggers a login popup
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
```

---

## 3. Microsoft Fabric: Direct Lakehouse Access (Delta Tables)
If you are working inside a **Fabric Notebook**, you don't even need a connection string! You can read **Delta Tables** directly from the Lakehouse using **Pandas** or **Polars**.

### Python (Pandas)
```python
# Inside a Fabric Notebook
import pandas as pd

# Path to a Delta table in your Lakehouse
path = "Files/data/my_delta_table"
df = pd.read_parquet(path) # Fabric stores Delta as Parquet
```

### Python (Polars)
```python
# Inside a Fabric Notebook
import polars as pl

# Polars can read the parquet files directly or use read_delta
path = "Files/data/my_delta_table"
df = pl.read_parquet(path)
```

---

## 4. Key Differences: R vs. Python
| Feature | R (odbc/DBI) | Python (SQLAlchemy) |
| --- | --- | --- |
| **Driver** | `odbc()` | `pyodbc` |
| **Connection** | `dbConnect()` | `create_engine()` |
| **Querying** | `dbGetQuery(con, sql)` | `pd.read_sql(sql, engine)` |
| **Writing** | `dbWriteTable(con, name, df)` | `df.to_sql(name, engine)` |
| **Chunking** | `dbFetch(res, n=1000)` | `pd.read_sql(sql, engine, chunksize=1000)` |

---

## 🏆 Challenge Exercise: The SQL Roundtrip
1.  **Requirement:** Ensure you have access to a SQL Server instance (or use a local SQLite DB for practice).
2.  **Task:** Create an engine for your database.
3.  **Step 1:** Use `df.to_sql()` to upload the `tips` dataset from `seaborn` to a table named `stg_tips`.
4.  **Step 2:** Write a SQL query that calculates the `average tip` grouped by `day`.
5.  **Step 3:** Use `pd.read_sql()` to bring those results back into a Python DataFrame.
6.  **Comparison:** How does the `urllib.parse.quote_plus` method for connection strings compare to the named arguments in R's `dbConnect`? Which do you find more robust?

---
[⬅️ Previous](01_advanced_features.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](03_apis.md)
