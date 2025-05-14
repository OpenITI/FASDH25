import pandas as pd
import plotly.express as px

# Load the data
df = pd.read_csv("data/title.csv")

# Combine year, month, and day to allow filtering by date
df['date'] = pd.to_datetime(df[['year', 'month', 'day']])

# 1. Histogram of articles < 300 words, colored by year
short_articles = df[df['length'] < 300]
fig1 = px.histogram(
    short_articles,
    x='length',
    color='year',
    title='Histogram of Article Lengths < 300 Words by Year',
    labels={'length': 'Article Length', 'year': 'Year'}
)
fig1.write_html("outputs/safwan-yaftali-short-articles-by-year.html")

# 2. Histogram of 2023 and 2024 articles, colored by year
recent_articles = df[df['year'].isin([2023, 2024])]
fig2 = px.histogram(
    recent_articles,
    x='length',
    color='year',
    title='Article Lengths in 2023 and 2024',
    labels={'length': 'Article Length', 'year': 'Year'}
)

# Add annotation (example: peak at 300 words)
fig2.add_annotation(
    text="Noticeable spike near 300 words",
    x=300,
    y=recent_articles['length'].value_counts().max() / 2,
    showarrow=True,
    arrowhead=2
)
fig2.write_html("outputs/safwan-yaftali-2023-2024-lengths.html")

# 3. Histogram of 2023 articles in Oct–Dec, colored by month
end_2023 = df[(df['year'] == 2023) & (df['month'].isin([10, 11, 12]))]
fig3 = px.histogram(
    end_2023,
    x='length',
    color='month',
    title='Article Lengths in Oct–Dec 2023 by Month',
    labels={'length': 'Article Length', 'month': 'Month'}
)

# Add annotation (example: cluster around 250 words)
fig3.add_annotation(
    text="Cluster near 250 words in late 2023",
    x=250,
    y=end_2023['length'].value_counts().max() / 2,
    showarrow=True,
    arrowhead=2
)
fig3.write_html("outputs/safwan-yaftali-Q4-2023-lengths.html")
