import pandas as pd
import plotly.express as px

#loads csv file
df = pd.read_csv('data/1-gram.csv')
print(df.head())

#list of stopwords from NLTK's list of english stopwords
stop_words = set([
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you',
    'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his',
    'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself',
    'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which',
    'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are',
    'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having',
    'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if',
    'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for',
    'with', 'about', 'against', 'between', 'into', 'through', 'during',
    'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in',
    'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then',
    'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any',
    'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no',
    'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's',
    't', 'can', 'will', 'just', 'don', 'should', 'now'
])

#Filter out stop words
df = df[~df['1-gram'].isin(stop_words)]

#finding the 5 most frequent unigrams globally
top_words = (
    df.groupby('1-gram')['count']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("Top 5 most frequent unigrams:")
print(top_words)

# Keep only rows where the 1-gram is in the top 5
top_words_list = top_words.index.tolist()
df_top = df[df['1-gram'].isin(top_words_list)]

# Create a 'date' column for time-based plotting
df_top = df_top.copy()  
df_top['date'] = pd.to_datetime(df_top[['year', 'month', 'day']])

# Group by date and 1-gram to get total mentions per day per word
df_grouped = df_top.groupby(['date', '1-gram'])['count'].sum().reset_index()

# Plot using Plotly
fig = px.line(df_grouped, x='date', y='count', color='1-gram',
              title='Evolution of the Top 5 Most Frequent Unigrams Over Time',
              labels={'count': 'Mentions', 'date': 'Date', '1-gram': 'Word'})

fig.show()
        
