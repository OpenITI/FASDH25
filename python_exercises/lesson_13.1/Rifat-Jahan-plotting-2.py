# Importing the necessary libraries
import pandas as pd
import plotly.express as px

# Reading the CSV file
df = pd.read_csv("data/title.csv")
print(df.columns)  
 
#Histogram for articles lengths < 300 words
df_short = df[df["length"] < 300]
fig1 = px.histogram(df_short, x="length", color="year",
                    title="Article Lengths (<300 words) Colored by Year",
                    labels={"length": "Article Length (words)", "year": "Publication Year"},
                    nbins=30)
fig1.write_html("outputs/Rifat-Jahan-hist-short-articles.html")

#Histogram for showing articles from the years 2023 & 2024
df_recent = df[df["year"].isin([2023, 2024])]
fig2 = px.histogram(df_recent, x="length", color="year",
                    title="Article Lengths in 2023 & 2024",
                    labels={"length": "Article Length (words)", "year": "Publication Year"},
                    nbins=30)
#Adding annotations
fig2.add_annotation(
    text="Spike in 2023 short articles",
    x=100, y=30, showarrow=True,
    arrowhead=1
)
fig2.write_html("outputs/Rifat-Jahan-hist-2023-2024.html")

#Histogram for articles from the months of Oct–Dec 2023
df_q4_2023 = df[(df["year"] == 2023) & (df["month"].isin([10, 11, 12]))]
fig3 = px.histogram(df_q4_2023, x="length", color="month",
                    title="Article Lengths for Oct–Dec 2023",
                    labels={"length": "Article Length (words)", "month": "Month"},
                    nbins=30)
#Adding the Annotations
fig3.add_annotation(
    text="Fewer long articles in November",
    x=200, y=10, showarrow=True,
    arrowhead=1
)
fig3.write_html("outputs/Rifat-Jahan-hist-oct-nov-dec-2023.html")


