import pandas as pd
import plotly.express as px

# Load the dataset from the CSV file
df = pd.read_csv("data/title.csv")
print(df.head())

# Plot histogram with title and new x-axis label
fig = px.histogram(df, x="length",
                   title="Article lengths in the Gaza corpus",
                   labels={"length": "Length in tokens"})

# Correct tick formatting
fig.update_xaxes(ticks="inside", tickwidth=2,
                 showgrid=True, minor=dict(ticks="inside", ticklen=4))

# Y-axis doesn't need 'counts', it auto-shows frequency. Just clean formatting:
fig.update_yaxes(title="Frequency")

# Show the plot
fig.show()

