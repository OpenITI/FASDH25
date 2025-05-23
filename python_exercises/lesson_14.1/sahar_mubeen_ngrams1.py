# Import the required libraries
import pandas as pd
import plotly.express as px

# Load the CSV file into a pandas DataFrame
csv_path = "data/1-gram.csv"
df = pd.read_csv(csv_path)

# Print the first 10 rows of the data to understand its structure
print(df.head(10))

# Get the 10 words with the highest counts (most frequent)

top_10 = df.sort_values(by="count", ascending=False)

#printing the top 10 frequency row

print(top_10)

# subset of the dataframe

df2= df[df ["1-gram"].isin( ["peace" , "agreement" , "truce"])]
print(df2)

fig = px.line(
    df2,
    x="month",
    y="count",
    title="Monthly Frequency of Selected Unigrams",
    labels={"month": "Month", "frequency": "Frequency", "1-gram": "Unigram"}
)

fig.show()
