import pandas as pd
import plotly.express as px

# reads the csv file
df = pd.read_csv("data/title.csv")

# filtering the data for article length shorter than 300
article_length = df[df["length"] < 300]

# plotting the histogram
fig1 = px.histogram(article_length,
    x="length",
    color="year",
    nbins=30,  
    title="Histogram of Article Lengths (Under 300 Words) by Year"
)

# Barspacing
fig1.update_layout(bargap=0.2)

# save to html
fig1.write_html("outputs/yasir-rauf-graph-articles-under-300words.html")

# filtering the years 2023 and 2024
filtered_data = df[df["year"].isin([2023, 2024])]

# plotting the histogram
fig2 = px.histogram(
    filtered_data,
    x="length",
    color="year",
    nbins=30,
    title="Histogram of Article Lengths (2023 & 2024)"
)

# Barspacing
fig2.update_layout(bargap=0.2)

# add annotation for fig2 above the bars in the graph
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

# save to html
fig2.write_html("outputs/yasir-rauf-graph-2023&2024-articleslength-annotation.html")

# filtering the articles from oct, nov, dec of 2023
filtered_articles = df[(df["year"] == 2023) & (df["month"].isin([10, 11, 12]))]

# plotting the histogram
fig3 = px.histogram(
    filtered_articles,
    x="length",
    color="month",
    nbins=30,
    title="Histogram of article length(October-December 2023)"
)

# Barspacing
fig3.update_layout(bargap=0.2)

# Add annotation for fig3 above the bars in the graph
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

# Save to html
fig3.write_html("outputs/yasir-rauf-graph-Oct-Dec-2023-articles-annotation.html")
