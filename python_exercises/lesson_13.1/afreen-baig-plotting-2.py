import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv("data/title.csv")

# First plot: Histogram of articles shorter than 300 words, colored by year
short_articles = df[df["length"] < 300]
fig1 = px.histogram(
    short_articles,
    x="length",
    color="year",
    nbins=30,
    title="Article Lengths < 300 Words, Colored by Year",
    labels={"length": "Article Length", "count": "Number of Articles"}
)
fig1.show()

# Second plot: Articles from 2023 and 2024 only
recent_articles = df[df["year"].isin([2023, 2024])]
fig2 = px.histogram(
    recent_articles,
    x="length",
    color="year",
    nbins=30,
    title="Histogram of Article Lengths (2023–2024)",
    labels={"length": "Article Length", "count": "Number of Articles"}
)
# Add annotation to highlight a visible spike
fig2.add_annotation(
    text="Spike in short articles",
    x=100, y=20,
    arrowhead=1,
    showarrow=True,
    bgcolor="lightyellow"
)
fig2.show()

# Third plot: Articles from Oct–Dec 2023, colored by month
late_2023 = df[(df["year"] == 2023) & (df["month"].isin([10, 11, 12]))]
fig3 = px.histogram(
    late_2023,
    x="length",
    color="month",
    nbins=30,
    title="Article Lengths for Oct–Dec 2023, Colored by Month",
    labels={"length": "Article Length", "count": "Number of Articles"}
)
# Annotate interesting feature
fig3.add_annotation(
    text="More long articles in November",
    x=250, y=10,
    arrowhead=1,
    showarrow=True,
    bgcolor="lightgreen"
)
fig3.show()
