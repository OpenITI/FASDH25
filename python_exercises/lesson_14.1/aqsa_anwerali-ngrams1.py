import pandas as pd
import plotly.express as px

# load the csv
df = pd.read_csv('data/1-gram.csv')

# printing the first 10 rows
print(df.head(10))

# Create a subset DataFrame with specific 1-grams
filter = df['1-gram'].isin(['peace', 'agreement', 'truce'])

df2 = df [filter]

# Display the new DataFrame
print(df2)

# plot the line graph:

fig = px.line(
    df2,
    x="month",
    y="count",
    title="Monthly Frequency of Selected Unigrams",
    labels={"month": "Month", "frequency": "Frequency", "1-gram": "Unigram"}
)

fig.show()
