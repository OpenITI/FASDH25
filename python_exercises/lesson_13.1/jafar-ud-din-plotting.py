import pandas as pd
import plotly.express as px

#path for the csv
df = pd.read_csv("titles.csv")

#printing the headings to check if df is loaded
print(df.head())

#plotting the histogram
fig = px.histogram(df, x='length', title='Analysis of Article lengths in the Gaza Corpus',
                   labels= {'length': 'length of the tokens'})

#adding ticks
fig.update_xaxes(ticks='inside', tickwidth=2)

#changing lavel of the y axis to frequency
fig.update_yaxes(title_text = "Frequency" )

#showing the graph plotted
fig.ahow()


