# Loading the necessary libraries for visualizations
import pandas as pd
import plotly.express as px

# Setting path to the data
data_path = "data/topic-model.csv"

# Read topic-model.csv as a pandas dataframe
df = pd.read_csv(data_path)

# Printing the head to understand the structure of the data
print(df.head())

# Filter out rows with Topic == -1. Topic -1 typically represents "noise" or unclassified articles.This line of code removes those rows, so only meaningful topics remain.
df = df[df["Topic"] != -1]

# Create a topic label using top keywords. Each topic in our dataframe has keywords like topic_1, topic_2, topic_3, and topic_4. This line of code combines the 4 keywords into a
# readable label for the topic which helps us easily understand what each topic is about instead of just calling it "topic_1", "topic_2".
df["Topic_Label"] = df[["topic_1", "topic_2", "topic_3", "topic_4"]].agg(", ".join, axis=1)

# Groups the data by Topic_Label and year, and counts how many articles belong to each topic in each year.
grouped = df.groupby(["Topic_Label", "year"]).size().reset_index(name="Article_Count")

# It first sums total articles per topic across all years. Then, it selects the 5 most frequent topics (those with the highest total counts).
# Finally, it filters grouped to include only those top 5 topics.
top_topics = grouped.groupby("Topic_Label")["Article_Count"].sum().nlargest(5).index
grouped = grouped[grouped["Topic_Label"].isin(top_topics)]

# Create the bar chart
fig = px.bar(grouped,
             x = "Topic_Label",
             y="Article_Count",
             facet_row="year",
             color="Topic_Label",
             labels={"year": "Year", "Article_Count": "Number of Articles", "Topic_Label": "Topic"},
             title="Article Counts by Year and Topic",
             hover_data={"Topic_Label": False, "year": False})

# Show the bar chart
fig.show()

# Saving bar chart as html
fig.write_html("yasir_Article_Counts_by_Year_and_Topic.html")
