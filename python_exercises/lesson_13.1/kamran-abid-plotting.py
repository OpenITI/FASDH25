import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv("data/title.csv")

# 1. Histogram: Articles < 300 words, colored by year
short_articles = df[df["length"] < 300]
fig1 = px.histogram(
    short_articles,
    x="length",
    color="year",
    nbins=30,
    title="Distribution of Article Lengths (Less than 300 Words)",
    labels={"length": "Article Length (words)", "year": "Publication Year"}
)
fig1.update_layout(bargap=0.2)
fig1.write_html("outputs/kamran-abid-short-articles.html")

# 2. Histogram: Articles from 2023 and 2024, colored by year
recent_articles = df[df["year"].isin([2023, 2024])]
fig2 = px.histogram(
    recent_articles,
    x="length",
    color="year",
    nbins=40,
    title="Article Lengths in 2023 and 2024",
    labels={"length": "Article Length (words)", "year": "Year"}
)

# Add annotation for the most common article length
common_length = recent_articles["length"].mode()[0]
fig2.add_annotation(
    x=common_length,
    y=0,
    text=f"Most common length: {common_length} words",
    showarrow=True,
    arrowhead=1,
    yshift=50
)

fig2.update_layout(bargap=0.2)
fig2.write_html("outputs/kamran-abid-2023-2024.html")

# 3. Histogram: Articles from Oct–Dec 2023, colored by month
oct_dec_articles = df[(df["year"] == 2023) & (df["month"].isin([10, 11, 12]))]
fig3 = px.histogram(
    oct_dec_articles,
    x="length",
    color=oct_dec_articles["month"].astype(str),  # Convert month to string for proper color distinction
    nbins=30,
    title="Article Lengths (Oct–Dec 2023)",
    labels={"length": "Article Length (words)", "color": "Month"}
)

# Add annotation for the longest article in this period
max_len_row = oct_dec_articles[oct_dec_articles["length"] == oct_dec_articles["length"].max()]
fig3.add_annotation(
    x=max_len_row["length"].values[0],
    y=0,
    text="Longest article in Oct–Dec",
    showarrow=True,
    arrowhead=2,
    yshift=40
)

fig3.update_layout(bargap=0.2)
fig3.write_html("outputs/kamran-abid-oct-nov-dec-2023.html")

print("All plots generated and saved in the 'outputs' folder.")
