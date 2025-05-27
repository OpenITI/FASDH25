import pandas as pd
import nltk
import plotly.express as px
from nltk.corpus import stopwords

nltk.download('stopwords')

# Load the unigram data
data_path = 'data/1-gram.csv'
df = pd.read_csv(data_path)

# Load English stopwords
english_stopwords = set(stopwords.words('english'))

# Normalize unigrams to lowercase
df['1-gram'] = df['1-gram'].str.lower()

# Remove stopwords
df_no_stopwords = df[~df['1-gram'].isin(english_stopwords)].copy()

# Calculate total counts for each unigram
total_counts = df_no_stopwords.groupby('1-gram')['count'].sum().reset_index()

# Select top 5 unigrams by total frequency
top_5_unigrams = total_counts.sort_values(by='count', ascending=False).head(5)['1-gram'].tolist()

# Filter dataframe to include only top 5 unigrams
top_unigrams_df = df_no_stopwords[df_no_stopwords['1-gram'].isin(top_5_unigrams)].copy()

# Group by year, month, and unigram; sum counts
monthly_counts = top_unigrams_df.groupby(['year', 'month', '1-gram'])['count'].sum().reset_index()

# Create datetime column for plotting
monthly_counts['date'] = pd.to_datetime(dict(year=monthly_counts['year'],
                                            month=monthly_counts['month'],
                                            day=1))

# Pivot for plotting: dates as rows, unigrams as columns
frequency_pivot = monthly_counts.pivot(index='date', columns='1-gram', values='count').fillna(0)

# Plot the line graph
fig = px.line(frequency_pivot,
              title='Monthly Frequency Trends of Top 5 Unigrams in al-Jazeera Corpus',
              labels={'value': 'Frequency', 'date': 'Month'},
              markers=True)

# Save plot as HTML
fig.write_html('kamran_abid_top5_unigrams_plot.html')

# Display the plot
fig.show()
