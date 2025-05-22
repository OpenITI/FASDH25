import pandas as pd
import plotly.express as px

# To load the data
df = pd.read_csv('data/1-gram.csv')

# Stopwords list
stopwords = {
        'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves',
    'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him',
    'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its',
    'itself', 'they', 'them', 'their', 'theirs', 'themselves',
    'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those',
    'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have',
    'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an',
    'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while',
    'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between',
    'into', 'through', 'during', 'before', 'after', 'above', 'below',
    'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over',
    'under', 'again', 'further', 'then', 'once', 'here', 'there',
    'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each',
    'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor',
    'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very',
    'can', 'will', 'just', 'don', 'should', 'now'
}

# Removing stopwords
df = df[~df['1-gram'].isin(stopwords)]

# Find the 5 most used words in the corpus
top5 = df.groupby('1-gram')['count'].sum().nlargest(5).index.tolist()

# Get rows with top 5 words and copy them
df_top5 = df[df['1-gram'].isin(top5)].copy()

# Create a new column with year and month
df_top5['year_month'] = df_top5['year'].astype(str) + "-" + df_top5['month'].astype(str).str.zfill(2)

# Organize the data by month and each word (1-gram)
df_grouped = df_top5.groupby(['year_month', '1-gram'])['count'].sum().reset_index()

# Plot the grouped data using Plotly
fig = px.line(
    df_grouped,
    x='year_month',
    y='count',
    color='1-gram',
    title='Top 5 Unigrams Over Time (Excluding Stopwords)',
    labels={'count': 'Frequency', 'year_month': 'Month'},
    markers=True
)

# Save the plot as HTML file
fig.write_html("ihtisham_top5_unigrams_plot.html")
# show the plot
fig.show()
