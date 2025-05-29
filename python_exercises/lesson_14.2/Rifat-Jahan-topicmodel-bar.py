#importing the necessary libraries
import pandas as pd
import plotly.express as px

# Loading the csv file
df = pd.read_csv("data/topic-model.csv")

# Removing unclassified
df = df[df["Topic"] != -1]

# Creating a readable label for topics
df["Topic_Label"] = df[["topic_1", "topic_2", "topic_3", "topic_4"]].agg(", ".join, axis=1)

# Groupig by year and topic
grouped = df.groupby(["year", "Topic_Label"]).size().reset_index(name="Article_Count")

# Getting top 5 topics by total article count
top_topics = grouped.groupby("Topic_Label")["Article_Count"].sum().nlargest(5).index

# Filtering to only include top 5 topics
grouped = grouped[grouped["Topic_Label"].isin(top_topics)]

# Converting year to string to keep it categorical on x-axis
grouped["year"] = grouped["year"].astype(str)

# Plot as a bar chart
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

fig.show()

# Save to HTML
fig.write_html("Rifat_Top5_Topics_by_Year.html")
