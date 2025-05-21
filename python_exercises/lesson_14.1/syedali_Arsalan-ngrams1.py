# Load essential libraries
import pandas as pd
import plotly.express as px

# Define the path to the CSV file
data_path = "data/1-gram.csv"

# Load the CSV data into a DataFrame
df = pd.read_csv(data_path)

# Display the first 10 entries for a quick preview
print(df.head(10))

# Sort data based on the 'count' column in descending order and view the top 10 results
df_sorted = df.sort_values(by='count', ascending=False)
print(df_sorted.head(10))

# Isolate rows where the 1-gram is one of the selected keywords
df2 = df[df['1-gram'].isin(["peace", "agreement", "truce"])].copy()
print(df2)

# Create a complete date column by combining year, month, and day
df2 = df2.assign(date=pd.to_datetime(df2[['year', 'month', 'day']]))

# Generate a monthly identifier from the date
df2 = df2.assign(month_year=df2['date'].dt.to_period('M'))

# Group the data by both month and 1-gram to sum the counts for each term per month
monthly_counts = df2.groupby(['month_year', '1-gram'])['count'].sum().reset_index()

# Convert the monthly period back to a timestamp for accurate plotting
monthly_counts['month_year'] = monthly_counts['month_year'].dt.to_timestamp()

# Build a line chart showing usage trends of selected unigrams over time
fig = px.line(
    monthly_counts,
    x='month_year',
    y='count',
    color='1-gram',
    title='Trend of Selected Unigrams Over Time (Monthly)',
    labels={
        "month_year": "Month-Year",
        "count": "Frequency",
        "1-gram": "Term"
    }
)

# Render the interactive plot
fig.show()
