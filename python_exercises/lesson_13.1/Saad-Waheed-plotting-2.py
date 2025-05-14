import pandas as pd
import plotly.express as px
csv_path = "data/title.csv"
df=pd.read_csv(csv_path)
print(df.head())
print(df.columns)
fig=px.histogram(df, x='length',
                 title="article length",
                 color='year',
                 labels={"length":"length in tokens",
                         'year':'year of publication'})
fig.show()

# histogram: articles < 300 words which are colored by year
short_articles = df[df["length"]<300]
fig1 = px.histogram(short_articles, x="length", color="year",
                    title="Articles Shorter Than 300 Words by Year",
                    labels={"length": "Article Length (words)", "year": "Year"})
fig1.write_html("outputs/Saad-Waheed-short-under300.html")


# histogram: articles from 2023-24colored by year plus annotation

recent_articles = df[df["year"].isin([2023, 2024])]
fig2 = px.histogram(recent_articles,x="length",color="year",
                    title="Article Lengths in 2023 and 2024",
                    labels={"length": "Article Length (words)", "year": "Year"})

# annotate a feature 
fig2.add_annotation(x=1000,
    y=recent_articles[recent_articles["length"] == 1000].shape[0],
    text="Spike around 1000 words",
    showarrow=True,
    arrowhead=1
)
fig2.write_html("outputs/Saad-Waheed-2023-2024-hist.html")


#histogram: articles from oct–dec 2023 colored by month plus annotation

oct_dec_articles = df[(df["year"] == 2023) & (df["month"].isin([10, 11, 12]))]
fig3 = px.histogram(oct_dec_articles, x="length", color="month",
                    title="Article Lengths in Oct–Dec 2023",
                    labels={"length": "Article Length (words)", "month": "Month"})

# annotate a common article length 
mode_len = oct_dec_articles["length"].mode().iloc[0]
fig3.add_annotation(
    x=mode_len,
    y=oct_dec_articles[oct_dec_articles["length"] == mode_len].shape[0],
    text=f"Common length: {mode_len} words",
    showarrow=True,
    arrowhead=2
)
fig3.write_html("outputs/Saad-Waheed-octdec2023.html")


