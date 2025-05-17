#import libraries
import pandas as pd
import plotly.express as px

#load the csv file
path = "data/1-gram.csv"
df = pd.read_csv(path)

#print the first 10 rows
print(df.head(10))

#sort by frequency and print the 10 highest frequency rows
df_sorted = df.sort_values(by="count", ascending=False)
print(df_sorted.head(10))

#filter for specific unigrams
filter = df["1-gram"].isin(["peace", "agreement", "truce"])
df2 = df[filter]

#plot the line graph
fig = px.line(df2, x="month", y="count", color="1-gram")
fig.show()
