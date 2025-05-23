import plotly.express as px
import pandas as pd

# Load CSV file into dataframe
df = pd.read_csv("data/1-gram.csv")

# Print first 10 lines
print(df.head(10))

# Sorting the top 10 frequencies
top_10 = df.sort_values(by='count', ascending=False).head(10)
print(top_10)

# Subset of the dataframe for selected unigrams
filter =df["1-gram"].isin(["peace", "agreement", "truce"])
df2 = df[filter]
print(df2)

#Now plot the line graph
fig = px.line(
    df2,
    x="month",
    y="count",
    color="1-gram",
    title="Frequency of 'peace', 'agreement', and 'truce' Over Time",
    labels={"count": "Frequency", "month": "month"}
)

# Show the plot
fig.show()


