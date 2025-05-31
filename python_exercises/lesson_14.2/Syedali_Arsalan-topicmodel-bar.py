
# Load necessary libraries for visualizations
import pandas as pd
import plotly.express as px

# Set path to data
data_path = "data/topic-model.csv"

# Read topic-model.csv as a pandas dataframe
df = pd.read_csv(data_path)

# Filter out rows with Topic == -1, which usually means unclassified/noise
df = df[df["Topic"] != -1]

# Create a readable label for each topic using its top keywords
df["Topic_Label"] = df[["topic_1", "topic_2", "topic_3", "topic_4"]].agg(", ".join, axis=1)

# Group data by topic and year to count number of articles
grouped = df.groupby(["Topic_Label", "year"]).size().reset_index(name="Article_Count")

# Identify top 5 most frequent topics across all years
top_topics = grouped.groupby("Topic_Label")["Article_Count"].sum().nlargest(5).index
grouped = grouped[grouped["Topic_Label"].isin(top_topics)]

# Create a bar chart with grouped bars by year
fig = px.bar(grouped,
             x="Topic_Label",
             y="Article_Count",
             color="year",
             barmode="group",
             labels={"year": "Year", "Article_Count": "Number of Articles", "Topic_Label": "Topic"},
             title="Top 5 Topics by Article Count and Year",
             hover_data={"Topic_Label": True, "year": True})

# Show the chart
fig.show()

# Save the chart as HTML
fig.write_html("Syedali-Arsalan-topicmodel-bar.html")
