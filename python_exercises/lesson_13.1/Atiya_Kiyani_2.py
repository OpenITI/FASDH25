# atiya-kiyani-plotting-2.py

import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv("data/title.csv")

# Create a proper date column
df["date"] = df["year"].astype(str) + "-" + df["month"].astype(str).str.zfill(2) + "-" + df["day"].astype(str).str.zfill(2)

# ----------------------------
# 1. Histogram of articles < 300 words, colored by year
short_articles = df[df["length"] < 300]
fig1 = px.histogram(short_articles, x="length", color="year",
                    title="Article Lengths (<300 words) by Year",
                    labels={"length": "Article Length (words)", "year": "Year"})
fig1.write_html("outputs/atiya-kiyani-short-articles.html")

# ----------------------------
# 2. Histogram of articles from 2023 and 2024, colored by year
recent_articles = df[df["year"].isin([2023, 2024])]
fig2 = px.histogram(recent_articles, x="length", color="year",
                    title="Article Lengths in 2023 and 2024",
                    labels={"length": "Article Length (words)", "year": "Year"})

# Add annotation: e.g., a spike at 100 words
fig2.add_annotation(x=100, y=10, text="Spike around 100 words", showarrow=True, arrowhead=1)
fig2.write_html("outputs/atiya-kiyani-2023-2024-hist.html")

# ----------------------------
# 3. Histogram of articles from Oct–Dec 2023, colored by month
late_2023 = df[(df["year"] == 2023) & (df["month"].isin([10, 11, 12]))]
fig3 = px.histogram(late_2023, x="length", color="month",
                    title="Late 2023 Articles by Length",
                    labels={"length": "Article Length (words)", "month": "Month"})

# Add annotation: e.g., cluster around 150–200
fig3.add_annotation(x=175, y=8, text="Many articles around 175 words", showarrow=True, arrowhead=1)
fig3.write_html("outputs/atiya-kiyani-late2023-hist.html")
