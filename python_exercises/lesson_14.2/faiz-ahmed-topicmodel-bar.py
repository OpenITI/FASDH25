#import libraries
import pandas as pd
import plotly.express as px

#loading CSV
df = pd.read_csv("data/topic-model.csv")

#removing unclassified
df = df[df["Topic"] != -1]

#creating a readable label for topics
df["Topic_Label"] = df[["topic_1", "topic_2", "topic_3", "topic_4"]].agg(", ".join, axis=1)

#grouping by year and topic
grouped = df.groupby(["year", "Topic_Label"]).size().reset_index(name="Article_Count")

#getting top 5 topics by total article count
top_topics = grouped.groupby("Topic_Label")["Article_Count"].sum().nlargest(5).index

#include top 5 topics
grouped = grouped[grouped["Topic_Label"].isin(top_topics)]

#converting year to string 
grouped["year"] = grouped["year"].astype(str)

#plot bar chart
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

#saving to HTML
fig.write_html("Faiz_Top5_Topics_by_Year.html")
