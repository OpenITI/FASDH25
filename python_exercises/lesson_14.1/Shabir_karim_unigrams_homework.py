# import necessary libraries
import pandas as pd
import nltk
"""For the following libraries, the code was adapted with the help of ChatGPT
in order to avoid manually creating a dictionary for stopwords."""
from nltk.corpus import stopwords
nltk.download('stopwords')
import plotly.express as px

# load the csv data
df = pd.read_csv('data/1-gram.csv')
print(df.columns)
print(df.head())

# Load the NLTK stopword list for English

stop_words = set(stopwords.words('english'))

# Convert all unigrams to lowercase so we can compare them to stopwords

df['1-gram'] = df['1-gram'].str.lower()

# Create a boolean filter to keep only non-stopwords

is_not_stopword = ~df['1-gram'].isin(stop_words)

# Apply the filter to make a new DataFrame without stopwords
# Code adapted with the help of CHATGPT

df_filtered = df[is_not_stopword].copy()

# print the first few rows for the confirmation of results

print(df_filtered.head())

# group the data by unigram and calculate total count for each word

unigram_totals = df_filtered.groupby('1-gram')['count'].sum().reset_index()

# sort the unigrams by total frequency, in descending order

unigram_totals_sorted = unigram_totals.sort_values(by='count', ascending=False)

# select the top 5 most frequent unigrams

top5_unigrams = unigram_totals_sorted.head(5)

#print the top 5 unigrams and their total counts

print(top5_unigrams)

# get the list of top 5 unigrams

top_words = top5_unigrams['1-gram'].tolist()

# Keep only rows where the unigram is in the top 5 list

filter_top = df_filtered['1-gram'].isin(top_words)

# Create a new DataFrame with just those top words

df_top = df_filtered[filter_top].copy()

# group by year, month, and 1-gram, then sum the 'count' values

grouped = df_top.groupby(['year', 'month', '1-gram'])['count'].sum().reset_index()

# Create a date column using year and month (always set day=1)

grouped['date'] = pd.to_datetime({
    'year': grouped['year'],
    'month': grouped['month'],
    'day': 1
})
# check the new date column

print(grouped[['year', 'month', 'date']].head())

#Learn the following chunk of codes from chatgpt
# Pivot the table: rows = date, columns = unigrams, values = count
pivot = grouped.pivot(index='date', columns='1-gram', values='count')

# replace any missing values with 0
print(pivot.head())

# Create a line plot for all 5 unigrams
fig = px.line(pivot,
              title='Top 5 Unigram Frequencies Over Time',
              labels={'value': 'Frequency', 'date': 'Month'},
              markers=True)

# Save the plot to an HTML file
fig.write_html("shabir_karim_top5_unigrams.html")

# Show the plot in the browser or notebook
fig.show()














