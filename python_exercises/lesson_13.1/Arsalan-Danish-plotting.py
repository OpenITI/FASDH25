# Import necessary libraries
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv("../lesson_13.1/data/title.csv")

### 1. Histogram of Short Articles (<300 words), grouped by Year ###

# Step 1: Filter articles that are less than 300 words
short_articles = df[df["length"] < 300]

# Step 2: Create a histogram showing distribution of short articles, colored by year
fig1 = px.histogram(
    short_articles,
    x="length",
    color="year",
    nbins=30,
    title="Histogram of Article Lengths (< 300 Words) by Year",
    labels={"length": "Article Length (words)", "count": "Number of Articles"}
)

# Step 3: Beautify the plot
fig1.update_layout(
    template="plotly_white",
    font=dict(size=14),
    title_font=dict(size=20),
    bargap=0.2  # Controls space between bars
)

# Custom hover information
fig1.update_traces(
    hovertemplate="Length: %{x}<br>Count: %{y}<br>Year: %{customdata[0]}"
)

# Step 4: Save the plot as an interactive HTML file
fig1.write_html("outputs/Arsalan-Danish-short-articles.html")


### 2. Histogram of Articles from 2023 & 2024 ###

# Step 1: Filter data for the years 2023 and 2024
recent_articles = df[df["year"].isin([2023, 2024])]

# Step 2: Create histogram
fig2 = px.histogram(
    recent_articles,
    x="length",
    color="year",
    nbins=30,
    title="Histogram of Article Lengths (2023 & 2024)",
    labels={"length": "Article Length (words)", "count": "Number of Articles"}
)

# Step 3: Beautify plot and add annotation
fig2.update_layout(
    template="plotly_white",
    font=dict(size=14),
    title_font=dict(size=20),
    bargap=0.2
)

# Annotation to highlight pattern
fig2.add_annotation(
    x=100,  # X-axis (length) position
    y=30,   # Y-axis (count) position — adjust based on your dataset
    text="2023 had more short articles than 2024",
    showarrow=False,
    font=dict(color="blue")
)

# Custom hover details
fig2.update_traces(
    hovertemplate="Length: %{x}<br>Count: %{y}<br>Year: %{customdata[0]}"
)

# Step 4: Save output
fig2.write_html("outputs/Arsalan-Danish-2023-2024-article-length.html")


### 3. Histogram for Articles in Oct–Dec 2023 ###

# Step 1: Filter articles from October, November, and December 2023
fall_articles = df[(df["year"] == 2023) & (df["month"].isin([10, 11, 12]))]

# Step 2: Create histogram by month
fig3 = px.histogram(
    fall_articles,
    x="length",
    color="month",
    nbins=30,
    title="Histogram of Article Lengths (Oct–Dec 2023)",
    labels={
        "length": "Article Length (words)",
        "count": "Number of Articles",
        "month": "Month"
    }
)

# Step 3: Styling and annotation
fig3.update_layout(
    template="plotly_white",
    font=dict(size=14),
    title_font=dict(size=20),
    bargap=0.2
)

# Highlight shorter article trend in December
fig3.add_annotation(
    x=20,
    y=15,  # Adjust to your data
    text="December shows a shift toward shorter articles",
    showarrow=False,
    font=dict(color="green")
)

# Custom hover text
fig3.update_traces(
    hovertemplate="Length: %{x}<br>Count: %{y}<br>Month: %{customdata[0]}"
)

# Step 4: Save to HTML
fig3.write_html("outputs/Arsalan-Danish-oct-nov-dec-2023.html")






