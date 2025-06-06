import pandas as pd 
import plotly.express as px

# reading the csv file
df=pd.read_csv("data/title.csv")

# filtering the data for article length shorter than 300
article_length=df[df["length"] <300]

# plotting the histogram
fig1=px.histogram(article_length,
    x="length",
    color="year",
    nbins=30,  # number of bins in the histogram
    title="Histogram of Article Lengths (Under 300 Words) by Year"
)

# Barspacing
fig1.update_layout(bargap=0.2)  # 0 = no gap, 1 = full gap

# saving to html
fig1.write_html("outputs/sara-baig-short-articles.html")

# filtering the years 2023 and 2024
filtered_data=df[df["year"].isin([2023,2024])]

# plotting the histogram
fig2 = px.histogram(
    filtered_data,
    x="length",
    color="year",
    nbins=30,
    title="Histogram of Article Lengths (2023 & 2024)"
)


fig2.update_layout(bargap=0.2)

       
# adding annotation
fig2.add_annotation(
    x=100,
    y=30,  # adjusting this based on your actual data
    text="2023 had more short articles than 2024",
    showarrow=False,
    font=dict(color="blue")
)

# saving to html
fig2.write_html("outputs/sara-baig-2023&2-2024-article-length.html")

# fitering the articles from Oct, Nov, Dec of 2023
filtered_articles= df[(df["year"] == 2023) & (df["month"].isin([10, 11, 12]))]

# plotting the histogram
fig3=px.histogram(
    filtered_articles,
    x="length",
    color="month",
    nbins=30,
    title="Histogram of article length(Oct-Dec 2023)"
)

fig3.update_layout(bargap=0.2)

# adding annotation
fig3.add_annotation(
    x=20,
    y=15,
    text="December shows a shift toward shorter articles",
    showarrow=False,
    font=dict(color="green")
)

# saving to html
fig3.write_html("outputs/sara-baig-(0ct-Dec, 2023)-articles.html")
