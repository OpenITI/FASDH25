import pandas as pd
import plotly.express as px

# Read the CSV file containing 1-gram data
data = pd.read_csv("data/1-gram.csv")

# Rename the column for convenience
data.rename(columns={"1-gram": "word"}, inplace=True)

# Construct a datetime column from year, month, and day
data["timestamp"] = pd.to_datetime(data[["year", "month", "day"]])

# Convert all words to lowercase 
data["word"] = data["word"].str.lower()

# Manually defined stop words (from https://gist.github.com/sebleier/554280)
excluded_words = set([
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves",
    "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their",
    "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are",
    "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an",
    "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about",
    "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up",
    "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when",
    "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no",
    "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don",
    "should", "now"
])

# Eliminate stop words from the dataset
filtered = data[~data["word"].isin(excluded_words)]

# Identify the five most common words based on total count
frequent_words = (
    filtered.groupby("word")["count"]
    .sum()
    .nlargest(5)
    .index
    .tolist()
)

# Focus only on the rows containing those top five words
top_words_df = filtered[filtered["word"].isin(frequent_words)].copy()

# Round datetime to the start of each month for grouping
top_words_df["month"] = top_words_df["timestamp"].dt.to_period("M").dt.to_timestamp()

# Aggregate word counts per word and per month
summary = (
    top_words_df.groupby(["month", "word"])["count"]
    .sum()
    .reset_index()
)

# Create an interactive line chart using Plotly
chart = px.line(
    summary,
    x="month",
    y="count",
    color="word",
    title="Monthly Trends of Top 5 Frequent Words",
    markers=True,
    labels={
        "month": "Month",
        "count": "Frequency",
        "word": "Word"
    }
)

# Export the plot to an HTML file
chart.write_html("Kamil-Ahmad-ngram-homework-plot.html")
