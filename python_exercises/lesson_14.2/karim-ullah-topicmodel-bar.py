import pandas as pd
import plotly.express as px  # For creating charts

# Load the data 
df = pd.read_csv("data/topic-model.csv")
print(df.columns)
print(df.head())

# Filter out rows where Topic = -1 (no topic assigned)
df = df[df["Topic"] != -1]

# Create a combined topic label from the 4 topic text columns
df["Topic_Label"] = df[["topic_1", "topic_2", "topic_3", "topic_4"]].agg(", ".join, axis=1)

# Group by Topic_Label and year, count articles
grouped = df.groupby(['Topic_Label', 'year']).size().reset_index(name='Article_Count')

# Find top 5 topics by total article count across all years
top_topics = grouped.groupby('Topic_Label')['Article_Count'].sum().nlargest(5).index.tolist()

# Keep only rows for these top 5 topics
grouped_top5 = grouped[grouped['Topic_Label'].isin(top_topics)]

# Create grouped bar chart for top 5 topics by year
fig = px.bar(grouped_top5, 
             x='year', 
             y='Article_Count', 
             color='Topic_Label', 
             barmode='group',
             title='Top 5 Topics by Year',
             labels={'Topic_Label': 'Topic', 'Article_Count': 'Number of Articles'})

# Save the chart as an HTML file
fig.write_html("karim_ullah_top_5_topic_bar_chart.html")
