import pandas as pd
import plotly.express as px

# Load the CSV file
df = pd.read_csv("data/1-gram.csv")

# Preview data
print(df.head(10))

# Top 10 most frequent unigrams
top_10 = df.sort_values(by='count', ascending=False).head(10)
print("Top 10 most frequent unigrams:")
print(top_10)

# Filter for specific unigrams
df2 = df[df["1-gram"].isin(["peace", "agreement", "truce"])].copy()
print("Filtered data for selected unigrams:")
print(df2)

# Combine year, month, day into a proper datetime
df2['date'] = pd.to_datetime(df2[['year', 'month', 'day']])

# Create 'month_year' column for monthly grouping
df2['month_year'] = df2['date'].dt.to_period('M').dt.to_timestamp()

# Group by month and unigram
monthly = df2.groupby(['month_year', '1-gram'])['count'].sum().reset_index()

# Create interactive line chart
fig = px.line(
    monthly,
    x="month_year",
    y="count",
    color="1-gram",
    title="Monthly Frequency of Selected Unigrams",
    labels={"month_year": "Month", "count": "Frequency", "1-gram": "Unigram"}
)

# Save plot as HTML
fig.write_html("rukhshan_rehmat-ngrams1.html")



