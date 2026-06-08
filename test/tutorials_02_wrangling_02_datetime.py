# Block 1
import pandas as pd
import polars as pl
import numpy as np

data = {
    'date_string': ['2023-01-01', '2023-02-15', '2023-03-20'],
    'value': [10, 20, 30]
}
df = pd.DataFrame(data)
df_pl = pl.DataFrame(data)

# Block 2
import pandas as pd
df['date'] = pd.to_datetime(df['date_string'])

# Block 3
import polars as pl
# Convert to datetime and create a new 'date' column for subsequent examples
df_pl = df_pl.with_columns(pl.col('date_string').str.to_datetime("%Y-%m-%d").alias('date'))
# Ensure pandas also has the 'date' column
df['date'] = pd.to_datetime(df['date_string'])

# Block 4
# Use the .dt accessor
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day_name'] = df['date'].dt.day_name()

# Block 5
# Use the .dt namespace
df_pl = df_pl.with_columns([
    pl.col('date').dt.year().alias('year'),
    pl.col('date').dt.month().alias('month'),
    pl.col('date').dt.strftime("%A").alias('day_name')
])

# Block 6
df['next_week'] = df['date'] + pd.Timedelta(days=7)

# Block 7
df_pl = df_pl.with_columns(
    next_week = pl.col('date') + pl.duration(days=7)
)

# Block 8
df['date_utc'] = df['date'].dt.tz_localize('UTC')
df['date_ny'] = df['date_utc'].dt.tz_convert('America/New_York')

# Block 9
df_pl = df_pl.with_columns(
    pl.col('date').dt.replace_time_zone('UTC').dt.convert_time_zone('America/New_York')
)

