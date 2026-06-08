# Block 1
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

# Block 2
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

# Block 3
import polars as pl

# Polars can use the same SQLAlchemy engine or a connection string (URI)
try:
    uri = f"mssql+pyodbc:///?odbc_connect={params}"
    # df = pl.read_database(query="SELECT TOP 10 * FROM my_table", connection=uri)
except NameError:
    print("params not defined")

# Block 4
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

# Block 5
# Inside a Fabric Notebook
import pandas as pd

# Path to a Delta table in your Lakehouse
path = "Files/data/my_delta_table"
df = pd.read_parquet(path) # Fabric stores Delta as Parquet

# Block 6
# Inside a Fabric Notebook
import polars as pl

# Polars can read the parquet files directly or use read_delta
path = "Files/data/my_delta_table"
df = pl.read_parquet(path)

