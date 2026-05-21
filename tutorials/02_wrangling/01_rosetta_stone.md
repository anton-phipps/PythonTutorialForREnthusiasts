# The Data Wrangling Rosetta Stone: Dplyr to Pandas/Polars

## Overview
This lesson maps the "Verbs" of the Tidyverse (`dplyr` and `tidyr`) to their Python equivalents in **Pandas** and **Polars**.

## 1. Core Verbs (dplyr)

### Filter (`filter`)
Selecting rows based on conditions.
*   **R:** `df %>% filter(mpg > 20, cyl == 4)`
*   **Pandas:** `df.query('mpg > 20 and cyl == 4')` or `df[(df['mpg'] > 20) & (df['cyl'] == 4)]`
*   **Polars:** `df.filter((pl.col('mpg') > 20) & (pl.col('cyl') == 4))`

### Select (`select`)
Choosing specific columns.
*   **R:** `df %>% select(mpg, horsepower, contains("weight"))`
*   **Pandas:** `df[['mpg', 'horsepower']]` or `df.filter(like='weight')`
*   **Polars:** `df.select([pl.col('mpg'), pl.col('horsepower'), pl.col('^.*weight.*$')])`

### Mutate (`mutate`)
Creating or transforming columns.
*   **R:** `df %>% mutate(hp_per_wt = horsepower / weight)`
*   **Pandas:** `df.assign(hp_per_wt = df['horsepower'] / df['weight'])`
*   **Polars:** `df.with_columns((pl.col('horsepower') / pl.col('weight')).alias('hp_per_wt'))`

### Group By & Summarize (`group_by` + `summarize`)
*   **R:** `df %>% group_by(cyl) %>% summarize(avg_mpg = mean(mpg))`
*   **Pandas:** `df.groupby('cyl').agg(avg_mpg=('mpg', 'mean'))`
*   **Polars:** `df.group_by('cyl').agg(avg_mpg=pl.col('mpg').mean())`

## 2. Reshaping (tidyr)

### Pivot Longer (`pivot_longer`)
Converting wide data to long format.
*   **R:** `df %>% pivot_longer(cols = c(Jan, Feb), names_to = "month", values_to = "temp")`
*   **Pandas:** `df.melt(id_vars=['id'], value_vars=['Jan', 'Feb'], var_name='month', value_name='temp')`

### Pivot Wider (`pivot_wider`)
Converting long data to wide format.
*   **R:** `df %>% pivot_wider(names_from = month, values_from = temp)`
*   **Pandas:** `df.pivot(index='id', columns='month', values='temp')`

## 3. String Manipulation (stringr)
*   **R:** `str_detect(column, "pattern")`
*   **Pandas:** `df['column'].str.contains("pattern")`
*   **Polars:** `pl.col('column').str.contains("pattern")`

---

## 🏆 Challenge Exercise: The Car Cleanup
Using the `mtcars` dataset (you can load it from `seaborn` or `plotnine.data`):
1.  Filter for cars with more than 100 `horsepower`.
2.  Create a new column called `efficiency` which is `mpg / weight`.
3.  Group the data by the number of cylinders (`cyl`).
4.  Calculate the `mean` and `std` of the `efficiency` column for each group.
5.  **Bonus:** Perform the same operations using **Polars** instead of Pandas.

---
[⬅️ Previous](../01_foundations/02_jupyter.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](02_datetime.md)
