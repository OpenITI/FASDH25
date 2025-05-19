import pandas as pd
import plotly.express as px
df = pd.read_csv("data/1-gram.csv")

# print first 10
print(df.head(10))

# filter the rows for peace, agrement and truce
filter = df["1-gram"].isin(["peace", "agreement", "truce"])
df2 = df[filter]

print(df2)

#plot the line graph 
fig = px.line(df2, x ="month", y="count", color ="1-gram")
fig.show()
