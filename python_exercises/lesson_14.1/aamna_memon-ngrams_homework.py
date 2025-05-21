import pandas as pd
import plotly.express as px

df= pd.read_csv('data/1-gram.csv')

#step 1
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
stopwords=set(ENGLISH_STOP_WORDS)
stopwords.update(['s','said', 'al'])
df_filtered=df[~df['1-gram'].isin(stopwords)].copy()

#step 2
five_ngram_global = df_filtered.groupby('1-gram')['count'].sum(
    ).sort_values(ascending =False).head(5)


#step 3
df_filtered['date']=pd.to_datetime(dict(
    year=df_filtered['year'],
    month=df_filtered['month'],
    day=1
    ))

top_five     = five_ngram_global.index
df_top_five  = df_filtered[df_filtered['1-gram'].isin(top_five)]

grouped_df=df_top_five.groupby(
    ['date','1-gram'],as_index=False)['count'].sum()

fig=px.line(grouped_df,
            x='date',
            y='count',color='1-gram',
            markers=True,
            title='Top 5 1-grams over time')
fig.write_html('aamna_homework.html')
