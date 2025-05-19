import pandas as pd
import plotly.express as px
from nltk.corpus import stopwords
import nltk

# Download stopwords if not already done
nltk.download("stopwords")

# Step 1: Load the CSV file
df = pd.read_csv("data/1-gram.csv")

# Step 2: Remove stopwords
stop_words = set(stopwords.words("english"))
df = df[~df["1-gram"].isin(stop_words)]

# Step 3: Find the 5 most frequent unigrams (globally)
top5 = df.groupby("1-gram", as_index=False)["count"].sum().sort_values(by="count", ascending=False).head(5)
top5_words = top5["1-gram"].tolist()

# Step 4: Filter original dataframe for these top 5 unigrams
df_top5 = df[df["1-gram"].isin(top5_words)]

# Step 5: Create datetime column and monthly grouping
df_top5["date"] = pd.to_datetime(df_top5[["year", "month", "day"]])
df_top5["month"] = df_top5["date"].dt.to_period("M").dt.to_timestamp()

df_monthly = df_top5.groupby(["month", "1-gram"], as_index=False)["count"].sum()

# Step 6: Plot the line graph
fig = px.line(
    df_monthly,
    x="month",
    y="count",
    color="1-gram",
    title="Monthly Frequency of Top 5 Non-Stopword Unigrams",
    labels={"month": "Month", "count": "Frequency", "1-gram": "Unigram"}
)
fig.show()
