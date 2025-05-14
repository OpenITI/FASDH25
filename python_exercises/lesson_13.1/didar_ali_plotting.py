import pandas as pd
import plotly.express as px

path = 'data/title.csv'
df = pd.read_csv(path)

# Creating the histogram
fig = px.histogram(
    df,
    x="length",
    title="Article lengths in the Gaza Corpus",
    labels={"length": "Length in tokens"}
)

# Add tick marks to x-axis
fig.update_xaxes(ticks="inside", tickwidth=2)

# Update the y-axis label to "Frequency"
fig.update_yaxes(title_text="Frequency")

# Show the figure
fig.show()
