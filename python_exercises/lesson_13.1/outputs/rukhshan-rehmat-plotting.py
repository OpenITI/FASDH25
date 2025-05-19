import pandas as pd
import plotly.express as px

# Load the dataset from the CSV file
df = pd.read_csv("data/title.csv")

# === Histogram 1: Articles shorter than 300 words, coloured by year ===
df_short = df[df['length'] < 300]

fig1 = px.histogram(df_short, x='length', color='year',
                    title='Histogram of Articles Shorter than 300 Words by Year',
                    labels={'length': 'Length in Tokens', 'year': 'Year'})

fig1.update_xaxes(ticks="inside", tickwidth=2, showgrid=True, minor=dict(ticks="inside", ticklen=4))
fig1.update_yaxes(title="Frequency")
fig1.show()
fig1.write_html("outputs/Rukhshan-Rehmat-short-articles.html")

# === Histogram 2: Articles from 2023 and 2024, coloured by year ===
df_23_24 = df[df['year'].isin([2023, 2024])]

fig2 = px.histogram(df_23_24, x='length', color='year',
                    title='Histogram of Article Lengths (2023 & 2024)',
                    labels={'length': 'Length in Tokens', 'year': 'Year'})

# Add annotation (e.g., spike in short articles in 2023)
fig2.add_annotation(text="Spike in short articles",
                    x=100, y=20, arrowhead=1,
                    showarrow=True)

fig2.update_xaxes(ticks="inside", tickwidth=2, showgrid=True, minor=dict(ticks="inside", ticklen=4))
fig2.update_yaxes(title="Frequency")
fig2.show()
fig2.write_html("outputs/Rukhshan-Rehmat-2023-2024.html")

# === Histogram 3: Articles from Oct, Nov, Dec of 2023, coloured by month ===
df_q4_2023 = df[(df['year'] == 2023) & (df['month'].isin([10, 11, 12]))]

fig3 = px.histogram(df_q4_2023, x='length', color='month',
                    title='Histogram of Article Lengths in Oct–Dec 2023',
                    labels={'length': 'Length in Tokens', 'month': 'Month'})

# Add annotation (e.g., high count of mid-length articles)
fig3.add_annotation(text="Cluster of ~200-word articles",
                    x=200, y=15, arrowhead=1,
                    showarrow=True)

fig3.update_xaxes(ticks="inside", tickwidth=2, showgrid=True, minor=dict(ticks="inside", ticklen=4))
fig3.update_yaxes(title="Frequency")
fig3.show()
fig3.write_html("outputs/Rukhshan-Rehmat-oct-nov-dec-2023.html")

