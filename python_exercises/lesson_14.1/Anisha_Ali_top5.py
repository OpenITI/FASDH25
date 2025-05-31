import pandas as pd
import plotly.express as px

# Loading data
df = pd.read_csv('data/1-gram.csv') 
print(df.head())

# Custom stopwords from NLTK
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

#keeping the rows only where the word is not a stopword
df = df[~df['1-gram'].isin(custom_stopwords)]

#finding the most common  5 words in the dataframe and extracting thier frequency per date
top_5_grams = df.groupby('1-gram')['count'].sum().nlargest(5).index.tolist()
df_top5 = df[df['1-gram'].isin(top_5_grams)].copy()
print(df_top5)

#add a date column for time-series plotting
df_top5['date'] = pd.to_datetime(df_top5[['year', 'month']].assign(day=1))


#summing how often each of the top five words appear per month
df_top5['year_month'] = pd.to_datetime(df_top5[['year', 'month']].assign(day=1))
df_monthly = df_top5.groupby(['year_month', '1-gram'])['count'].sum().reset_index()

df_monthly = df_top5.groupby(['date', '1-gram'])['count'].sum().reset_index()

#plotting
fig = px.line(
    df_monthly, 
    x="date", 
    y="count", 
    color="1-gram",
    title="Evolution of Top 5 Unigrams in News Corpus",
    labels={"count": "Frequency", "date": "Month"},
    markers=True
)

fig.show()

#save as HTML
fig.write_html("Anisha_Ali_top5_evolutions.html")

