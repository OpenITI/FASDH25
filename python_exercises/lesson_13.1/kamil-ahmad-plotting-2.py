import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv("data/title.csv")

# Graph 1: Articles under 300 words
short_articles = df[df["length"] < 300]

fig1 = px.histogram(
    short_articles,
    x="length",
    color="year",
    nbins=30,
    title="Distribution of Articles Under 300 Words by Year"
)
fig1.update_layout(bargap=0.2)

# Save as HTML
fig1.write_html("outputs/kamil-ahmad-short-articles.html")

# Graph 2: Articles from 2023 and 2024
recent_articles = df[df["year"].isin([2023, 2024])]

fig2 = px.histogram(
    recent_articles,
    x="length",
    color="year",
    nbins=30,
    title="Article Lengths in 2023 and 2024"
)
fig2.update_layout(bargap=0.2)

# Add annotation to fig2
fig2.add_annotation(
    x=150,
    y=50,
    text="More short articles in 2023 compared to 2024",
    showarrow=True,
    arrowhead=2,
    arrowcolor="blue",
    font=dict(color="blue", size=12, family="Arial"),
    bgcolor="lightgray",
    bordercolor="blue",
    borderwidth=1,
    borderpad=4
)

# Save as HTML
fig2.write_html("outputs/kamil-ahmad-2023-2024-articleslength.html")

# Graph 3: Oct–Dec 2023 
late_2023_articles = df[(df["year"] == 2023) & (df["month"].isin([10, 11, 12]))]

fig3 = px.histogram(
    late_2023_articles,
    x="length",
    color="month",
    nbins=30,
    title="Article Lengths (Oct–Dec 2023) by Month"
)
fig3.update_layout(bargap=0.2)

# Add annotation to fig3
fig3.add_annotation(
    x=50,
    y=25,
    text="Fewer short articles published in December",
    showarrow=True,
    arrowhead=2,
    arrowcolor="green",
    font=dict(color="green", size=12, family="Arial"),
    bgcolor="lightgray",
    bordercolor="green",
    borderwidth=1,
    borderpad=4
)

# Save as HTML
fig3.write_html("outputs/kamil-ahmad-late2023-annotation.html")


