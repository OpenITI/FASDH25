import pandas as pd
import plotly.express as px

#read the csv
df = pd.read_csv("data/title.csv")

#filter articles shorter than 300 words
short_articles = df[df['length'] < 300]


#plotting the histogram
fig1 = px.histogram(short_articles,
                    x ="length",
                   title = "Artcle length < 300 words by year",
                   color = "year",
                    nbins=30,
                    labels = {"length": "Article length(words)", "year": "Year"}
                    )
#adding more ticks
fig1.update_xaxes(ticks = "inside", tickwidth = 2)
fig1.show()

#save to html
fig1.write_html("outputs/Jafar-uddin-graph-articles-under-300words.html")

#Filter for 2023 and 2024
recent_articles = df[df['year'].isin([2023,2024])]

#plotting
fig2 = px.histogram(
    recent_articles,
    x='length',
    color='year',
    nbins=30,
    title='Article lengths in 2023 and 2024',
    labels={'length': 'Article Length (words)', 'year': 'Year'}
)




#add annotation to the graph
fig2.add_annotation(
    text="Peak between 0-200",
    x=100,
    y=700,
    font=dict(color="blue", size=12, family="Arial"),
    bgcolor="lightgray",
    bordercolor="blue",
    borderwidth=1,
    borderpad=4,
    showarrow=True,
    arrowhead=2
)

#adding more ticks
fig2.update_xaxes(ticks = "inside", tickwidth = 2)
    
# Displaying the graph
fig2.show()

#save to html
fig2.write_html("outputs/Jafar-Uddin-graph-2023&2024-length.html")

#filtering the articles from oct, nov, dec of 2023
filtered_articles = df[(df["year"] == 2023) & (df["month"].isin([10, 11, 12]))]  

#plotting the graph
fig3 = px.histogram(
    filtered_articles,
    x="length",
    color="month",
    nbins=30,
    title="Artcle length from Oct-Dec 2023"
)


#adding more ticks
fig3.update_xaxes(ticks = "inside", tickwidth = 2)

# Adding annotation for an interesting feature
fig3.add_annotation(
    x=250,
    y=70,
    text='Notice the dip',
    showarrow=True,
    arrowhead=2,
    font=dict(color="blue", size=12, family="Arial"),
    bgcolor="lightgray",
    bordercolor="green",
)


# Displaying the figure
fig3.show()

#save to html
fig3.write_html("outputs/Jafar-Uddin-graph-oct-dec.html")

