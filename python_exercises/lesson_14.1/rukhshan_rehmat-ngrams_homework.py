# Loading the necessary libraries
import pandas as pd
import plotly.express as px
import nltk
from nltk.corpus import stopwords

# Download the stopwords dataset from NLTK
nltk.download('stopwords')

# Set path to the data
data_path = "data/1-gram.csv"

# Read 1-gram.csv as a pandas dataframe
df = pd.read_csv(data_path)

# Print first 40 rows before removing stop words
print("Before removing stop words:")
print(df.head(40))

# Get list of English stop words
stop_words = set(stopwords.words('english'))

# Filter out stop words
filtered_df = df.loc[df['1-gram'].apply(lambda x: isinstance(x, str) and x.lower() not in stop_words)].copy()

# Print first 40 rows after removing stop words
print("\nAfter removing stop words:")
print(filtered_df.head(40))

# Ensure count column is numeric
filtered_df['count'] = pd.to_numeric(filtered_df['count'], errors='coerce')

# Convert year, month, day into a datetime column
filtered_df['date'] = pd.to_datetime(filtered_df[['year', 'month', 'day']])

# Create a 'month_year' column in YYYY-MM format
filtered_df['month'] = filtered_df['date'].dt.to_period('M').astype(str)

# Group by unigram and sum total frequency
top_5_unigrams = filtered_df.groupby('1-gram')['count'].sum().sort_values(ascending=False).head(5)
print("\nTop 5 most frequent unigrams:")
print(top_5_unigrams)

# Filter DataFrame for only the top 5 unigrams
top5_list = top_5_unigrams.index.tolist()
top5_df = filtered_df[filtered_df['1-gram'].isin(top5_list)]

# Group by month and unigram to sum frequencies
monthly_counts = top5_df.groupby(['month', '1-gram'])['count'].sum().reset_index()

# Create line plot
fig = px.line(
    monthly_counts,
    x='month',
    y='count',
    color='1-gram',
    title="Monthly Frequency of Top 5 Unigrams (Excluding Stopwords)",
    labels={'month': 'Month', 'count': 'Frequency', '1-gram': 'Unigram'}
)

# Save plot to HTML file
fig.write_html("rukhshan_top5_1grams_plot.html")

# Show the plot
fig.show()

