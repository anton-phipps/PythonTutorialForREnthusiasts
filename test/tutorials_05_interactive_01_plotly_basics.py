# Block 1
import plotly.express as px

# Load the Gapminder dataset
df = px.data.gapminder()

# Create an interactive bubble chart
fig = px.scatter(df, x="gdpPercap", y="lifeExp", 
                 size="pop", color="continent", 
                 hover_name="country", 
                 log_x=True, size_max=60)

# Show the figure
fig.show()

# Block 2
# Facet by continent and color by year
fig = px.scatter(df, x="gdpPercap", y="lifeExp", 
                 facet_col="continent", 
                 color="year",
                 log_x=True)
fig.show()

# Block 3
fig.update_layout(
    title="Customized Plotly Figure",
    xaxis_title="GDP per Capita (USD)",
    yaxis_title="Life Expectancy (Years)",
    template="plotly_dark" # Try 'ggplot2', 'seaborn', or 'none'
)
fig.show()

# Block 4
fig.write_html("interactive_plot.html")

