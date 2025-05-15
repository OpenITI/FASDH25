# importing libraries
import pandas as pd
import plotly.express as px

# loading the csv file
df = pd.read_csv("data/1-gram.csv")

# printing the first 10 rows now
print(df.head(10))


# filtering the rows for peace, agreement and truce:

filter = df["1-gram"].isin(["peace","agreement","truce"])
df2 = df[ filter ]

print(df2)

# plotting the line:
fig = px.line(df2, x="month", y="count", color="1-gram")

# printing the graph
fig.show()
