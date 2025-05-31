import pandas as pd
import plotly.express as px

# load the csv file:
csv_path = "data/1-gram.csv"
df = pd.read_csv(csv_path)

# print first 10 rows
print (df.head(10))


# filter the rows for peace, agreement and truce:

filter = df["1-gram"].isin(["peace", "agreement", "truce"])
df2 = df[ filter ]

print(df2)

# plot the line graph:
fig = px.line(df2, x="month", y="count", color="1-gram")
fig.show()
