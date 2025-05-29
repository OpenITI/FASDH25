# import pandas
import pandas as pd

# Import Plotly Express for plotting
import plotly.express as px

# load the csv file
df = pd.read_csv("data/1-gram.csv")


# List of common English stop words copied from NLTK's list of english stopwords:
stop_words = [
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your",
    "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her",
    "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs",
    "themselves", "what", "which", "who", "whom", "this", "that", "these", "those",
    "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had",
    "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if",
    "or", "because", "as", "until", "while", "of", "at", "by", "for", "with",
    "about", "against", "between", "into", "through", "during", "before", "after",
    "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over",
    "under", "again", "further", "then", "once", "here", "there", "when", "where",
    "why", "how", "all", "any", "both", "each", "few", "more", "most", "other",
    "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too",
    "very", "s", "t", "can", "will", "just", "don", "should", "now"
]

# Create a new DataFrame that excludes rows where the "1-gram" word is in the stop_words list
df_no_stop = df[df["1-gram"].isin(stop_words) == False]

# Group by each unique word (1-gram) and sum up their counts to get the total mentions of each word in the entire dataset
total_counts = df_no_stop.groupby("1-gram")["count"].sum()

# Sort the words by their total counts in descending order to get the most frequent words first
sorted_counts = total_counts.sort_values(ascending=False)

# Display the first few entries to check the output
print(sorted_counts.head())

# Select the top 5 most frequent words
top_5 = sorted_counts.head(5)

# Display the top 5 words and their total counts
print("Top 5 most frequent unigrams:")
print(top_5)

# Filter the original dataframe to include only the top 5 words
df_top_5 = df_no_stop[df_no_stop["1-gram"].isin(top_5.index)]

# Display the filtered data to verify the output
print(df_top_5.head())

# Create a new datetime column for grouping (set day=1)
df_top_5.loc[:, 'date'] = pd.to_datetime(df_top_5[['year', 'month']].assign(day=1))

# Group by date and word, sum counts
monthly_counts = df_top_5.groupby(['date', '1-gram'])['count'].sum().reset_index()


# Plot the line graph
fig = px.line(monthly_counts, x="date", y="count", color="1-gram", title="Frequency of Top 5 Words Over Time")

fig.write_html("output.html")
# Show the graph
fig.show()






