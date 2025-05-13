import pandas as pd
import plotly.express as px

#file path
csv_path = r"data\title.csv"

#defining df
df = pd.read_csv(csv_path)

#printing the first few lines to check if df is loaded.
print(df.head())


#plotting histogram
fig = px.histogram(df, x ="length",
                   title = "Article in the Gaza Corpus",
                   color = "year",
                    labels = {"length": "Length in tokens"})
#adding ticks
fig.update_xaxes(ticks = "inside", tickwidth = 2)

#Changing the label of y axis to frequency
fig.update_yaxes(title_text = "Frequency")

#show the figures
fig.show()

                 
