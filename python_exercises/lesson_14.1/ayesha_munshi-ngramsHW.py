import pandas as pd
import plotly.express as px

df= pd.read_csv("data/1-gram.csv")
print(df.head())

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

df= df[df["1-gram"].isin(stop_words)]
frequent_unigrams = df.groupby("1-gram")["count"].sum().nlargest(5).index.tolist()
print(frequent_unigrams)
top_5 = df[df["1-gram"].isin(frequent_unigrams)].copy()
print(top_5)

top_5["date"] = pd.to_datetime(top_5[["year", "month", "day"]])

df_plot = top_5.groupby(["date", "1-gram"])["count"].sum().reset_index()
df_monthly = top_5.groupby(["month", "1-gram"])["count"].sum().reset_index()
fig = px.line (
    df_monthly,
    x = "month",
    y = "count",
    color = "1-gram", 
    title = "Frequency of the 5 Most Frequent Unigrams In The Al-Jazeera Corpus",
    labels = {"count": "frequency", "month": "time"},
    markers=True
)
fig.show()
fig.write_html("top_5_unigrams.html")
