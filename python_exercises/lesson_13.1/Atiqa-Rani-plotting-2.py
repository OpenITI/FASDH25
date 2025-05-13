import pandas as pd
import plotly.express as px

# read the data file
df=pd.read_csv("data/title.csv")


short_articles = df[df["length"] < 300]
#plot the histogram
fig1 = px.histogram(
    short_articles,
    x="length",
    color="year",
    nbins=30,
    title="Articles Shorter Than 300 Words by Year",
)
#set bar gap
fig1.update_layout(bargap=0.2)

#save to html
fig1.write_html("outputs/Atiqa-Rani-short-articles.html")

#filter the years 2023 and 2024
recent_years = df[df["year"].isin([2023, 2024])]

#plot the histogram
fig2 = px.histogram(
    recent_years,
    x="length",
    color="year",
    nbins=30,
    title="Article Lengths in 2023 and 2024",
)

# Add annotation at the mean length

fig2.add_annotation(
    x=100,
    y=30,
    text="2023 had more short articles than 2024",
    showarrow=False,
    font=dict(color="blue")
)
 #set bar space
fig2.update_layout(bargap=0.2)

#save as html
fig2.write_html("outputs/Atiqa-Rani-2023-2024.html")

#filter the articles of October, November, and December of 2023
last_quarter = df[
    (df["year"] == 2023) & 
    (df["month"].isin([10, 11, 12]))
]

#plot the histogram
fig3 = px.histogram(
    last_quarter,
    x="length",
    color="month",
    nbins=30,
    title="Articles in October–December 2023 by Length",
)

    
# Add annotation 

fig3.add_annotation(
    x=20,
    y=15,
    text="December shows a shift toward shorter articles",
    showarrow=False,
    font=dict(color="green")
)

#set bargap
fig3.update_layout(bargap=0.2)
#save as htlm
fig3.write_html("outputs/Atiqa-Rani-Q4-2023.html")
