# Lesson 03: The Data Wrangling Rosetta Stone: Dplyr to Pandas/Polars

## Overview
This lesson is the core of your transition. We will map the "Verbs" of the Tidyverse (`dplyr` and `tidyr`) to their Python equivalents in **Pandas** and **Polars**.

---

## 1. Categorical Data (Factors)
In R, `factors` are a first-class citizen. In Python, we have `Categorical` data.

### Pandas:
```python
# Convert to categorical (Factor)
df['size'] = pd.Categorical(df['size'], categories=['S', 'M', 'L'], ordered=True)

# Accessing categories
print(df['size'].cat.categories)
```

### Polars:
```python
# Polars uses 'Enum' or 'Categorical'
df = df.with_columns(pl.col("size").cast(pl.Categorical))
```

---

## 2. The Method Chain vs. The Pipe
In R, you use the pipe `%>%` (or `|>`). In Python, we use **Method Chaining**.

### R (Dplyr)
```r
df %>%
  filter(cyl == 4) %>%
  mutate(hp_wt = hp / wt) %>%
  select(mpg, hp_wt)
```

### Python (Pandas)
```python
(df
 .query('cyl == 4')
 .assign(hp_wt = lambda x: x.hp / x.wt)
 .loc[:, ['mpg', 'hp_wt']])
```

### Python (Polars)
```python
(df
 .filter(pl.col('cyl') == 4)
 .with_columns((pl.col('hp') / pl.col('wt')).alias('hp_wt'))
 .select(['mpg', 'hp_wt']))
```

---

## 2. Core Verbs Comparison

### Filter (`filter`)
**R:** `df %>% filter(mpg > 20)`

**Pandas:**
```python
df.query('mpg > 20')
# or
df[df['mpg'] > 20]
```

**Polars:**
```python
df.filter(pl.col('mpg') > 20)
```

### Select (`select`)
**R:** `df %>% select(mpg, hp)`

**Pandas:**
```python
df[['mpg', 'hp']]
```

**Polars:**
```python
df.select(['mpg', 'hp'])
```

### Mutate (`mutate`)
**R:** `df %>% mutate(new_col = x * 2)`

**Pandas:**
```python
df.assign(new_col = df['x'] * 2)
```

**Polars:**
```python
df.with_columns((pl.col('x') * 2).alias('new_col'))
```

### Summarize & Group By (`group_by` + `summarize`)
**R:** `df %>% group_by(cyl) %>% summarize(mean_mpg = mean(mpg))`

**Pandas:**
```python
(df
 .groupby('cyl')
 .agg(mean_mpg=('mpg', 'mean')))
```

**Polars:**
```python
(df
 .group_by('cyl')
 .agg(mean_mpg=pl.col('mpg').mean()))
```

### Arrange (`arrange`)
**R:** `df %>% arrange(desc(mpg))`

**Pandas:** `df.sort_values('mpg', ascending=False)`

**Polars:** `df.sort('mpg', descending=True)`

### Rename (`rename`)
**R:** `df %>% rename(new_name = old_name)`

**Pandas:** `df.rename(columns={'old_name': 'new_name'})`

**Polars:** `df.rename({'old_name': 'new_name'})`

### Distinct (`distinct`)
**R:** `df %>% distinct(cyl)`

**Pandas:** `df[['cyl']].drop_duplicates()`

**Polars:** `df.select('cyl').unique()`

---

## 3. Joining Datasets
Joins are slightly different in Python. Pandas uses `merge`, Polars uses `join`.

### Left Join (`left_join`)
**R:** `left_join(df1, df2, by = "id")`

**Pandas:**
```python
df1.merge(df2, on='id', how='left')
```

**Polars:**
```python
df1.join(df2, on='id', how='left')
```

---

## 4. Conditional Logic (`case_when` / `ifelse`)
One of the most used features in R is `if_else` or `case_when`.

### R:
```r
df %>%
  mutate(cat = case_when(
    x < 10 ~ "low",
    x < 20 ~ "med",
    TRUE   ~ "high"
  ))
```

### Pandas (`np.select` or `.loc`):
```python
import numpy as np
conditions = [df['x'] < 10, df['x'] < 20]
choices = ['low', 'med']
df['cat'] = np.select(conditions, choices, default='high')
```

### Polars (`pl.when`):
```python
df.with_columns(
    cat = pl.when(pl.col('x') < 10).then(pl.lit('low'))
            .when(pl.col('x') < 20).then(pl.lit('med'))
            .otherwise(pl.lit('high'))
)
```

---

## 5. Reshaping (Tidyr)

### Pivot Longer (`pivot_longer`)
**R:** `df %>% pivot_longer(cols = c(Jan, Feb), names_to = "month", values_to = "temp")`

**Pandas:**
```python
df.melt(id_vars=['id'], value_vars=['Jan', 'Feb'], var_name='month', value_name='temp')
```

**Polars:**
```python
df.unpivot(index='id', on=['Jan', 'Feb'], variable_name='month', value_name='temp')
```

### Pivot Wider (`pivot_wider`)
**R:** `df %>% pivot_wider(names_from = month, values_from = temp)`

**Pandas:**
```python
df.pivot(index='id', columns='month', values='temp')
```

**Polars:**
```python
df.pivot(on='month', values='temp', index='id')
```

---

## 4. Indexing and Slicing
R is 1-based, Python is 0-based.

**R:** `df[1:5, ]`

**Pandas:**
```python
df.iloc[0:5] # Rows 0 to 4
```

**Polars:**
```python
df[0:5] # Polars uses standard Python slicing directly
```

---

## 🏆 Challenge Exercise: The Car Cleanup
Using the `mtcars` dataset:
1.  **Filter:** Only keep cars with `hp` > 100.
2.  **Mutate:** Create a column `efficiency` = `mpg / wt`.
3.  **Group:** Group by `cyl`.
4.  **Summarize:** Calculate the `mean` efficiency for each group.
5.  **Bonus:** Implement this entire chain once in **Pandas** and once in **Polars**.

---
[⬅️ Previous](../01_foundations/02_jupyter.md) | [🏠 Table of Contents](../../README.md) | [Next ➡️](02_datetime.md)
