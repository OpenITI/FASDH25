# Importing necessary libraries 
import pandas as pd
import plotly.express as px
import nltk
from nltk.corpus import stopwords

# Download the stopwords from NLTK
nltk.download('stopwords')

# Load the CSV file into a dataframe
df = pd.read_csv("../lesson_14.1/data/1-gram.csv")

# Get the list of stopwords in English
stop_words = set(stopwords.words('english'))

# Remove rows where the 1-gram is a stopword
non_stopword_filter = ~df["1-gram"].isin(stop_words)
df = df[non_stopword_filter]
print("After removing stopwords:")
print(df.head(10))

# Find the top 5 most frequent 1-grams overall
top_5_df = df.groupby("1-gram")["count"].sum().sort_values(ascending=False).head(5)
print("Top 5 most frequent non-stopword 1-grams:")
print(top_5_df)

# Filter the original dataframe for just those top 5 unigrams
top5_words = top_5_df.index.tolist()
filter = df["1-gram"].isin(top5_words)
df2 = df[filter].copy()  # Copying to avoid warning
print("Filtered DataFrame (top 5 1-words):")
print(df2.head(10))

# Combine year, month, and day to make a full 'date' column
df2["date"] = pd.to_datetime({
    "year": df2["year"],
    "month": df2["month"],
    "day": df2["day"]
})

# Create a 'month_year' column for grouping by month
df2["month_year"] = df2["date"].dt.to_period("M")

# Group by month and 1-gram and sum the counts
grouped = df2.groupby(["month_year", "1-gram"])["count"].sum().reset_index()

# Convert month_year back to full date format for plotting 
grouped["month_year"] = grouped["month_year"].dt.to_timestamp()

# Plotting the line graph for top 5 1-grams 
fig = px.line(grouped, x="month_year", y="count", color="1-gram",
              title="Top 5 Most Frequent 1-grams Over Time (Excluding Stopwords)")

# Save the plot as an HTML file
fig.write_html("bushra_hoorani_top5_homework_plot.html")

# Show the plot
fig.show()
