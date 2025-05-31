import pandas as pd
import plotly.express as px

# Read the topic model data
data = pd.read_csv("data/topic-model.csv")

# Show sample rows to check structure
print(data.head())

# Exclude rows with undefined topics
data = data[data["Topic"] != -1]

# Combine multiple topic labels into one
data["Label"] = data[["topic_1", "topic_2", "topic_3", "topic_4"]].agg(", ".join, axis=1)

# Count articles by topic label and year
counts = data.groupby(["Label", "year"]).size().reset_index(name="Articles")

# Keep only the top 5 most frequent topics
top_labels = counts.groupby("Label")["Articles"].sum().nlargest(5).index
counts = counts[counts["Label"].isin(top_labels)]

# Create a bar chart with separate bars for each year
fig = px.bar(counts,
             x="year",
             y="Articles",
             color="Label",
             barmode="group",
             labels={"year": "Year", "Articles": "Number of Articles", "Label": "Topic"},
             title="Most Frequent Topics by Year")

# Show chart in browser
fig.show()

# Save chart as an HTML file
fig.write_html("abdus-salam-topics-bar.html")
