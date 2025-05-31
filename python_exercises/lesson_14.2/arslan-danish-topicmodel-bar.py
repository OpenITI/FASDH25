import pandas as pd
import plotly.express as px

# Load the dataset — should be in the same folder, else update path
data = pd.read_csv("data/topic-model.csv")

# Let's take a quick look at the data to figure out what we're working with
print(data.head())

# Sometimes there's a -1 topic, which usually just means "unassigned" or "junk", so we'll drop those
data = data[data["Topic"] != -1]

# Gonna combine topic columns into a readable label — not perfect, but works
# TODO: Maybe clean up redundant topics later
topic_cols = ["topic_1", "topic_2", "topic_3", "topic_4"]
data["Topic_Label"] = data[topic_cols].agg(lambda x: ", ".join(x.astype(str)), axis=1)

# Let's count how many articles we have per topic per year
# Note: Could've used value_counts here but groupby feels clearer
summary = data.groupby(["Topic_Label", "year"]).size().reset_index(name="Article_Count")

# Figuring out the top 5 most talked-about topics overall (across all years)
top_labels = summary.groupby("Topic_Label")["Article_Count"].sum().sort_values(ascending=False).head(5).index.tolist()

# Only keeping rows related to the top 5 topics for clarity
summary = summary[summary["Topic_Label"].isin(top_labels)]

# Now, making the bar chart — grouped by year and colored by topic
# (Grouped mode stacks them side by side)
fig = px.bar(
    summary,
    x="year",
    y="Article_Count",
    color="Topic_Label",
    barmode="group",
    labels={
        "year": "Year",
        "Article_Count": "Number of Articles",
        "Topic_Label": "Topic"
    },
    title="Article Counts by Year and Topic"
)

# Pop up the plot in a browser tab — works great in Jupyter too
fig.show()

# Save it to file just in case we want to send it or archive the results
fig.write_html("Arsalan_Article_Counts_by_Year_and_Topic.html")
