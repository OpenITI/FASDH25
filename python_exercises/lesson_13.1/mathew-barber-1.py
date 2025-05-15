import pandas as pd
import plotly.express as px

df = pd.read_csv("data/title.csv")

# Plot the histogram with colors based on the year

fig = px.histogram(df, x="length",
                   title = "Article lengths in the Gaza corpus",
                   color = "year",
                   labels = {"length": "Length in tokens",
                             "year": "Year of Publication"})

# Add arrow pointing to a peak in the data

fig.add_annotation(x=150, y=260,
                   ax=650, ay=290,
                   axref="x", ayref="y",
                   text = "Second peak",
                   showarrow = True,
                   arrowhead = 1,
                   bgcolor="white")

# Add a vline for the mean article length

mean_length = df["length"].mean()

fig.add_vline(x=mean_length, line_dash="dash")

# Give a text annotation to the vline

fig.add_annotation(x=mean_length,
                   y=320,
                   xshift=50,
                   showarrow = False,
                   text = "Mean length")

                   
fig.show()
