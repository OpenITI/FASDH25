import pandas as pd
import plotly.express as px

# Load the dataset containing article titles and metadata
df = pd.read_csv("data/title.csv")

# Select articles that are under 300 words
short_articles = df[df["length"] < 300]

# Create a histogram to visualize short articles by year
fig1 = px.histogram(
    short_articles,
    x="length",
    color="year",
    nbins=30,
    title="Distribution of Articles Under 300 Words by Year",
)

# Adjust spacing between histogram bars
fig1.update_layout(bargap=0.2)

# Save the interactive visualization to an HTML file
fig1.write_html("outputs/Fatima-Karim-short-articles.html")

# Focus on articles published in the years 2023 and 2024
recent_years = df[df["year"].isin([2023, 2024])]

# Generate a histogram to compare article lengths across 2023 and 2024
fig2 = px.histogram(
    recent_years,
    x="length",
    color="year",
    nbins=30,
    title="Comparison of Article Lengths in 2023 and 2024",
)

# Add an annotation with a different message and styling
fig2.add_annotation(
    x=120,
    y=25,
    text="Noticeable skew toward shorter articles in 2023",
    showarrow=False,
    font=dict(color="darkred", size=12)
)

# Set spacing between bars for clarity
fig2.update_layout(bargap=0.2)

# Save the plot as an HTML file
fig2.write_html("outputs/Fatima-Karim-2023-2024.html")

# Extract articles published in the final quarter of 2023
last_quarter = df[
    (df["year"] == 2023) & 
    (df["month"].isin([10, 11, 12]))
]

# Build a histogram to examine article lengths by month for Oct–Dec 2023
fig3 = px.histogram(
    last_quarter,
    x="length",
    color="month",
    nbins=30,
    title="Length Distribution of Articles in Q4 2023",
)

# Insert a unique annotation with new wording and location
fig3.add_annotation(
    x=40,
    y=10,
    text="Slight dip in article length seen in December",
    showarrow=False,
    font=dict(color="green", size=12)
)

# Apply consistent bar spacing for visual appeal
fig3.update_layout(bargap=0.2)

# Export the visualization as an HTML file
fig3.write_html("outputs/Fatima-Karim-Q4-2023.html")
