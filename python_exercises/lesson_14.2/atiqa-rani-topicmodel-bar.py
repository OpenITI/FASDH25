
# importing necessary libraries

import pandas as pd
import plotly.express as px

# loading the topic modeling csv file

df=pd.read_csv("data/topic-model.csv")

# printing the first top rows to understand the structure

print(df.head())

# Exclude rows where Topic is -1 (unclassified or irrelevant)

df = df[df["Topic"] != -1]

# Combine the individual topic descriptors into a single string label

df["Topic_Label"] = df[["topic_1", "topic_2", "topic_3", "topic_4"]].agg(", ".join, axis=1)

# Group the Dataset by Topic_Label and year, count the number of articles in each group,
# and reset the index to get a clean DataFrame with a column 'Article_Count'

grouped = df.groupby(["Topic_Label", "year"]).size().reset_index(name="Article_Count")


# Identify the top 5 topics frequent topic labels by total article mentions.

top_topics = grouped.groupby("Topic_Label")["Article_Count"].sum().nlargest(5).index

# Filter the grouped DataFrame to include only those top 5 topics

grouped = grouped[grouped["Topic_Label"].isin(top_topics)]

# Generate the bar chart

fig = px.bar(grouped,
             x="year",
             y="Article_Count",
             color="Topic_Label",
             barmode="group",
             labels={"year": "Year", "Article_Count": "Number of Articles", "Topic_Label": "Topic"},
             title="Article Counts by Year and Topic")

# Display the bar chart




fig.show()

# Export the bar chart as HTML file

fig.write_html("Atiqa_Article_Counts_by_Year_and_Topic.html")



