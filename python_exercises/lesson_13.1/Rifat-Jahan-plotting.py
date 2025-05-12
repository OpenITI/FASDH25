#importing the necessary libraries
import pandas as pd
import plotly.express as px
import os

# Reading the CSV file
df = pd.read_csv('title.csv')
print(df.columns)
# Create output directory if it doesn't exist
os.makedirs("outputs", exist_ok=True)

df_short = df[df["word_count"] < 300]

fig1 = px.histogram(df_short, x="article_length", color="year",
                    title="Article Lengths (<300 words) Colored by Year",
                    labels={"article_length": "Article Length (words)", "year": "Publication Year"},
                    nbins=30)
fig1.write_html("outputs/Rifat-Jahan-hist-short-articles.html")
df_recent = df[df["year"].isin([2023, 2024])]

fig2 = px.histogram(df_recent, x="article_length", color="year",
                    title="Article Lengths in 2023 & 2024",
                    labels={"article_length": "Article Length (words)", "year": "Publication Year"},
                    nbins=30)

# Add annotation: highlight a spike or dip, adjust x/y as needed
fig2.add_annotation(
    text="Spike in 2023 short articles",
    x=100, y=20, showarrow=True,
    arrowhead=1
)
fig2.write_html("outputs/Rifat-Jahan-hist-2023-2024.html")

 # Histogram: Oct-Dec 2023, colored by month
 
df_q4_2023 = df[(df["year"] == 2023) & (df["month"].isin([10, 11, 12]))]

fig3 = px.histogram(df_q4_2023, x="article_length", color="month",
                    title="Article Lengths for Oct–Dec 2023",
                    labels={"article_length": "Article Length (words)", "month": "Month"},
                    nbins=30)

# Add annotation
fig3.add_annotation(
    text="Fewer long articles in November",
    x=200, y=10, showarrow=True,
    arrowhead=1
)
fig3.write_html("outputs/Rifat-Jahan-hist-oct-nov-dec-2023.html")
 # Show the plot
fig.show()
