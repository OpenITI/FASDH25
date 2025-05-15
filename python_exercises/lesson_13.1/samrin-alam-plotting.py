import pandas as pd
import plotly.express as px

# read it in the dataframe
df = pd.read_csv("data/title.csv")

# printing the head of dataframe
print(df.head())

#Plot histogram from the given data
fig = px.histogram(df, x = "length",
                   title = "Article lengths in the Gaza corpus",
                   labels= {"length": "Length in tokens"})

#Adding ticks marks to the x-axis
fig.update_xaxes(ticks="outside", tickwidth=2,
                 minor_ticks="outside", minor_tickwidth=2)

fig.update_yaxes(title="frequency")
fig.show()


