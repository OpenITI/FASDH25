
import plotly.express as px
import pandas as pd

# Load the CSV file in Dataframe
df = pd.read_csv("data/1-gram.csv")

# Print the first 10 rows of the Dataframe
print(df.head(10))

# Filter the Dataframe to only include relevent n-grams
filter = df["1-gram"].isin(["peace", "agreement", "truce"])
print(filter)
df2 = df[ filter ]


fig = px.line(df2, x="month", y="count")
fig.show()
