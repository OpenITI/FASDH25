import pandas as pd
import plotly.express as px

# Read the CSV file
df = pd.read_csv("data/title.csv")

# 1. Histogram: Articles < 300 words by year

# Filter articles shorter than 300 words
short_articles = df[df['length'] < 300]

# Create histogram of short article lengths, colored by year
fig1 = px.histogram(
    short_articles,  
    x="length",
    color="year",
    nbins=30,
    title="Distribution of Article Lengths Under 300 Words by Year"
    
)

# Bar spacing
fig1.update_layout(bargap=0.2)
 
# Save the plot to HTML
fig1.write_html("outputs/Mahpara-Karim-short-articles.html")


# 2. Histogram: Articles in 2023 and 2024


# Filter articles from years 2023 and 2024
recent_articles = df[df["year"].isin([2023, 2024])]

# Create histogram of lengths, colored by year
fig2 = px.histogram(
    recent_articles,
    x="length",
    color="year",
    nbins=30,
    title="Article Lengths in 2023 and 2024"
)

# Bar spacing
fig2.update_layout(bargap=0.2)

# Add annotation to highlight a peak
fig2.add_annotation(
    x=100, 
    y=50,   
    ax=100,  
    ay=30,   
    text="2023 has more concise articles than 2024",
    showarrow=True,
    arrowhead=2,
    arrowcolor="blue",
    font=dict(color="blue", size=12, family="Arial"),
    bgcolor="lightgray",
    bordercolor="blue",
    borderwidth=1,
    borderpad=4
)


# Save the plot to HTML
fig2.write_html("outputs/Mahpara-Karim-2023-2024.html")


# 3. Histogram: Oct–Dec 2023 articles by month


# Filter articles from October to December 2023
filtered_articles = df[(df['year'] == 2023) & (df['month'].isin([10, 11, 12]))]

# Create histogram of article lengths, colored by month
fig3 = px.histogram(
    filtered_articles,
    x="length",
    color="month",
    nbins=30,
    title="Article Lengths in Oct-Dec 2023 by Month"
)

# Barspacing
fig1.update_layout(bargap=0.2)

# Add annotation to highlight spike in October
fig3.add_annotation(
    x=50,  
    y=210,  
    ax=50,  
    ay=50,  
    text="Shift lesser shorter articles in December 2023",
    showarrow=True,
    arrowhead=2,
    arrowcolor="green",
    font=dict(color="green", size=12, family="Arial"),
    bgcolor="lightgray",
    bordercolor="green",
    borderwidth=1,
    borderpad=4
)


# Save the plot to HTML
fig3.write_html("outputs/Mahpara-Karim-late2023.html")
