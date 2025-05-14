import  pandas  as pd
import plotly.express as px

data_path = "data/1-gram.csv"

# Read 1-gram.csv as a pandas dataframe
df = pd.read_csv(data_path)

# Print the first ten rows
print(df.head(10))

# Sort by the 'frequency' column in descending order and print the top 10 rows
df_sorted = df.sort_values(by='count', ascending=False)
print(df_sorted.head(10))

# Filter the DataFrame to include only specific 1-grams of interest and create a new copy to avoid potential warnings when modifying
df2 = df[df['1-gram'].isin(["peace", "agreement", "truce"])].copy()
print(df2)

# Assign a new 'date' column by combining 'year', 'month', and 'day' columns Using .assign() to avoid SettingWithCopyWarning
df2 = df2.assign(
    date=pd.to_datetime(df2[['year', 'month', 'day']])
)

# Create a 'month_year' column to aggregate data by month, converting to a period
df2 = df2.assign(
    month_year=df2['date'].dt.to_period('M')
)

# Aggregate the data by 'month_year' and '1-gram' to get the total count per month
monthly_counts = df2.groupby(['month_year', '1-gram'])['count'].sum().reset_index()

# Convert 'month_year' to a timestamp for accurate plotting on the x-axis
monthly_counts['month_year'] = monthly_counts['month_year'].dt.to_timestamp()

# Creating the line plot 
fig = px.line(
    monthly_counts, 
    x='month_year', 
    y='count', 
    color='1-gram',
    title='Monthly Frequency of Selected 1-Grams',
    labels={
        "month_year": "Month-Year",
        "count": "Total Count",
        "1-gram": "1-Gram"
    }
)

# Display the plot
fig.show()
