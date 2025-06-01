#importing libraries
import pandas as pd
import plotly.express as px

# Load the topic model csv
df = pd.read_csv("data/topic-model.csv")

# Remove rows with unclassified topics
df = df[df["Topic"] != -1]

# Creating a readable label for topics using the keywords
df['Topic_Label'] = df[['topic_1', 'topic_2', 'topic_3', 'topic_4']].agg(", ".join, axis=1)

# Keeping rows only with labeled topics
df = df[df["Topic_Label"].notna()]

# count and group by year and topic label
grouped = df.groupby(["year", "Topic_Label"]).size().reset_index(name="Article_Count")

# Identify the top 5 topics by total article count
top_topics = grouped.groupby("Topic_Label")["Article_Count"].sum().nlargest(5).index

# Filter to include only the top 5 topics
grouped = grouped[grouped["Topic_Label"].isin(top_topics)]

# Convert year to string for categorical plotting on x-axis
grouped["year"] = grouped["year"].astype(str)

# Create the grouped bar chart
fig = px.bar(
    grouped,
    x="year",
    y="Article_Count",
    color="Topic_Label",
    barmode="group",
    title="Top 5 Topics by Article Count Over the Years",
    labels={
        "year": "Year",
        "Article_Count": "Number of Articles",
        "Topic_Label": "Topic"
    }
)

# Show the chart
fig.show()

# Save it to HTML
fig.write_html("Aqsa_Anwerali_Top5_Topics_by_Year.html")
