# importing the necessary libraries 
import pandas as pd
import plotly.express as px

# Load your data 
csv_path = "C:/Users/hp/Downloads/FASDH25/python_exercises/lesson_13.1/data/title.csv"
df = pd.read_csv(csv_path)

# filter the articles shorter than 300 words 
short_articles = df[df['length'] < 300]

# creating histogram of these short articles, colored by year 
fig1 = px.histogram(short_articles, x='length', color='year',
                    title='Articles < 300 Words by Year')
                    
# label x-axes and y-axes
fig1.update_layout(xaxis_title='Length (words)', yaxis_title='Number of Articles')


# save the plot as an HTML file 
fig1.write_html("outputs/ulya-batool-short-articles.html")

# filter articles from year 2023 and 2024
recent = df[df['year'].isin([2023, 2024])]

# create histogram
fig2 = px.histogram(recent, x='length', color='year',
                    title='Articles from 2023 and 2024')
# updating axis labels
fig2.update_layout(xaxis_title='Length (words)', yaxis_title='Number of Articles')

# adding annotations to highlight a feature in the graph
fig2.add_annotation(text="Look: peak in 2023 around 500 words",
                    x=500, y=20, arrowhead=2)
# save the figure as HTM
fig2.write_html("outputs/ulya-batool-2023-2024.html")

# filter the articles from Oct, Nov, and Dec 2023 
end_2023 = df[(df['year'] == 2023) & (df['month'].isin([10, 11, 12]))]

# create histgram
fig3 = px.histogram(end_2023, x='length', color='month',
                    title='Articles from Oct-Dec 2023')
# label axes
fig3.update_layout(xaxis_title='Length (words)', yaxis_title='Number of Articles')

# add annotation
fig3.add_annotation(text="Spike in December",
                    x=450, y=15, arrowhead=1)

# save to HTML
fig3.write_html("outputs/ulya-batool-end2023.html")
    
