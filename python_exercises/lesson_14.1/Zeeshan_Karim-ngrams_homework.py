#importing libraries
import pandas as pd
import plotly.express as px
import nltk
from nltk.corpus import stopwords

# Download stopwords
nltk.download('stopwords')
#loading dataframe
df = pd.read_csv('data/1-gram.csv')
print(df.head())

# Step 1: Load a list of English stop words (using NLTK)
import nltk
from nltk.corpus import stopwords

# Download stopwords if not already downloaded
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Step 2: Remove stop words from the DataFrame
df = df[~df['1-gram'].isin(stop_words)]

# Step 3: Find the top 5 most frequent unigrams (globally, not per month)
top5_words = (
    df.groupby('1-gram')['count']
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .index.tolist()
)

print("Top 5 most frequent words:", top5_words)

# Step 4: Filter the DataFrame for these top 5 words
df_top5 = df[df['1-gram'].isin(top5_words)].copy()

# Step 5: Create a proper datetime column for grouping by month
df_top5['date'] = pd.to_datetime({
    'year': df_top5['year'],
    'month': df_top5['month'],
    'day': df_top5['day']
})

# Step 6: Create a month-year column for grouping
df_top5['month_year'] = df_top5['date'].dt.to_period('M')

# Step 7: Group by month and word, summing the counts
grouped = (
    df_top5.groupby(['month_year', '1-gram'])['count']
    .sum()
    .reset_index()
)

# Step 8: Convert period to timestamp for plotting
grouped['month_year'] = grouped['month_year'].dt.to_timestamp()

# Step 9: Plot the line graph
fig = px.line(grouped,
              x='month_year',
              y='count',
              color='1-gram',
              markers=True,
              title='Top 5 Most Frequent Non-Stopword Unigrams Over Time')

fig.show()
