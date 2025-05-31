import pandas as pd
import plotly.express as px

#Read topic model data from the CSV file in the data directory
data = pd.read_csv("data/topic-model.csv")

#Preview the structure of the data
print(data.head())

#Display sample titles to understand how topics were assigned
print(data['title'].head(5))

#Remove entries that were not assigned a valid topic
data = data[data["Topic"] != -1]

#Combine keywords from topic columns to create a descriptive topic label
data["Topic_Name"] = data[["topic_1", "topic_2", "topic_3", "topic_4"]].agg(", ".join, axis=1)

#Count number of articles for each topic per year
counts = data.groupby(["Topic_Name", "year"]).size().reset_index(name="Count")

#Identify the top 5 most frequent topics across all years
top_topics = counts.groupby("Topic_Name")["Count"].sum().nlargest(5).index

#Keep only the top 5 topics in the data for visualization
counts = counts[counts["Topic_Name"].isin(top_topics)]

#Plot a grouped bar chart showing article counts per topic by year
fig = px.bar(
    counts,
    x='year',
    y='Count',
    color='Topic_Name',
    barmode='group',
    title='Distribution of Articles by Topic and Year',
    labels={'Topic_Name': 'Topic', 'Count': 'Article Count', 'year': 'Year'}
)
#export the image 
fig.write_html("topic_bar_chart.html")

