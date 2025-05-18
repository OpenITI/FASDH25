import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('data/1-gram.csv') 
print(df.head())

#words from NLTK 
stop_words = [
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and",
    "any", "are", "aren't", "as", "at", "be", "because", "been", "before", "being",
    "below", "between", "both", "but", "by", "can", "can't", "cannot", "could",
    "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't", "down",
    "during", "each", "few", "for", "from", "further", "had", "hadn't", "has",
    "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her",
    "here", "here's", "hers", "herself", "him", "himself", "his", "how", "how's",
    "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't", "it",
    "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my",
    "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or",
    "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same",
    "shan't", "she", "she'd", "she'll", "she's", "should", "shouldn't", "so",
    "some", "such", "than", "that", "that's", "the", "their", "theirs", "them",
    "themselves", "then", "there", "there's", "these", "they", "they'd", "they'll",
    "they're", "they've", "this", "those", "through", "to", "too", "under",
    "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're",
    "we've", "were", "weren't", "what", "what's", "when", "when's", "where",
    "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with",
    "won't", "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've",
    "your", "yours", "yourself", "yourselves"
]
#filter from the English stop word
df = df[~df['1-gram'].isin(stop_words)]

#Group by '1-gram' and sum counts to find the most frequent unigrams globally
top_unigrams = df.groupby('1-gram')['count'].sum().nlargest(5).index.tolist()
print("Top 5 unigrams:", top_unigrams)
#top five unigrams 
df_top5 = df[df['1-gram'].isin(top_unigrams)]
print(df_top5)

#Create date column for proper time series
df_top5['date'] = pd.to_datetime(df_top5[['year', 'month', 'day']])

#Aggregate counts by date and unigram
df_plot = df_top5.groupby(['date', '1-gram'])['count'].sum().reset_index()

#ploting the evolutoin of these 5 unigrams in the coprus globally
df_monthly = df_top5.groupby(['month', '1-gram'])['count'].sum().reset_index()
fig = px.line(
    df_monthly, 
    x="month", 
    y="count", 
    color="1-gram",
    title="Evolution of Top 5 Unigrams in News Corpus",
    labels={"count": "Frequency", "month": "Time"},
    markers=True
)
fig.show()

