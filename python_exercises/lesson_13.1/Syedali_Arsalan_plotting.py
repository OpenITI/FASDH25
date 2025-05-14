import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv("data/title.csv")

# --------------------------
# Plot 1: Articles < 300 words by year
# --------------------------
short_articles = df[df["length"] < 300]
fig1 = px.histogram(
    short_articles,
    x="length",
    color="year",
    nbins=30,
    title="Histogram of Article Lengths (< 300 words) by Year",
    labels={"length": "Article Length", "year": "Year"}
)
fig1.write_html("outputs/syedali-arsalan-short-articles.html")

# --------------------------
# Plot 2: Articles from 2023 and 2024
# --------------------------
recent_articles = df[df["year"].isin([2023, 2024])]
fig2 = px.histogram(
    recent_articles,
    x="length",
    color="year",
    nbins=30,
    title="Histogram of Article Lengths (2023 and 2024)",
    labels={"length": "Article Length", "year": "Year"}
)

# Annotation for an interesting feature
max_2023 = recent_articles[recent_articles["year"] == 2023]["length"].max()
fig2.add_annotation(
    x=max_2023,
    y=5,
    text="Longest 2023 article",
    showarrow=True,
    arrowhead=2
)
fig2.write_html("outputs/syedali-arsalan-2023-2024.html")

# --------------------------
# Plot 3: Articles from Oct, Nov, Dec 2023
# --------------------------
last_quarter = df[(df["year"] == 2023) & (df["month"].isin([10, 11, 12]))]
fig3 = px.histogram(
    last_quarter,
    x="length",
    color=last_quarter["month"].astype(str),  # Convert month to string for color
    nbins=30,
    title="Histogram of Article Lengths (Oct-Dec 2023)",
    labels={"length": "Article Length", "month": "Month"}
)

# Add annotation
mean_length = last_quarter["length"].mean()
fig3.add_annotation(
    x=mean_length,
    y=4,
    text="Average Length",
    showarrow=True,
    arrowhead=2
)
fig3.write_html("outputs/syedali-arsalan-q4-2023.html")
