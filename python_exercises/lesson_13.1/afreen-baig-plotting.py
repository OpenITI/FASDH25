import pandas as pd
import plotly.express as px

df = pd.read_csv("data/title.csv")

print(df.head())

fig = px.histogram(df, x="length",
                   title = "Distribution of Article Lengths")
#adding the tick marks to the xaxis
fig.update_xaxes(ticks = "inside", tickwidth =2)
#Add Axis Labels
fig.update_layout(
    xaxes_title="Article Length (words or units)",
    yaxes_title="Frequency"
)

# Show the plot
fig.show()


