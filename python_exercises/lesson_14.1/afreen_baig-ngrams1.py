import pandas as pd
import plotly.express as px

#load csv file
df = pd.read_csv("data/1-gram.csv")

#print the 1st 10 rows
print(df.head(10))

#crating a subse for 1 grams
filter = df["1-gram"].isin(["peace", "agreement", "truce"])
df2 = df[ filter ]

print(df2)

#creating a line graph
fig = px.line(df2, x="month", y="count")
fig.show()



