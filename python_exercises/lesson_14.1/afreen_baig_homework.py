# Import necessary libraries
import pandas as pd
import plotly.express as px
import nltk
from nltk.corpus import stopwords

# Make sure stopwords are downloaded for filtering
nltk.download('stopwords')

# Specify the location of the CSV file
data_path = "data/1-gram.csv"

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(data_path)

# Display the first 40 rows before cleaning for comparison
print("Initial data (before removing stop words):")
print(df.head(40))

# Get a set of standard English stop words
stop_words = set(stopwords.words('english'))

# Remove rows where the unigram is a stop word (ignoring case)
filtered_df = df.loc[df['1-gram'].apply(lambda x: isinstance(x, str) and x.lower() not in stop_words)].copy()

# Eliminate rows with missing values in the '1-gram' column
df = df.dropna(subset=['1-gram'])

# Show the top 40 rows after removing stop words for verification
print("\nCleaned data (after removing stop words):")
print(filtered_df.head(40))

# Make sure 'count' column is treated as numeric
filtered_df['count'] = pd.to_numeric(filtered_df['count'], errors='coerce')

# Combine year, month, and day into a single datetime column
filtered_df['date'] = pd.to_datetime(filtered_df[['year', 'month', 'day']])

# Create a 'month' column as a formatted period string (e.g., '2023-03')
filtered_df['month'] = filtered_df['date'].dt.to_period('M').astype(str)

# Calculate total frequency of each unigram by date
date_unigram_counts = filtered_df.groupby(['date', '1-gram'])['count'].sum().reset_index()

# Sort the records from most recent to oldest by date
date_unigram_counts = date_unigram_counts.sort_values('date', ascending=False)

# Sum up total frequency per unigram across all dates
unigram_frequencies = date_unigram_counts.groupby('1-gram')['count'].sum()

# Identify the top 5 most frequent unigrams
top_5_unigrams = unigram_frequencies.sort_values(ascending=False).head(5)

# Display the top unigrams based on frequency
print("\nMost frequent 5 unigrams (after sorting by date):")
print(top_5_unigrams)

# Keep only the rows corresponding to the top 5 unigrams
top_5_unigrams_list = top_5_unigrams.index.tolist()
top_5_df = filtered_df[filtered_df['1-gram'].isin(top_5_unigrams_list)]

# Calculate total monthly frequency per top unigram
monthly_counts = top_5_df.groupby(['month', '1-gram'])['count'].sum().reset_index()

# Create a line chart to show trends over time
fig = px.line(
    monthly_counts, 
    x='month', 
    y='count', 
    color='1-gram', 
    title="Top 5 Unigram Trends by Month",
    labels={'month': 'Month', 'count': 'Frequency', '1-gram': 'Unigram'}
)

# Show the interactive chart
fig.show()

# Save the chart as an HTML file
fig.write_html("n-afreen-baig_unigrams.html")
