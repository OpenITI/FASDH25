# import necessary libraries
import pandas as pd
import nltk
"""the following libraries code is written with the  help of chatgpt
in order to get rid of making a dictionary for stopwords"""
from nltk.corpus import stopwords
nltk.download('stopwords')
import plotly.express as px

# load the csv data
df = pd.read_csv('data/1-gram.csv')
print(df.columns)
print(df.head())

# Load the NLTK stopword list for English
stop_words = set(stopwords.words('english'))

# Make sure all unigrams are in lowercase for consistent comparisons to stopwords
df['1-gram'] = df['1-gram'].str.lower()

#  Make a filter to pick out words that are NOT in the stopwords list
is_not_stopword = ~df['1-gram'].isin(stop_words)

# Applying the filter to make a new DataFrame without stopwords
# (Learned this method while getting help from ChatGPT)
df_filtered = df[is_not_stopword].copy()

# Check the first few rows of the cleaned data to be sure it worked
print(df_filtered.head())

# Group the words together and add up their total counts
unigram_totals = df_filtered.groupby('1-gram')['count'].sum().reset_index()

# sort the unigrams by total frequency, in descending order
unigram_totals_sorted = unigram_totals.sort_values(by='count', ascending=False)

# Pick out the top 5 most common words
top5_unigrams = unigram_totals_sorted.head(5)

# print the top 5 unigrams and their total counts
print(top5_unigrams)

#Turn those top 5 words into a list so we can use it for filtering later
top_words = top5_unigrams['1-gram'].tolist()

# Make a filter to keep only the rows where the word is one of those top 5
filter_top = df_filtered['1-gram'].isin(top_words)

# Apply the filter to make a new DataFrame with just those top 5 words
df_top = df_filtered[filter_top].copy()

# Group the data by year, month, and word — then add up the counts for each
grouped = df_top.groupby(['year', 'month', '1-gram'])['count'].sum().reset_index()

# Create a proper date column using year and month (day is always 1)
grouped['date'] = pd.to_datetime({
    'year': grouped['year'],
    'month': grouped['month'],
    'day': 1
})

# Check if the new date column looks good
print(grouped[['year', 'month', 'date']].head())


# Change the table shape so each word has its own column, with dates as rows
# (Got help from ChatGPT for the next part)
pivot = grouped.pivot(index='date', columns='1-gram', values='count')

# replace any missing values with 0
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

# Save the chart as an HTML file so it can be opened in a browser
fig.write_html("Zeeshan_karim_top5_unigrams.html")

# Show the plot in the browser or notebook
fig.show()
