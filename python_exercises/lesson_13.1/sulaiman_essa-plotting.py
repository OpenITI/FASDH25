import pandas as pd

#read the csv and print the titles column
df = pd.read_csv("data/title.csv")
print(df["title"])

# Import the relevant libraries
import plotly.express as px

fig = px.histogram(df, x="length",
                   title = "Article lengths in the Gaza corpus",
                            labels = {"length": "Length in tokens"})
fig.update_xaxes(ticks = "inside", tickwidth = 2)

                   
