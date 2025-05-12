import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('data/title.csv')

# Create a histogram using the 'length' column
fig = px.histogram(df, x='length')

# Customize the title and x-axis label
fig.update_layout(
    title='Distribution of Article Lengths',
    xaxis_title='Article Length (in paragraphs)',
)

# Add tick marks to the x-axis
fig.update_xaxes(tickmode='linear')

# Change y-axis label to 'Frequency'
fig.update_yaxes(title_text='Frequency')

# Show the figure
fig.show()
