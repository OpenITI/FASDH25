import pandas as pd
import plotly.express as px

# reading the dataset from the csv file
df = pd.read_csv("data/title.csv")

# Plot 1:showing only articles with less than 300 words, colored by the year they were published
short_articles = df[df["length"] < 300]
fig1 = px.histogram(
    short_articles,
    x="length",
    color="year",
    nbins=30,
    title="Article Lengths Under 300 Words, Grouped by Year",
    labels={"length": "Article Length", "count": "Number of Articles"}
)
fig1.show()

# Optional:save the first plot as an html file
fig1.write_html("outputs/ali_zain-short-articles.html")

# Plot 2:focusing just on articles from the years 2023 and 2024
recent_articles = df[df["year"].isin([2023, 2024])]
fig2 = px.histogram(
    recent_articles,
    x="length",
    color="year",
    nbins=30,
    title="Article Lengths in 2023 and 2024",
    labels={"length": "Article Length", "count": "Number of Articles"}
)

# Adding a little note to highlight a noticeable pattern in the data
fig2.add_annotation(
    text="Spike in short articles",
    x=100, y=20,
    arrowhead=1,
    showarrow=True,
    bgcolor="lightyellow"
)
fig2.show()

# Optional:save the second plot as well
fig2.write_html("outputs/ali_zain-2023-2024-article-lengths.html")

# Plot 3:filtering only articles from October, November, and december of 2023
late_2023 = df[(df["year"] == 2023) & (df["month"].isin([10, 11, 12]))]
fig3 = px.histogram(
    late_2023,
    x="length",
    color="month",
    nbins=30,
    title="Article Lengths for Oct, Nov, and Dec 2023 (Grouped by Month)",
    labels={"length": "Article Length", "count": "Number of Articles"}
)

# pointing out something interesting in the data such as more longer articles in november
fig3.add_annotation(
    text="More long articles in November",
    x=250, y=10,
    arrowhead=1,
    showarrow=True,
    bgcolor="lightgreen"
)
fig3.show()

# Optional:save the third plot
fig3.write_html("outputs/ali_zain-oct-dec-2023-articles.html")
