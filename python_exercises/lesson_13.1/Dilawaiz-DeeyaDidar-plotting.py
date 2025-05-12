import pandas as pd 
import plotly.express as px

df = pd.read_csv("data/title.csv")

print(df.head())

fig = px.histogram(df, x="length", title="Distribution of Title Lengths", labels={"length": "Title Length (words)"})

fig.update_yaxes(title="Frequency")

fig.show()
