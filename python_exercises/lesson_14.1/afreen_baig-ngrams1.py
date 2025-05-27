import pandas as pd
import plotly.express as px

# Define the file path to the dataset
data_path = "data/1-gram.csv"

# Load the CSV file into a DataFrame
df = pd.read_csv(data_path)

# Display the first 10 entries to understand the structure
print(df.head(10))

# Rank the entries by count in descending order and preview the top results
df_sorted = df.sort_values(by='count', ascending=False)
print(df_sorted.head(10))

# Extract only the rows that contain the target unigrams and make a fresh copy
df2 = df[df['1-gram'].isin(["peace", "agreement", "truce"])].copy()
print(df2)

# Combine year, month, and day into a single datetime column
df2 = df2.assign(
    date=pd.to_datetime(df2[['year', 'month', 'day']])
)

# Add a new column that groups entries by month and year
df2 = df2.assign(
    month_year=df2['date'].dt.to_period('M')
)

# Summarize the counts by month-year and unigram
monthly_counts = df2.groupby(['month_year', '1-gram'])['count'].sum().reset_index()

# Convert the period format back into a regular datetime for plotting
monthly_counts['month_year'] = monthly_counts['month_year'].dt.to_timestamp()

# Generate a line chart to visualize monthly trends for each selected unigram
fig = px.line(
    monthly_counts, 
    x='month_year', 
    y='count', 
    color='1-gram',
    title='Trends of Selected Unigrams Over Time',
    labels={
        "month_year": "Month-Year",
        "count": "Frequency",
        "1-gram": "Unigram"
    }
)

# Show the line chart
fig.show()
