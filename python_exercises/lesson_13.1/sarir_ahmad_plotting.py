#importing libraries

import plotly.express as px
import pandas as pd

#reading the path of title.csv:
csv_path = "data/title.csv"
df = pd.read_csv (csv_path)
print(df.head)

#plotting histogram:
fig = px.histogram(df, x="length",
                   title = "Article lengths in the Corpus",
                   color = "year",
                   labels = {"length" : "Length in tokens",
                             "year" : "year of publication"})
fig.show()

#add tick markers to inside of the graph on the x axis:
date_xaxes(ticks = "inside" , tickwidth =2,
           minor_ticks ="inside", minor_tickwidth = 2,)

#add arrow pointing:
fig.add_annotations

#add annotation:
fig.add_annotation(x=mean_length,
                   y=320,
                   xshift=50,
                   showarrow= False,
                   text = "Mean length")
