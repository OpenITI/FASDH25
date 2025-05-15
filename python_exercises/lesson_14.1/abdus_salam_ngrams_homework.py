# Import necessary libraries
import pandas as pd
import plotly.express as px
import nltk
from nltk.corpus import stopwords

# Download stopwords
nltk.download('stopwords')

# Load the CSV file
df = pd.read_csv("../lesson_14.1/data/1-gram.csv")

# Get list of English stopwords
stop_words = set(stopwords.words('english'))

# Remove stopwords from the DataFrame
# This keeps only rows where the 1-gram is NOT in stopwords
non_stopword_filter = ~df["1-gram"].isin(stop_words)
df = df[non_stopword_filter]
print("After removing stopwords:")
print(df.head(10))

#  Find the top 5 most frequent 1-grams overall
top_5_df = df.groupby("1-gram")["count"].sum().sort_values(ascending=False).head(5)
print("Top 5 most frequent non-stopword 1-grams:")
print(top_5_df)

#  Filter the original dataframe for just those top 5 unigrams
top5_words = top_5_df.index.tolist()
filter = df["1-gram"].isin(top5_words)
df2 = df[filter].copy()  # .copy() to avoid SettingWithCopyWarning
print("Filtered DataFrame (top 5 1-grams):")
print(df2.head(10))

#  Create a 'date' column by combining year, month, and day
df2["date"] = pd.to_datetime({
    "year": df2["year"],
    "month": df2["month"],
    "day": df2["day"]
})

# Create a 'month_year' column for grouping by month
df2["month_year"] = df2["date"].dt.to_period("M")

# Group by month and 1-gram, sum the counts
grouped = df2.groupby(["month_year", "1-gram"])["count"].sum().reset_index()

# Convert month_year to full date format for plotting
grouped["month_year"] = grouped["month_year"].dt.to_timestamp()

# Plot the line graph
fig = px.line(grouped, x="month_year", y="count", color="1-gram",
              title="Top 5 Most Frequent 1-grams Over Time (Excluding Stopwords)")

#  Save the plot to an HTML file
fig.write_html("abdus_salam_top5_homework_plot.html")

# Show the plot
fig.show()
