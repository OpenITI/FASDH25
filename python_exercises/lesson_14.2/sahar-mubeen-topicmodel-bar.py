import pandas as pd
import plotly.express as px

# Load the CSV
df = pd.read_csv("C:/Users/840 G3/Downloads/FASDH25/python_exercises/lesson_14.2/data/topic-model.csv")

# Remove unclassified articles (Topic = -1)
df = df[df["Topic"] != -1]

# combine multiple topics into one
df["Topic_Label"] = df[["topic_1", "topic_2", "topic_3", "topic_4"]].agg(", ".join, axis=1)

# Group data by year and topic label
grouped = df.groupby(["year", "Topic_Label"]).size().reset_index(name="Article_Count")

# Find the top 5 topics overall
top_5_topics = grouped.groupby("Topic_Label")["Article_Count"].sum().nlargest(5).index

# Filter data to include only the top 5 topics
grouped = grouped[grouped["Topic_Label"].isin(top_5_topics)]

# Make sure 'year' is a string for clear x-axis labels
grouped["year"] = grouped["year"].astype(str)

# Create bar chart using Plotly
fig = px.bar(
    grouped,
    x="year",
    y="Article_Count",
    color="Topic_Label",
    barmode="group",
    labels={
        "year": "Year",
        "Article_Count": "Number of Articles",
        "Topic_Label": "Topic"
    },
    title="Top 5 Topics by Article Count Over the Years"
)

# Save chart as an HTML file
fig.write_html("sahar-mubeen-topicmodel-bar.html")

# Show the chart
fig.show()

print("The code is complete here")

