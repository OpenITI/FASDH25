# import the libraries we'll need
import pandas as pd
import plotly.express as px

# load our topic model data from a CSV file
df = pd.read_csv("data/topic-model.csv")

# take a quick look at the first few rows to see what the data looks like
print(df.head())

# remove any rows where the topic was marked as -1 (likely unclassified or irrelevant)
df = df[df["Topic"] != -1]

# combine the four topic keywords into a single string for each article
# this makes it easier to track topics together in visualizations
df["Topic_Label"] = df[["topic_1", "topic_2", "topic_3", "topic_4"]].apply(lambda row: ", ".join(row), axis=1)

# count how many articles are associated with each topic label for every year
article_counts = (
    df.groupby(["Topic_Label", "year"])
    .size()
    .reset_index(name="Count")
)

# find the 5 topic labels that appear most frequently across all years combined
top_labels = (
    article_counts.groupby("Topic_Label")["Count"]
    .sum()
    .nlargest(5)
    .index
)

# keep only the data for those top 5 topics so the chart stays clear and focused
filtered_df = article_counts[article_counts["Topic_Label"].isin(top_labels)]

# build a grouped bar chart to show how many articles were written on each top topic every year
bar_chart = px.bar(
    filtered_df,
    x="year",
    y="Count",
    color="Topic_Label",
    title="Top 5 Topics by Year - Article Frequency",
    labels={"year": "Year", "Count": "Number of Articles", "Full_Topic_Label": "Topic"},
    barmode="group"
)

# export the chart to an HTML file so it can be viewed in a browser
bar_chart.write_html("Zeeshan-karim-topicmodel-bar.html")
