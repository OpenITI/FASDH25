# Loading the necessary libraries
import pandas as pd
import plotly.express as px
import nltk
from nltk.corpus import stopwords

# Download the stopwords dataset from NLTK
nltk.download('stopwords')

# Setting path to the data
data_path = "data/1-gram.csv"

# Read 1-gram.csv as a pandas dataframe
df = pd.read_csv(data_path)

# Print first 40 rows for the later comparison after removing stop words
print("Before removing stop words:")
print(df.head(40))

# Get the list of English stop words
stop_words = set(stopwords.words('english'))

# Create a new dataframe by filtering out stop words using .loc[]
filtered_df = df.loc[df['1-gram'].apply(lambda x: isinstance(x, str) and x.lower() not in stop_words)].copy()

# Drop rows where '1-gram' is None (stop words)
df = df.dropna(subset=['1-gram'])

# Print first 40 rows and compare with earlier 40 rows printed before removing stop words to check whether they have been successfully removed
# from 1-40 I noticed that only "your" was the stop word and it has been removed it means that stop words have been successfully removed from the dataframe
print("\nAfter removing stop words:")
print(filtered_df.head(40))

# Ensure that the count column is numeric
filtered_df['count'] = pd.to_numeric(filtered_df['count'], errors='coerce')

# Convert 'year', 'month', and 'day' columns to a datetime object in filtered_df
filtered_df['date'] = pd.to_datetime(filtered_df[['year', 'month', 'day']])

# Convert 'month' to a new column safely with explicit casting
filtered_df = filtered_df.copy()  # Create a copy to avoid SettingWithCopyWarning
filtered_df['month'] = filtered_df['date'].dt.to_period('M').astype(str)

# Group by date and unigram to aggregate frequencies by date
date_unigram_counts = filtered_df.groupby(['date', '1-gram'])['count'].sum().reset_index()

# Sort by date to ensure we are considering the most recent data first
date_unigram_counts = date_unigram_counts.sort_values('date', ascending=False)

# Now, group by unigram and sum the frequencies after sorting by date
unigram_frequencies = date_unigram_counts.groupby('1-gram')['count'].sum()

# Sort by frequency in descending order and get the top 5 unigrams
top_5_unigrams = unigram_frequencies.sort_values(ascending=False).head(5)

# Print the top 5 unigrams after date sorting
print("\nTop 5 most frequent unigrams after sorting by date:")
print(top_5_unigrams)

# Filter the dataframe to include only the top 5 unigrams
top_5_unigrams_list = top_5_unigrams.index.tolist()
top_5_df = filtered_df[filtered_df['1-gram'].isin(top_5_unigrams_list)]

# Group by month and unigram to calculate the monthly sum of frequencies
monthly_counts = top_5_df.groupby(['month', '1-gram'])['count'].sum().reset_index()

# Create a line plot to visualize the frequency trends of the top 5 unigrams over time
fig = px.line(
    monthly_counts, 
    x='month', 
    y='count', 
    color='1-gram', 
    title="Monthly Frequency of Top 5 Unigrams After Date Sorting",
    labels={'month': 'Month', 'count': 'Frequency', '1-gram': 'Unigram'}
)

# displaying the line plot
fig.show()

# Saving line plot as html
fig.write_html("yasir_top_5_unigrams.html")
