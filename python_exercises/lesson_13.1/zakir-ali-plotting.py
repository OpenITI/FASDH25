import pandas as pd
import plotly.express as px

csv_path = "data/title.csv"

df = pd.read_csv(csv_path)

print(df.head())


# plot histogram with title and new xaxis label
fig = px.histogram(df, x="length", title="Article length distribution", color = "year", labels={"length": "Length in tokens", "year": "Year of Publication"})

# add tick markers to inside of the graph of x axis
fig.update_xaxes(ticks="inside", tickwidth=2)
fig.update_yaxes(title="Frequency") 

# Show the plot
fig.show()



