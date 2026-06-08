# Block 1
import pandas as pd
import polars as pl
import numpy as np

# Create a sample DataFrame for demonstration
data = {
    'size': ['S', 'M', 'L', 'S', 'M'],
    'cyl': [4, 6, 8, 4, 4],
    'hp': [110, 175, 245, 62, 95],
    'wt': [2.62, 3.21, 3.44, 2.14, 3.15],
    'mpg': [21, 21, 14, 22, 19],
    'x': [1, 2, 3, 4, 5],
    'id': [1, 2, 3, 4, 5]
}
df = pd.DataFrame(data)
df_pl = pl.DataFrame(data)

# For joining examples
df1 = df.copy()
df2 = pd.DataFrame({'id': [1, 2, 3], 'val': ['A', 'B', 'C']})
df1_pl = pl.DataFrame(df1)
df2_pl = pl.DataFrame(df2)

# For reshaping examples
df_wide = pd.DataFrame({
    'id': [1, 2],
    'Jan': [10, 20],
    'Feb': [15, 25]
})
df_wide_pl = pl.DataFrame(df_wide)

# Block 2
# Convert to categorical (Factor)
df['size'] = pd.Categorical(df['size'], categories=['S', 'M', 'L'], ordered=True)

# Accessing categories
print(df['size'].cat.categories)

# Block 3
# Polars uses 'Enum' or 'Categorical'
df_pl = df_pl.with_columns(pl.col("size").cast(pl.Categorical))

# Block 4
(df
 .query('cyl == 4')
 .assign(hp_wt = lambda x: x.hp / x.wt)
 .loc[:, ['mpg', 'hp_wt']])

# Block 5
(df_pl
 .filter(pl.col('cyl') == 4)
 .with_columns((pl.col('hp') / pl.col('wt')).alias('hp_wt'))
 .select(['mpg', 'hp_wt']))

# Block 6
df.query('mpg > 20')
# or
df[df['mpg'] > 20]

# Block 7
df_pl.filter(pl.col('mpg') > 20)

# Block 8
df[['mpg', 'hp']]

# Block 9
df_pl.select(['mpg', 'hp'])

# Block 10
df.assign(new_col = df['x'] * 2)

# Block 11
df_pl.with_columns((pl.col('x') * 2).alias('new_col'))

# Block 12
(df
 .groupby('cyl')
 .agg(mean_mpg=('mpg', 'mean')))

# Block 13
(df_pl
 .group_by('cyl')
 .agg(mean_mpg=pl.col('mpg').mean()))

# Block 14
df1.merge(df2, on='id', how='left')

# Block 15
df1_pl.join(df2_pl, on='id', how='left')

# Block 16
import numpy as np
conditions = [df['x'] < 10, df['x'] < 20]
choices = ['low', 'med']
df['cat'] = np.select(conditions, choices, default='high')

# Block 17
df_pl.with_columns(
    cat = pl.when(pl.col('x') < 10).then(pl.lit('low'))
            .when(pl.col('x') < 20).then(pl.lit('med'))
            .otherwise(pl.lit('high'))
)

# Block 18
df_wide.melt(id_vars=['id'], value_vars=['Jan', 'Feb'], var_name='month', value_name='temp')

# Block 19
df_wide_pl.unpivot(index='id', on=['Jan', 'Feb'], variable_name='month', value_name='temp')

# Block 20
# Assuming df_melted exists
df_melted = df_wide.melt(id_vars=['id'], value_vars=['Jan', 'Feb'], var_name='month', value_name='temp')
df_melted.pivot(index='id', columns='month', values='temp')

# Block 21
# Assuming df_unpivoted exists
df_unpivoted = df_wide_pl.unpivot(index='id', on=['Jan', 'Feb'], variable_name='month', value_name='temp')
df_unpivoted.pivot(on='month', values='temp', index='id')

# Block 22
df.iloc[0:5] # Rows 0 to 4

# Block 23
df[0:5] # Polars uses standard Python slicing directly

