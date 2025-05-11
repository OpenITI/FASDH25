import pandas as pd
import plotly.express as px

#reading the CSV files

df = pd.read_csv('data/title.csv')

#print the head of dataframe
print(df.head())

#plot histogram with title and new xaxis label
fig = px.histogram(df, x ="length",
                   title = "Analysis of Article Lengths in the Gaza Corpus",
                   labels= {"length": "Length in tokens"})

#add ticks markers to xaxis
fig.update_xaxes(ticks="inside", tickwidth=2)

fig.update_yaxes(title_text="Frequency")

fig.show()
