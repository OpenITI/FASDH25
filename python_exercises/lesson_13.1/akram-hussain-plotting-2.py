import pandas as pd
import plotly.express as px

# Step 1: Load the dataset
data_path = "data/title.csv"
df = pd.read_csv(data_path)

# -----------------------------------------
# Plot 1: Articles shorter than 300 words
# -----------------------------------------
# We are looking for articles that are shorter than 300 words.
short_articles = df[df['length'] < 300]

# Now, we create a histogram showing the length of these articles,
# and we will color them according to their publication year.
fig1 = px.histogram(short_articles, x='length', color='year',
                    title='Article Lengths (<300 words) by Year',
                    labels={'length': 'Article Length (Words)', 'year': 'Year'})


# Saving the plot to an HTML file in the outputs folder
fig1.write_html("outputs/akram-hussain-articles-under-300.html")
fig1.show()

# -----------------------------------------
# Plot 2: Articles from 2023 and 2024
# -----------------------------------------
# We are selecting only the articles from the years 2023 and 2024 for this plot.
articles_2023_2024 = df[(df['year'] == 2023) | (df['year'] == 2024)]

# We will create a histogram for these articles, with colors representing the different years.
fig2 = px.histogram(articles_2023_2024, x='length', color='year',
                    title='Article Lengths in 2023 and 2024',
                    labels={'length': 'Article Length (Words)', 'year': 'Year'})

# Adding a simple annotation to highlight an interesting point in the graph
fig2.add_annotation(x=150, y=60, text='Peak around 150 words', showarrow=True)

# Saving the plot to an HTML file in the outputs folder
fig2.write_html("outputs/akram-hussain-2023-2024.html")
fig2.show()

# -----------------------------------------
# Plot 3: Articles from Oct, Nov, Dec 2023
# -----------------------------------------
# Now, we are interested in articles from October, November, and December of 2023.
# Filtering the dataset to get only those articles.
end_of_year_articles = df[(df['year'] == 2023) & (df['month'].isin([10, 11, 12]))]

# Creating a histogram for these articles, with colors representing the month of publication.
fig3 = px.histogram(end_of_year_articles, x='length', color='month',
                    title='Article Lengths in Oct, Nov, Dec 2023',
                    labels={'length': 'Article Length (Words)', 'month': 'Month'})

# Adding an annotation to highlight an interesting feature (spike in December)
fig3.add_annotation(x=180, y=30, text='Spike in December', showarrow=True)

# Saving the plot to an HTML file in the outputs folder
fig3.write_html("outputs/akram-hussain-oct-nov-dec-2023.html")
fig3.show()
