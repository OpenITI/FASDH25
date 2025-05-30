# import necessary libraries
import pandas as pd
import plotly.express as px

# load the data
df = pd.read_csv("data/topic-model.csv")

#print the first few rows of the dataframe
print(df.head())

#Exclude rows where topic is -1
df = df[df["Topic"] != -1]

# Combine the topic keywords into a single string label for each article
# code adapted with the Help of CHATGPT
df["Topic_Label"] = df[["topic_1", "topic_2", "topic_3", "topic_4"]].apply(lambda row: ", ".join(row), axis=1)

# count how many articles exist for each topic label each year
article_counts = (
    df.groupby(["Topic_Label", "year"])
    .size()
    .reset_index(name="Count")
)

# identify the most 5 frequent topics based on total article count
top_labels = (
    article_counts.groupby("Topic_Label")["Count"]
    .sum()
    .nlargest(5)
    .index
)

# filter data to keep only top topics
filtered_df = article_counts[article_counts["Topic_Label"].isin(top_labels)]

# create a bar chart
bar_chart = px.bar(
    filtered_df,
    x="year",
    y="Count",
    color="Topic_Label",
    title="Top 5 Topics by Year - Article Frequency",
    labels={"year": "Year", "Count": "Number of Articles", "Full_Topic_Label": "Topic"},
    barmode="group"
)

# save the chart as HTML file
bar_chart.write_html("shabir-karim-topicmodel-bar.html")


