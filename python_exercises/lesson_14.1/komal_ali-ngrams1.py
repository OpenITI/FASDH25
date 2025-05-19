# Import necessary libraries 
import plotly.express as px
import pandas as pd

#Load the csv file into pandas DataFrame
df = pd.read_csv("data/1-gram.csv")

#print first 10 rows 
print(df.head(10))

#sorting top 10 frequencies
top_10 = df.sort_values(by = "count", ascending= False).head(10)

#print top 10
print(top_10)

#subset of the DataFrame
filter = df["1-gram"].isin(["peace", "agreement", "truce"])
df2 = df[filter]
print(df2)

fig = px.line(
    df2,
    x="month",
    y="count",
    title= "Monthly Frequency of Selected Unigrams",
    labels = {"month": "Month", "frequency": "Frequency", "1-gram": "Unigram"}
)
fig.show()
