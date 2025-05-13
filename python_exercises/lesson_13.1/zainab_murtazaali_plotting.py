# Import the pandas library
import pandas as pd

# Define the path to your CSV file
csv_path = "data/title.csv"

df = pd.read_csv(csv_path)

print(df.head())

#plot histogram with title and new x-axis label
# length will be out x-axis
import plotly.express as px

fig = px.histogram(df, x ="length",
                   title = "Article lengths in the Gaza Corpus",
                   color = "year",
                   labels = {"length": "Length in tokens",
                             "year": "Year of publication"},
                   color_discrete_map = {2024: "Lightgreen",
                                         2022: "Lightblue"})
                   
fig.add_annotation (x=150, y=260,
                    ax=650, ay=290,
                    axref= "x", ayref= "y",
                    text = "Second peak",
                    showarrow = True,
                    arrowhead = 1,
                    bgcolor = "white")

mean_length = df["length"].mean()

fig.add_vline(x=mean_length, line_dash="dash")

fig.add_annotation(x=mean_length,
                   y=320,
                   xshift=50,
                   showarrow = False,
                   text = "Mean Length")

fig.update_xaxes(ticks = "inside", tickwidth = 2,
                 minor_ticks = "inside", minor_tickwidth = 2)

fig.update_yaxes(ticks = "outside", tickwidth = 2,
                 minor_ticks = "outside", minor_tickwidth= 2)

fig.show()
