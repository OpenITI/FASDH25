import pandas as pd
import plotly.express as px

# Reading the CSV file
df = pd.read_csv('data/title.csv')

#Print the head of the dataframe
print(df.head())
# Creating a histogram from data using the correct column 'length'
fig = px.histogram(df, x="length",
                   title= "Analysis of Article Lengths in the Gaza Corpus",
                   color = "year",
                   labels= {"length": "Length in tokens",
                            "year": "Year of Publication"},
                   color_discrete_map = {2024:"LightGreen"})

# Adding tick marks to the x-axis
fig.update_xaxes(ticks="inside", tickwidth=2)

# Updating the y-axis label to 'Frequency'
fig.update_yaxes(title_text="Frequency")

# Show the plot
fig.show()
