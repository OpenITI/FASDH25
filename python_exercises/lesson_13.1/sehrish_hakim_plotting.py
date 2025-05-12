# import libraries
import pandas as pd
import plotly.express as px

#Load title .csv as a data frame
df= pd.read_csv("data/title.csv")

#print the head of the dataframe
print(df.head())


#costomizing the title 
fig = px.histogram(df, x="length",
                   title ="Article with the Longest length",
                   color = "year"
                    labels={"length": "Length in tokens"
                             })
# Updating the x axis
fig.update_xaxes(ticks="outside", tickwidth=1,
                 minor_ticks="outside", minor_tickwidth=2)

#updating the y axis to frequency 
fig.update_yaxes(title="frequency")

fig.show()


