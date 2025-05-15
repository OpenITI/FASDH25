import pandas as pd
import plotly.express as px

# Load the CSV file in Dataframe
df = pd.read_csv("data/1-gram.csv")

# Print the first 10 rows of the Dataframe
print(df.head(10))

# Sorting the top 10 frequencies
top_10 = df.sort_values (by='count', ascending=False).head(10)
print(top_10)

# Filter the Dataframe to only include relevent n-grams
filter = df["1-gram"].isin(["peace", "agreement", "truce"])
print(filter)
df2 = df[ filter ]
print(df2)

# Plot the line graph
fig = px.line(df2, x="month", y="count", color="1-gram")
fig.show()
