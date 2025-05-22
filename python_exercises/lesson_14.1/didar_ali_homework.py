# import necessary libraries
import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import plotly.express as px

# loading the csv data
df = pd.read_csv('data/1-gram.csv')
print(df.columns)
print(df.head())

# Loading the NLTK stopword list for English
stop_words = set(stopwords.words('english'))

# Lowercase unigrams to maintain consistency when checking against stopwordss
df['1-gram'] = df['1-gram'].str.lower()

#  Filter out stopwords by keeping only words not found in the stopwords list
is_not_stopword = ~df['1-gram'].isin(stop_words)

# Apply the filter to generate a new DataFrame excluding stopwords #Help from ChatGpt
df_filtered = df[is_not_stopword].copy()

# Checking the first few rows of the cleaned data
print(df_filtered.head())

# Group words and calculate the total count for each
unigram_totals = df_filtered.groupby('1-gram')['count'].sum().reset_index()

# Sort the list of unigrams by their total frequency (descending)
unigram_totals_sorted = unigram_totals.sort_values(by='count', ascending=False)

# Get the five most frequent unigrams
top5_unigrams = unigram_totals_sorted.head(5)

# Print the five most common unigrams and their counts
print(top5_unigrams)

# Turn those top 5 words into a list so we can use it for filtering later
top_words = top5_unigrams['1-gram'].tolist()

# Make a filter to keep only the rows where the word is one of those top 5
filter_top = df_filtered['1-gram'].isin(top_words)

# Create a new DataFrame that contains just the top 5 unigrams
df_top = df_filtered[filter_top].copy()

# Group data by year, month, and word, then sum the counts for each group
grouped = df_top.groupby(['year', 'month', '1-gram'])['count'].sum().reset_index()

# Generate a proper date column by combining year and month(day is always 1)
grouped['date'] = pd.to_datetime({
    'year': grouped['year'],
    'month': grouped['month'],
    'day': 1
})

# Checking if the new date column
print(grouped[['year', 'month', 'date']].head())


# Change the table shape so each word has its own column, with dates as rows #Help from ChatGPT
pivot = grouped.pivot(index='date', columns='1-gram', values='count')

# Replace any missing values with 0
pivot.fillna(0, inplace=True)
print(pivot.head())

# Make a line chart to show how the top 5 words trended over time
fig = px.line(
    pivot,
    x=pivot.index,  # Dates on the X-axis
    y=top_words,    # The top words on Y-axis
    title='Top 5 Unigram Frequencies Over Time',
    labels={'value': 'Frequency', 'date': 'Month'},
    markers=True
)

# Save the chart as an HTML file
fig.write_html("Didar_Ali_top5_unigrams.html")

# Display the plot
fig.show()
