import plotly.express as px 
import pandas as pd
csv_path = "data/title.csv"

df = pd.read_csv(csv_path)
print(df.head())
# Filter articles that are shorter than 300 words
df_short_articles = df[df["length"] < 300]

# Create a histogram of article lengths, colored by year
fig1 = px.histogram(df_short_articles, x="length", color="year", 
                     title="Histogram of Article Lengths (Articles < 300 words)", 
                     labels={"length": "Article Length (words)", "year": "Year"})

# Show the plot
fig1.show()

# Export the plot to an HTML file
fig1.write_html("outputs/syed-azhar-uddin-short-articles.html")
# Filter articles from the years 2023 and 2024
df_2023_2024 = df[df["year"].isin([2023, 2024])]

# Create a histogram of article lengths, colored by year
fig2 = px.histogram(df_2023_2024, x="length", color="year", 
                     title="Histogram of Article Lengths (2023 & 2024)", 
                     labels={"length": "Article Length (words)", "year": "Year"})

# Add annotation to highlight an interesting feature
fig2.add_annotation(
    x=350,  # x position on the graph
    y=25,   # y position (frequency) on the graph
    text="Interesting feature",  # Annotation text
    showarrow=True,  # Draw an arrow to the point
    arrowhead=2,  # Arrow style
    ax=0,  # X position of the arrow’s tail
    ay=-40,  # Y position of the arrow’s tail
    font=dict(size=12, color="red")
)

# Show the plot
fig2.show()

# Export the plot to an HTML file
fig2.write_html("outputs/syed-azhar-uddin-2023-2024-articles.html")
# Filter articles from October, November, and December of 2023
df_q4_2023 = df[(df["year"] == 2023) & (df["month"].isin([10, 11, 12]))]

# Create a histogram of article lengths, colored by month
fig3 = px.histogram(df_q4_2023, x="length", color="month", 
                     title="Histogram of Article Lengths (Q4 2023)", 
                     labels={"length": "Article Length (words)", "month": "Month"})

# Add annotation to highlight an interesting feature
fig3.add_annotation(
    x=400,  # x position on the graph
    y=15,   # y position (frequency) on the graph
    text="Interesting feature",  # Annotation text
    showarrow=True,  # Draw an arrow to the point
    arrowhead=2,  # Arrow style
    ax=0,  # X position of the arrow’s tail
    ay=-40,  # Y position of the arrow’s tail
    font=dict(size=12, color="blue")
)

# Show the plot
fig3.show()

# Export the plot to an HTML file
fig3.write_html("outputs/syed-azhar-uddin-q4-2023-articles.html")



