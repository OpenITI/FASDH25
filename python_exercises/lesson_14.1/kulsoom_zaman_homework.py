import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv('data/1-gram.csv') 
print(df.head())
#custom stopwords I took from NLTK's list
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
#filter out where the corpus is an English stop word
df = df[~df['1-gram'].isin(custom_stopwords)]

# Group by '1-gram' and sum counts to find the most frequent unigrams globally
top_unigrams = df.groupby('1-gram')['count'].sum().nlargest(5).index.tolist()
print("Top 5 unigrams:", top_unigrams)
#top five unigrams 
df_top5 = df[df['1-gram'].isin(top_unigrams)]
print(df_top5)

# 5. Create date column for proper time series
df_top5['date'] = pd.to_datetime(df_top5[['year', 'month', 'day']])

# 6. Aggregate counts by date and unigram
df_plot = df_top5.groupby(['date', '1-gram'])['count'].sum().reset_index()

#ploting the evolutoin of these 5 unigrams in the coprus globally
df_top5['year_month'] = pd.to_datetime(df_top5[['year', 'month']].assign(day=1))
df_monthly = df_top5.groupby(['year_month', '1-gram'])['count'].sum().reset_index()

fig = px.line(
    df_monthly, 
    x="year_month", 
    y="count", 
    color="1-gram",
    title="Evolution of Top 5 Unigrams in News Corpus",
    labels={"count": "Frequency", "year_month": "Month"},
    markers=True
)
fig.show()
#saving html file
fig.write_html("kulsoom_zaman_top_5_unigrams_evolution.html")


