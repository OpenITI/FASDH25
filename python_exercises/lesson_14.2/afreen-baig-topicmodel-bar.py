import pandas as pd
import plotly.express as px

# Load the topic model data
df = pd.read_csv("data/topic-model.csv")

# Remove unclassified topics (-1)
df = df[df['Topic'] != -1]

# Create a readable label for topics using the keywords
df['Topic_Label'] = df[['topic_1', 'topic_2', 'topic_3', 'topic_4']].agg(", ".join, axis=1)

# Group by year and topic label
grouped = df.groupby(['year', 'Topic_Label']).size().reset_index(name='Article_Count')

# Get top 5 topics by total article count
top_topics = grouped.groupby('Topic_Label')['Article_Count'].sum().nlargest(5).index

# Keep only top 5 topics
grouped = grouped[grouped['Topic_Label'].isin(top_topics)]

# Convert year to string for categorical axis
grouped['year'] = grouped['year'].astype(str)

# Create bar chart
fig = px.bar(
    grouped,
    x='year',
    y='Article_Count',
    color='Topic_Label',
    barmode='group',
    labels={
        'year': 'Year',
        'Article_Count': 'Number of Articles',
        'Topic_Label': 'Topic Keywords'
    },
    title='Top 5 Topics by Article Count (Based on Keywords)'
)

# Show the chart
fig.show()

# Save to HTML
fig.write_html("afreen-baig-topicmodel-bar.html")
