# Importing libraries
import pandas as pd
import plotly.express as px

# Loading the CSV data
df = pd.read_csv("data/topic-model.csv")

# Keeping only classified articles
df = df[df["Topic"] != -1]

# Creating readable topic labels by combining topic_1 to topic_4
df["Topic_Label"] = df[["topic_1", "topic_2", "topic_3", "topic_4"]].agg(", ".join, axis=1)

# Grouping by topic label to get total article counts per topic
topic_counts = df["Topic_Label"].value_counts().nlargest(5).index.tolist()

# Filtering data for top 5 topics only
filtered_df = df[df["Topic_Label"].isin(topic_counts)]

# Grouping by year and topic label to count articles
grouped_data = filtered_df.groupby(["year", "Topic_Label"]).size().reset_index(name="Article_Count")

# Converting year to string for categorical x-axis
grouped_data["year"] = grouped_data["year"].astype(str)

# Creating bar chart
fig = px.bar(
    grouped_data,
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

# Show the plot
fig.show()

# Saving the plot as an HTML file
fig.write_html("akram-top5-topics-by-year.html")
