import pandas as pd
import plotly.express as px

# Load your data (adjust filename/path as needed)
df = pd.read_csv('ner_counts.tsv', sep='\t')

# Ensure date-related columns are numeric
df['year'] = pd.to_numeric(df['year'], errors='coerce')
df['month'] = pd.to_numeric(df['month'], errors='coerce')
df['word_count'] = pd.to_numeric(df['word_count'], errors='coerce')

# ==============================
# 1. Histogram of articles < 300 words, colored by year
# ==============================

df_short = df[df['word_count'] < 300]

fig1 = px.histogram(df_short, x='word_count', color='year', nbins=30,
                    title='Articles Shorter than 300 Words by Year',
                    labels={'word_count': 'Article Word Count', 'year': 'Publication Year'})

fig1.write_html('outputs/Atiya-Kiyani-short-articles-by-year.html')

# ==============================
# 2. Histogram of 2023 and 2024 articles, colored by year
# ==============================

df_2023_2024 = df[df['year'].isin([2023, 2024])]

fig2 = px.histogram(df_2023_2024, x='word_count', color='year', nbins=30,
                    title='Article Lengths in 2023 and 2024',
                    labels={'word_count': 'Article Word Count', 'year': 'Year'})

# Add annotation
fig2.add_annotation(text="Notice spike near 250 words",
                    x=250, y=10, arrowhead=1, showarrow=True)

fig2.write_html('outputs/Atiya-Kiyani-articles-2023-2024.html')

# ==============================
# 3. Histogram of Oct-Dec 2023 articles, colored by month
# ==============================

df_oct_dec = df[(df['year'] == 2023) & (df['month'].isin([10, 11, 12]))]

fig3 = px.histogram(df_oct_dec, x='word_count', color='month', nbins=30,
                    title='Article Lengths in Oct–Dec 2023 by Month',
                    labels={'word_count': 'Word Count', 'month': 'Month'})

# Add annotation
fig3.add_annotation(text="Lower article counts in November",
                    x=150, y=5, arrowhead=1, showarrow=True)

fig3.write_html('outputs/Atiya-Kiyani-oct-dec-2023.html')
