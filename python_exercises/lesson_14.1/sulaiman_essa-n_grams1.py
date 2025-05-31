import pandas as pd
import plotly.express as px

csv_path = "data/1-gram.csv"
df = pd.read_csv(csv_path)

print(df.head(10))


filter = df["1-gram"].isin(["peace", "agreement", "truce"])
df2 = df[ filter ]


print(df2)

#plot the line graph:
fig = px.line(df2, x="month", y="count", color="1-gram")
fig.show()
