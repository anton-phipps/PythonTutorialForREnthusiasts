# Date and Time Manipulation: The Lubridate Equivalent

## Overview
In R, `lubridate` makes working with dates intuitive. In Python, we use the `.dt` accessor in Pandas, which provides nearly identical functionality.

## 1. Parsing Dates
Converting strings to datetime objects.
*   **R:** `ymd("2023-05-21")`, `dmy("21-05-2023")`
*   **Pandas:** `pd.to_datetime("2023-05-21")` or `pd.to_datetime(df['date_string'])`

```python
import pandas as pd

# Pandas is very smart at guessing formats
dates = pd.to_datetime(["2023-01-01", "01/02/2023", "March 3rd, 2023"])
print(dates)
```

## 2. The `.dt` Accessor
Once a column is in datetime format, you can extract any component using `.dt`.

```python
df['date'] = pd.to_datetime(df['raw_date'])

df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day_name'] = df['date'].dt.day_name()
df['is_weekend'] = df['date'].dt.weekday >= 5
```

## 3. Date Arithmetic
Adding or subtracting time.
*   **R:** `date + days(7)`, `date %m+% months(1)`
*   **Pandas:** `date + pd.Timedelta(days=7)` or `date + pd.DateOffset(months=1)`

```python
# Moving forward by a week
next_week = df['date'] + pd.Timedelta(weeks=1)

# Calculating duration
df['duration'] = df['end_date'] - df['start_date']
print(df['duration'].dt.days) # Get duration in days as an integer
```

## 4. Time Zones
*   **Naive:** `pd.Timestamp("2023-01-01")` (No timezone)
*   **Aware:** `pd.Timestamp("2023-01-01", tz="UTC")`
*   **Convert:** `df['date'].dt.tz_convert("US/Eastern")`

---

## 🏆 Challenge Exercise: The Timesheet Analyzer
1.  Create a DataFrame with two columns: `start_time` and `end_time` (fill with strings like "2023-05-21 09:00:00").
2.  Convert both columns to datetime objects.
3.  Calculate a new column `hours_worked`.
4.  Extract the `weekday` name for each entry.
5.  **Bonus:** Filter for only the entries where the work started before 10:00 AM.

---
[⬅️ Previous](01_rosetta_stone.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](../03_visualization/01_static_plots.md)
