import pandas as pd
import plotly.express as px

# Step 1 & 2: Load the data and create a histogram
df = pd.read_csv("data/title.csv")

#data path
data_path = "data/title.csv"

#read in the dataframe
df= pd.read_csv(data_path)

#print the head of the data frame
print(df.head())

# Plot histogram with title and new x-axis label
fig = px.histogram(df, x="length",
                   title="Article lengths in the Gaza corpus",
                   labels={"length": "Length in tokens"})


# Add tick markers to outside of the graph on the x-axis
fig.update_xaxes(ticks="outside", tickwidth=2,
                 minor_ticks="outside", minor_tickwidth=2)

fig.update_yaxes(title="frequency")
fig.show()
