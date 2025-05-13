import pandas as pd 
import plotly.express as px

# Loading the data
df = pd.read_csv("data/title.csv")
print(df.head())

# Creating the histogram
fig = px.histogram(df, x="length", title="Distribution of Title Lengths", labels={"length": "Title Length (words)"})

# Customizing tick marks on the x-axis
fig.update_xaxes(tickmode="linear", tick0=0, dtick=60)

# Renaming y-axis to "Frequency"
fig.update_yaxes(title="Frequency")

# Showing figure the figure
fig.show()
