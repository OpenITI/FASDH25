#import necessary libraries
import pandas as pd
import plotly.express as px

# Reads the csv file
df = pd.read_csv("data/title.csv")

#filtering the data for article length shorter than 300
article_length=df[df["length"] <300]

#Histogram of article lengths < 300 words, colored by year
fig1=px.histogram(article_length,
    x="length",
    color="year",
    nbins=30,  # number of bins in the histogram
    title="Histogram of Article Lengths (Under 300 Words) by Year"
)

#Barspacing
fig1.update_layout(bargap=0.2)  # 0 = no gap, 1 = full gap

#Save as html
fig1.write_html("outputs/Bushra-Hoorani-short-articles.html")

#filtering the years 2023 and 2024
filtered_data=df[df["year"].isin([2023,2024])]

#Histogram of articles from 2023 and 2024, colored by year
fig2 = px.histogram(
    filtered_data,
    x="length",
    color="year",
    nbins=30,
    title="Histogram of Article Lengths (2023 & 2024)"
)

# Add annotation
fig2.add_annotation(
    text="Notice spike around 500-word articles",
    x=500,
    y=filtered_data['length'].value_counts().max(),
    arrowhead=2,
    showarrow=True
)

#Bar spacing
fig2.update_layout(bargap=0.2)


#add anoatation
fig2.add_annotation(
    x=100,
    y=30,  # adjust this based on your actual data
    text="2023 had more short articles than 2024",
    showarrow=False,
    font=dict(color="blue")
)

#save as html
fig2.write_html("outputs/Bushra-Hoorani-2023-2024.html")

#fitering the articles from oct,nov,dec of 2023
filtered_articles= df[(df["year"] == 2023) & (df["month"].isin([10, 11, 12]))]


#Histogram for Oct–Dec 2023, colored by month
fig3=px.histogram(
    filtered_articles,
    x="length",
    color="month",
    nbins=30,
    title="Histogram of article length(Oct-Dec 2023)"
)

#Bar Spacing
fig3.update_layout(bargap=0.2)


#add anotation
fig3.add_annotation(
    x=20,
    y=15,
    text="December shows a shift toward shorter articles",
    showarrow=False,
    font=dict(color="green")
) 

#save to html 
fig3.write_html("outputs/Bushra-Hoorani-q4-2023.html")












