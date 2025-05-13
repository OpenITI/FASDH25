# importing neccessary Libraries

import pandas as pd
import plotly.express as px

# Read the dataset CSV file
df = pd.read_csv("../lesson_13.1/data/title.csv")

# 1. HISTOGRAM: Articles shorter than 300 words, colored by year

# Filter articles with length less than 300
short_articles = df[df["length"] < 300]

# Plot histogram of short articles
fig1 = px.histogram(
    short_articles,
    x="length",
    color="year",
    nbins=30,
    title="Histogram of Article Lengths (< 300 Words) by Year",
    labels={"length": "Article Length (words)", "count": "Number of Articles"}
)

# Set spacing between bars
fig1.update_layout(bargap=0.2)

# Code from CHATGPT for enhancement of the plot
fig1.update_layout(template="plotly_white", font=dict(size=14))
fig1.update_traces(hovertemplate="Length: %{x}<br>Count: %{y}<br>Year: %{customdata[0]}")
fig1.update_layout(title_font=dict(size=20))

# Save to HTML file
fig1.write_html("outputs/Zeeshan-karim-short-articles.html")

# 2. HISTOGRAM: Articles from 2023 and 2024, colored by year

# Filter for articles from 2023 and 2024
filtered_years = df[df["year"].isin([2023, 2024])]

# Plot histogram for 2023 & 2024 articles
fig2 = px.histogram(
    filtered_years,
    x="length",
    color="year",
    nbins=30,
    title="Histogram of Article Lengths (2023 & 2024)",
    labels={"length": "Article Length (words)", "count": "Number of Articles"}
)

# Set spacing between bars
fig2.update_layout(bargap=0.2)

# Add annotation to highlight an interesting pattern
fig2.add_annotation(
    x=100,
    y=30,  # Adjust based on your data
    text="2023 had more short articles than 2024",
    showarrow=False,
    font=dict(color="blue")
)

# Code from CHATGPT for enhancement of the plot
fig2.update_layout(template="plotly_white", font=dict(size=14))
fig2.update_traces(hovertemplate="Length: %{x}<br>Count: %{y}<br>Year: %{customdata[0]}")
fig2.update_layout(title_font=dict(size=20))

# Save to HTML file
fig2.write_html("outputs/Zeeshan-karim-2023-2024-article-length.html")


# 3. HISTOGRAM: Articles from Oct–Dec 2023, colored by month

# Filter for articles from October, November, December 2023
fall_articles = df[(df["year"] == 2023) & (df["month"].isin([10, 11, 12]))]

# Plot histogram by month
fig3 = px.histogram(
    fall_articles,
    x="length",
    color="month",
    nbins=30,
    title="Histogram of Article Lengths (Oct–Dec 2023)",
    labels={"length": "Article Length (words)", "count": "Number of Articles", "month": "Month"}
)

# Set spacing between bars
fig3.update_layout(bargap=0.2)

# Add annotation to highlight a pattern
fig3.add_annotation(
    x=20,
    y=15,  # Adjust based on actual data
    text="December shows a shift toward shorter articles",
    showarrow=False,
    font=dict(color="green")
)
# Code from CHATGPT for enhancement of the plot
fig3.update_layout(template="plotly_white", font=dict(size=14))
fig3.update_layout(title_font=dict(size=20))
fig3.update_traces(hovertemplate="Length: %{x}<br>Count: %{y}<br>Month: %{customdata[0]}")

# Save to HTML file
fig3.write_html("outputs/Zeeshan-karim-oct-nov-dec-2023.html")








