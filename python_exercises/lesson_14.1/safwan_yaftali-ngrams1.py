# Import necessary libraries
import pandas as pd
import plotly.express as px

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("data/1-gram.csv")

# Print the first 10 rows to inspect the data
print(df.head(10))

#sorting the top 10 frequency
top_10= df.sort_values(by='count', ascending=False).head(10)
#printing the top 10 frequency row
print(top_10)

#subset of the dataframe
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


