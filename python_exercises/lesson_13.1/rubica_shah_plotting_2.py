import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv("data/title.csv")

# Ensure correct data types
df['year'] = df['year'].astype(int) #learn from chatgpt
df['month'] = df['month'].astype(int) #learn from chatgpt

# Articles shorter than 300 tokens
df_short = df[df['length'] < 300]

fig1 = px.histogram(df_short, x='length', color='year',  #coloured by year
                    title='Distribution of Short Articles (<300 Tokens) by Year',
                    labels={'length': 'Article Length (in Tokens)', 'year': 'Publication Year'},
                    nbins=30)

fig1.update_xaxes(ticks="inside", tickwidth=2, showgrid=True, minor=dict(ticks="inside", ticklen=4))
fig1.update_yaxes(title="Number of Articles")
fig1.write_html("outputs/rubica-shah-short-articles.html")
fig1.show()  # Histogram 1

# Articles from 2023 and 2024
df_23_24 = df[df['year'].isin([2023, 2024])]

fig2 = px.histogram(df_23_24, x='length', color='year',      #coloured by year
                    title='Article Length Distribution in 2023 and 2024',
                    labels={'length': 'Article Length (in Tokens)', 'year': 'Publication Year'},
                    nbins=30)

fig2.add_annotation(text="Spike in shorter articles (2023)",
                    x=100, y=20, arrowhead=1,
                    showarrow=True)

fig2.update_xaxes(ticks="inside", tickwidth=2, showgrid=True, minor=dict(ticks="inside", ticklen=4))
fig2.update_yaxes(title="Number of Articles")
fig2.write_html("outputs/rubica-shah-2023-2024.html")
fig2.show() # Histogram 2

# Articles from Oct–Dec 2023
df_q4_2023 = df[(df['year'] == 2023) & (df['month'].isin([10, 11, 12]))]
month_map = {10: 'October', 11: 'November', 12: 'December'}
df_q4_2023['month_name'] = df_q4_2023['month'].map(month_map)

fig3 = px.histogram(df_q4_2023, x='length', color='month_name', #coloured by month
                    title='Article Lengths in Q4 2023 (Oct–Dec)',
                    labels={'length': 'Article Length (in Tokens)', 'month_name': 'Month'},
                    nbins=30)

fig3.add_annotation(text="Cluster of ~200-token articles",
                    x=200, y=15, arrowhead=1,
                    showarrow=True)

fig3.update_xaxes(ticks="inside", tickwidth=2, showgrid=True, minor=dict(ticks="inside", ticklen=4))
fig3.update_yaxes(title="Number of Articles")
fig3.write_html("outputs/rubica-shah-q4-2023.html")
fig3.show() # Histogram 3
