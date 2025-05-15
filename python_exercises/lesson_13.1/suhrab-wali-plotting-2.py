import pandas as pd
import plotly.express as px
df = pd.read_csv("data/title.csv")

# print the head of the dataframe
print(df.head())


#filtering DataFrame for articles shorter than 300 words
short_articles = df[df["length"] < 300]

#Plot histogram with colors based on the year
fig1 = px.histogram(short_articles, x = "length", color="year",
                   title = "Lengths of articles shorter than 300 words by year",
                   labels= {"length": "Length in tokens", "year": "Publication Year"})

#Add ticks marks to the xaxis
fig1.update_xaxes(ticks= "inside", tickwidth = 2)

fig1.update_yaxes(title_text= "Frequency")

fig1.write_html("outputs/suhrab-wali-short-articles.html")




#Filtering articles from 2023 and 2024 coloured by year
recent_articles =df[df["year"].isin ([2023, 2024])]

fig2 = px.histogram(recent_articles, x="length", color="year",
                    title = "Artilce Lengths in 2023 and 2024",
                    labels = {"length": "Article Length in tokens", "year": "Publication Year"}
)



#Add ticks marks to the xaxis
fig2.update_xaxes(ticks= "inside", tickwidth = 2)

fig2.update_yaxes(title_text= "Frequency")

#Add anotations for 500 tokens
fig2.add_annotation(
    x=500, y=20,
    text = "Spike in articles length around 500 tokens",
    showarrow = True,
    arrowhead =1,
    bgcolor = "white"
)

fig2.write_html("outputs/suhrab-wali-articles-2023-2024.html")


#Filtering articles from October, November and December 2023
final_2023_articles = df[(df["year"] == 2023) & (df["month"].isin([10, 11, 12]))]

fig3 = px.histogram(final_2023_articles, x = "length", color = "month",
                    title = "Article Lengths from Oct to Dec 2023 by Month",
                    labels = {"length": "Article Length in tokens", "month": "Month"}
)

fig3.update_xaxes(ticks="inside", tickwidth=2)
fig3.update_yaxes(title_text="Frequency")


#Adding annotation for special feature
fig3.add_annotation(
    x=200, y=10,
    text = "Short articles in November",
    showarrow=True,
    arrowhead=1,
    bgcolor = "white"
)

fig3.write_html("outputs/suhrab-wali-final_2023_articles.html")
