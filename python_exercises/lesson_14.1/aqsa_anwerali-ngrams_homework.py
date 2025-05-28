import pandas as pd
import plotly.express as px

#Load the data
df = pd.read_csv("data/1-gram.csv")
print(df.head())

# stop words from NLTK list
stop_words = {
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

#filter out stop words from the corpus
df = df[~df["1-gram"].isin(stop_words)]

#finding first most frequent unigrams in the corpus
top_unigrams = df.groupby("1-gram")["count"].sum().nlargest(5).index.tolist()
print("Top 5 unigrams:", top_unigrams)

#five unigrams
df_top5 = df[df["1-gram"].isin(top_unigrams)]
print(df_top5)


#creating date column for proper time series
df_top5["date"] = pd.to_datetime(df_top5[["year", "month", "day"]])

#Aggregate counts by dat and unigram
df_plot =df_top5.groupby(["date", "1-gram"])["count"].sum().reset_index()

#plottign these five unigrams globally
df_top5['year_month'] = pd.to_datetime(df_top5[['year', 'month']].assign(day=1))
df_monthly = df_top5.groupby(['year_month', '1-gram'])['count'].sum().reset_index()

fig = px.line (
    df_monthly,
    x="year_month", 
    y="count", 
    color="1-gram",
    title="Evolution of Top 5 Unigrams in News Corpus",
    labels={"count": "Frequency", "month": "Time"},
    markers=True
)
fig.show()

#save in html file
fig.write_html("aqsa_anwerali_top_5_unigrams_evolution.html")
