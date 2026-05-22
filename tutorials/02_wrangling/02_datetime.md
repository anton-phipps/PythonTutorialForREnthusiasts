# Lesson 04: Date and Time Manipulation: The Lubridate Equivalent

## Overview
In R, `lubridate` makes working with dates intuitive. In Python, both **Pandas** and **Polars** provide powerful tools for time-series data.

---

## 1. Parsing Dates
Converting strings to datetime objects.

**R:** `ymd("2023-05-21")`

**Pandas:**
```python
import pandas as pd
df['date'] = pd.to_datetime(df['date_string'])
```

**Polars:**
```python
import polars as pl
df = df.with_columns(pl.col('date_string').str.to_datetime("%Y-%m-%d"))
```

---

## 2. Extracting Components
Accessing the year, month, or day.

**R:** `year(date)`, `month(date)`

**Pandas:**
```python
# Use the .dt accessor
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day_name'] = df['date'].dt.day_name()
```

**Polars:**
```python
# Use the .dt namespace
df = df.with_columns([
    pl.col('date').dt.year().alias('year'),
    pl.col('date').dt.month().alias('month'),
    pl.col('date').dt.strftime("%A").alias('day_name')
])
```

---

## 3. Date Arithmetic
Adding or subtracting time.

**R:** `date + days(7)`

**Pandas:**
```python
df['next_week'] = df['date'] + pd.Timedelta(days=7)
```

**Polars:**
```python
df = df.with_columns(
    next_week = pl.col('date') + pl.duration(days=7)
)
```

---

## 4. Time Zones
Handling time-zone conversions.

**R:** `with_tz(date, tzone = "UTC")`

**Pandas:**
```python
df['date_utc'] = df['date'].dt.tz_localize('UTC')
df['date_ny'] = df['date_utc'].dt.tz_convert('America/New_York')
```

**Polars:**
```python
df = df.with_columns(
    pl.col('date').dt.replace_time_zone('UTC').dt.convert_time_zone('America/New_York')
)
```

---

## 🏆 Challenge Exercise: The Timesheet Analyzer
1.  **Data:** Create a small dataset with `start_time` and `end_time` strings.
2.  **Conversion:** Convert both columns to datetime objects.
3.  **Calculation:** Create a `duration` column showing the difference.
4.  **Extraction:** Create a `weekday` column.
5.  **Bonus:** Implement this workflow in both **Pandas** and **Polars**. Which syntax felt more "R-like"?

---
[⬅️ Previous](01_rosetta_stone.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](../03_visualization/01_static_plots.md)
