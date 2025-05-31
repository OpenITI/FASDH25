import pandas as pd
import plotly.express as px

# Read the CSV file
df = pd.read_csv("data/topic-model.csv")

# Remove rows with Topic = -1
df = df[df["Topic"] != -1]

# Combine topic keywords into a single label
df["Topic_Label"] = df["topic_1"] + ", " + df["topic_2"] + ", " + df["topic_3"] + ", " + df["topic_4"]

# Count articles by year and topic
summary = df.groupby(["year", "Topic_Label"]).size().reset_index(name="Article_Count")

# Get top 5 topics by total article count
top5 = summary.groupby("Topic_Label")["Article_Count"].sum().nlargest(5).index
summary = summary[summary["Topic_Label"].isin(top5)]

# Convert year to string for proper x-axis display
summary["year"] = summary["year"].astype(str)

# Create the bar chart
fig = px.bar(
    summary,
    x="year",
    y="Article_Count",
    color="Topic_Label",
    barmode="group",
    title="Top 5 Topics by Article Count Over the Years",
    labels={"year": "Year", "Article_Count": "Number of Articles", "Topic_Label": "Topic"}
)

# Save the chart as HTML
fig.write_html("kamil-ahmad-topicmodel-bar.html")

# Show the chart
fig.show()
