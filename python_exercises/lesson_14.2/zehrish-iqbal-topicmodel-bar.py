#import libraries
import pandas as pd
import plotly.express as px

#load the csv file
df=pd.read_csv("data/topic-model.csv")

#print the head to understand the structure of the data
print(df.head())

# filter out rows where Topic is -1 
df = df[df["Topic"] != -1]

# Create a single label by joining topic columns with commas
df["Topic_Label"] = df[["topic_1", "topic_2", "topic_3", "topic_4"]].agg(", ".join, axis=1)

# Group the DataFrame by Topic_Label and year, count the number of articles belonging to each topic in each year,
 
grouped = df.groupby(["Topic_Label", "year"]).size().reset_index(name="Article_Count")#reset the index to get a clean DataFrame with a column 'Article_Count'


# Get the top 5 most frequent topics with the highest total article count
top_topics = grouped.groupby("Topic_Label")["Article_Count"].sum().nlargest(5).index

# Filter the grouped DataFrame to include only those top 5 frequent topics
grouped = grouped[grouped["Topic_Label"].isin(top_topics)]

# Create the bar chart
fig = px.bar(grouped,
             x="year",
             y="Article_Count",
             color="Topic_Label",
             barmode="group",
             labels={"year": "Year", "Article_Count": "Number of Articles", "Topic_Label": "Topic"},
             title="Article Counts by Year and Topic")

# Show the bar chart
fig.show()

# write the bar chart as html
fig.write_html("Zehrish_Article_Counts_by_Year_and_Topic.html")

