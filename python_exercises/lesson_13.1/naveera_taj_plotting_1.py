# import the necessary libraries

import pandas as pd
import plotly.express as px
# reading path of the title.csv
csv_path = r"C:/Users/HP/Downloads/FASDH25/python_exercises/lesson_13.1/data/title.csv"
df = pd.read_csv(csv_path)
print(df.head)

#plot histogram with title and new xaxis label
fig = px.histogram(df, x="length",
                   title ="Articles length in the Gaza corpus",
                   labels = {"length": "Length in tokens"})
fig.show()
fig.write_image 

# add tick markers inside of the graph on the xaxis
fig.updata_xaxes(ticks = "inside", tickwidth = 2,
           minor_ticks= "inside", minor_tickwidth=2)
#adding tick markers to outside of the graph on the yaxis
fig.updata_yaxes(ticks = "outside", tickwidth = 2,
           minor_ticks = "outside", minor_tickwidth=2)
fig.show

# Annotating the figure
# plotting the histogram with colors based on the year
fig = px. histogram(df, x="length",
                    title = "Article length in the Gaza corpus",
                    color = "year",
                    labels = {"length": "Length in tokens",
                              "year": "Year of the Publication"})

# Add arrow pointing to a peak in the data

fig.add_annotation(x=150, y=260,
                   ax=650, ay=290,
                   axref="x", ayrefz="y",
                   text = "Second peak",
                   showarrow = True,
                   arrowhead = 1,
                   bgcolor="white")
# Adding a vline for the mean article length
mean_length = df["length"].mean()
fig.add_vline(x=mean-length, line_dash="dasg")

#Give a text annotation to the vline
fig.add_annotation(x=mean_length,
                   y=320)

