# Block 1
import plotly.express as px
df = px.data.iris()

# Interactive Scatter Plot
fig = px.scatter(df, x="sepal_width", y="sepal_length", 
                 color="species", size='petal_length',
                 hover_data=['petal_width'],
                 title="Iris Dataset: Sepal Width vs Length")
fig.show()

# Block 2
from plotnine import ggplot, aes, geom_point, geom_smooth, facet_wrap, theme_minimal, labs
from plotnine.data import mpg

(ggplot(mpg, aes(x='displ', y='hwy', color='class'))
 + geom_point(size=3, alpha=0.7)
 + geom_smooth(method='lm', se=False)
 + facet_wrap('~drv')
 + theme_minimal()
 + labs(title="Engine Displacement vs Highway MPG",
        x="Displacement (L)", y="Highway MPG"))

# Block 3
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# Block 4
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') # For headless environments

