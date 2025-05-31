import pandas as pd
import plotly.express as px

#load the data containing topoic model
df = pd.read_csv("data/topic-model.csv")

#print  few rows to understand the data
print(df.head())

#print some of the titles from topic to assign labels 
print(df['title'].head(5))

#Filter out rows with Topic = -1 as it has not been assigned any topic 
df = df[df["Topic"] != -1]

#Map the topic numbers to labels using keywords such as topic_1
df["Topic_Label"] = df[["topic_1", "topic_2", "topic_3", "topic_4"]].agg(", ".join, axis=1)

#Group the DataFrame by Topic_Label and year and count the number of articles in each group
# and rename it to get a new DataFramae with a column called "Article Count"
grouped = df.groupby(["Topic_Label", "year"]).size().reset_index(name="Article_Count")

# Take the top five topics with the highest total artcile count
top_five_topics = grouped.groupby("Topic_Label")["Article_Count"].sum().nlargest(5).index

#Filter the DataFrame to get the top five topics
grouped = grouped[grouped["Topic_Label"].isin(top_five_topics)]


#Create the Bar chart 
fig = px.bar(
    grouped,
    x='year',
    y='Article_Count',
    color='Topic_Label',
    barmode='group',
    title='Article Counts by Topic and Year',
    labels={'Topic_Label': 'Topic', 'Article_Count': 'Number of Articles', 'year': 'Year'}
)

fig.show()
