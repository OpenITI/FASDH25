import plotly.express as px
import pandas as pd

# Load the data
df = pd.read_csv("data/title.csv")

# Create a histogram of the 'length' column
fig = px.histogram(
    df,
    x="length",
    title="Distribution of Article Lengths",
    labels={"length": "Article Length"}
)

# Show the plot
fig.show()

