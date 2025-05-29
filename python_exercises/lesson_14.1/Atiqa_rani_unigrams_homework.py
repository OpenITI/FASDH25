# Import required libraries
import pandas as pd
import plotly.express as px
import nltk
from nltk.corpus import stopwords

# Download stopwords (only needed the first time)
nltk.download('stopwords')

# Load the unigram dataset
data = pd.read_csv('data/1-gram.csv')

# Convert all unigrams to lowercase for consistent comparison
data['1-gram'] = data['1-gram'].str.lower()

# Get the list of English stopwords
english_stopwords = set(stopwords.words('english'))

# Filter out the rows where the unigram is a stopword
non_stopword_mask = ~data['1-gram'].isin(english_stopwords)
cleaned_data = data[non_stopword_mask].copy()

# Group by unigram and calculate the total frequency
total_counts = cleaned_data.groupby('1-gram')['count'].sum().reset_index()

# Sort by frequency and pick the top 5 unigrams
top_unigrams = total_counts.sort_values(by='count', ascending=False).head(5)
top_words = top_unigrams['1-gram'].tolist()

# Filter the cleaned data to include only the top 5 unigrams
top_only = cleaned_data[cleaned_data['1-gram'].isin(top_words)].copy()

# Group by year, month, and unigram to get monthly totals
monthly_counts = top_only.groupby(['year', 'month', '1-gram'])['count'].sum().reset_index()

# Create a proper date column (day is always set to 1)
monthly_counts['date'] = pd.to_datetime({
    'year': monthly_counts['year'],
    'month': monthly_counts['month'],
    'day': 1
})

# Pivot the data: rows = date, columns = unigrams, values = count
reshaped = monthly_counts.pivot(index='date', columns='1-gram', values='count')

# Create a line plot using Plotly
fig = px.line(
    reshaped,
    title='Monthly Trends of Top 5 Unigrams (Excluding Stopwords)',
    labels={'value': 'Frequency', 'date': 'Month'},
    markers=True
)

# Save the interactive plot as an HTML file
fig.write_html("Atiq_rani_top5_unigrams.html")

# Show the plot
fig.show()
