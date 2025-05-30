#importing the necessary libraries
import pandas as pd
import plotly.express as px
#imported nltk for the stop words of English
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

# Load CSV data
df = pd.read_csv("data/1-gram.csv")
print(df.head())

# Combine year, month, day into a single datetime column
df['date'] = pd.to_datetime(df[['year', 'month', 'day']])

# Get English stopwords
stop_words = set(stopwords.words('english'))

# Remove stop words
df = df[~df["1-gram"].isin(stop_words)]

# Finding top 5 most frequent unigrams overall (sum counts across all dates)
top_words = df.groupby("1-gram")["count"].sum().nlargest(5).index.tolist()
print("Top 5 unigrams:", top_words)

# Filter dataframe to keep only top 5 words
df_top = df[df["1-gram"].isin(top_words)].copy()
print(df_top.head())

# Create a "month" column for grouping
df_top["month"] = df_top["date"].dt.to_period("M").dt.to_timestamp()

# Group by month and unigram, sum counts
df_monthly = df_top.groupby(["month", "1-gram"], as_index=False)["count"].sum()

# Plotting
fig = px.line(
    df_monthly,
    x="month", 
    y="count", 
    color="1-gram",
    title="Evolution of Top 5 Unigrams in News Corpus",
    labels={"count": "Frequency", "month": "Time", "1-gram": "Unigram"},
    markers=True
)

# Saving as HTML
fig.write_html('Rifat_Jahan-top_5_unigrams_plot.html')
fig.show()




