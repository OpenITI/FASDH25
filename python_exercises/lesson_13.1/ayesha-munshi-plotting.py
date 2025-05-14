import pandas as pd
import plotly.express as px
csv_path = "data/title.csv"
df = pd.read_csv(csv_path)

#plot histogram with title and and x-axis label
fig = px.histogram(df, x= "length", 
                   title = "Articles in Gaza corpus",
                   labels = {"length": "Length in tokens"})
#add tick markers to the x axis
fig.update_xaxes(ticks = "inside", tickwidth = 2, 
                 minor_ticks = "inside", minor_tickwidth= 2)
#change the label of the y axis to frequency
fig.update_yaxes(ticks = "outside", tickwidth = 2,
                 minor_ticks = "outside", minor_tickwidth= 2)

fig.show()
