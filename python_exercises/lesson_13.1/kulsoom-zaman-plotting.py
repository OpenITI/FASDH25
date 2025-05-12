#import libraries
import pandas as pd
import plotly.express as px

# loading data path
data_path = "data/title.csv"

#read it in dataframe
df= pd.read_csv(data_path)

#printing the heads of the dataframe
print(df.head())

# Create histogram of article lengths
fig = px.histogram(df, x="length", title="Article length distribution", color = "year", labels={"length": "Length in tokens", "year": "Year of Publication"})

fig.update_xaxes(ticks="inside", tickwidth=2)
fig.update_yaxes(title="Frequency") 

# Show the plot
fig.show()
