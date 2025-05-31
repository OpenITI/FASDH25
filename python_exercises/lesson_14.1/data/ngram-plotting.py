# Import libraries
import pandas as pd
import plotly.express as px
import nltk
from nltk.corpus import stopwords

# Download NLTK stopword list
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Load the unigrams CSV
df = pd.read_csv("lesson_14.1\data")

# Remove stop words
df = df[~df['unigram'].str.lower().isin(stop_words)]

# Find the 5 most frequent unigrams across the entire dataset
top5_unigrams = df.groupby('unigram')['frequency'].sum().nlargest(5).index.tolist()

# Filter to only top 5 unigrams
df_top5 = df[df['unigram'].isin(top5_unigrams)]

# Convert date to datetime and extract month
df_top5['date'] = pd.to_datetime(df_top5['date'])
df_top5['month'] = df_top5['date'].dt.to_period('M').dt.to_timestamp()

# Group by month and unigram, sum frequencies
monthly_freq = df_top5.groupby(['month', 'unigram'])['frequency'].sum().reset_index()

# Plot using Plotly
fig = px.line(monthly_freq, x='month', y='frequency', color='unigram',
              title='Monthly Frequency of Top 5 Unigrams in al-Jazeera Corpus (After Removing Stop Words)',
              labels={'month': 'Month', 'frequency': 'Frequency', 'unigram': 'Unigram'})

# Save to HTML
fig.write_html("top5_unigram_plot.html")
print("Plot saved as top5_unigram_plot.html")
