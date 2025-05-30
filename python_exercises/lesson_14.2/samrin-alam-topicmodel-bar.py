import pandas as pd
import plotly.express as px

# Load the topic model data from CSV file
df = pd.read_csv("data/topic-model.csv")

# Display the first few rows to understand the data
print(df.head())

# Print the first few titles to understand topic content (optional)
print("Sample Titles:\n", df['title'].head())

# Remove rows with unassigned topics (Topic = -1)
df = df[df["Topic"] != -1]

# Create a descriptive label for each topic by combining keywords
df["Topic_Label"] = df[["topic_1", "topic_2", "topic_3", "topic_4"]].agg(", ".join, axis=1)

# Group the data by topic label and publication year and count articles
grouped = df.groupby(["Topic_Label", "year"]).size().reset_index(name="Article_Count")

# Select top 5 most frequent topics overall
top_5_topics = grouped.groupby("Topic_Label")["Article_Count"].sum().nlargest(5).index

# Filter the grouped data for only those top 5 topics
grouped_top5 = grouped[grouped["Topic_Label"].isin(top_5_topics)]

# Create an grouped bar chart
fig = px.bar(
    grouped_top5,
    x='year',
    y='Article_Count',
    color='Topic_Label',
    barmode='group',
    title='Top 5 Topics: Article Counts by Year',
    labels={'Topic_Label': 'Topic', 'Article_Count': 'Number of Articles', 'year': 'Year'}
)

# Save the chart as HTML
fig.write_html("samrin-alam-topicmodel-bar.html")

# Show the chart
fig.show()
