import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('data/1-gram.csv') 
print(df.head())

# Custom stopwords taken from NLTK's list
custom_stopwords = {
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 
    'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 
    'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 
    'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 
    'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 
    'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 
    'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 
    'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 
    'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 
    'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 
    'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 
    'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now'
}

# Filter out stop words
df = df[~df['1-gram'].isin(custom_stopwords)]

# Find top 5 most frequent unigrams in the entire corpus
top_unigrams = df.groupby('1-gram')['count'].sum().nlargest(5).index.tolist()
print("Top 5 unigrams:", top_unigrams)

# Filter for top 5 unigrams
df_top5 = df[df['1-gram'].isin(top_unigrams)].copy()

# Create a date column (for grouping by month, day is kept but can be ignored)
df_top5['date'] = pd.to_datetime(df_top5[['year', 'month', 'day']])

# Aggregate counts by month and unigram
df_monthly = df_top5.groupby([df_top5['date'].dt.to_period('M'), '1-gram'])['count'].sum().reset_index()
df_monthly['date'] = df_monthly['date'].dt.to_timestamp()

# Plot the evolution of top 5 unigrams per month
fig = px.line(
    df_monthly,
    x="date",
    y="count",
    color="1-gram",
    title="Monthly Frequency Evolution of Top 5 Unigrams in News Corpus",
    labels={"count": "Frequency", "date": "Month"},
    markers=True
)

fig.show()

# Save plot as HTML file
fig.write_html("top5_unigrams_evolution.html")
