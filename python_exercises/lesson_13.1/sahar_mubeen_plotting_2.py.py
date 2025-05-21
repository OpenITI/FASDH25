import pandas as pd
import plotly.express as px

# Read the CSV file

df = pd.read_csv("data/title.csv")

# Filter for articles shorter than 300 words
short_articles = df[df['length'] < 300]

# Plot
fig1 = px.histogram(short_articles, x='length', color='year',
                    title='Articles < 300 Words by Year',
                    labels={'length': 'Article Length (words)', 'year': 'Year'})

# Save plot as HTML
fig1.write_html('outputs/sahar-mubeen-length-under-300.html')

# Filter for articles from 2023 and 2024
recent_articles = df[df['year'].isin([2023, 2024])]

# Plot
fig2 = px.histogram(recent_articles, x='length', color='year',
                    title='Article Lengths in 2023 and 2024',
                    labels={'length': 'Article Length (words)', 'year': 'Year'})

# Annotate a feature (e.g., peak)
fig2.add_annotation(x=250, y=20, text="Peak at ~250 words", showarrow=True, arrowhead=1)

# Save as HTML
fig2.write_html('outputs/sahar-mubeen-2023-2024.html')

# Filter for Oct, Nov, Dec 2023
end_of_year_articles = df[(df['year'] == 2023) & (df['month'].isin([10, 11, 12]))]

# Plot
fig3 = px.histogram(end_of_year_articles, x='length', color='month',
                    title='Article Lengths in Oct–Dec 2023',
                    labels={'length': 'Article Length (words)', 'month': 'Month'})

# Annotate a feature (e.g., increase in November)
fig3.add_annotation(x=400, y=10, text="Noticeable spike", showarrow=True, arrowhead=2)

# Save as HTML
fig3.write_html('outputs/sahar-mubeen-oct-dec-2023.html')


