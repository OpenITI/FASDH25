import pandas as pd
import plotly.express as px

#file path
csv_path = r"data\title.csv"

#defining df
df = pd.read_csv(csv_path)

#printing the first few lines to check if df is loaded.
print(df.head())


#plotting histogram
fig = px.histogram(df, x ="length",
                   title = "Article in the Gaza Corpus",
                   color = "year",
                    labels = {"length": "Length in tokens"})
#adding ticks
fig.update_xaxes(ticks = "inside", tickwidth = 2)

#Changing the label of y axis to frequency
fig.update_yaxes(title_text = "Frequency")

#show the figures
fig.show()

# Filtering the DataFrame for articles shorter than 300 words
df_filtered_short = df[df['length'] < 300]

# Creating the Histogram for articles shorter than 300 words
fig = px.histogram(
    df_filtered_short, 
    x='length', 
    color='year', 
    title='Distribution of Article Lengths (Under 300 Words)',
    labels={'length': 'Article Length (in Tokens)', 'year': 'Publication Year'},
    nbins=20
)

# Adding ticks and improving axis labels
fig.update_xaxes(ticks='inside', tickwidth=2)
fig.update_yaxes(title_text='Frequency')

# Displaying the figure
fig.show()

# Filtering the DataFrame for articles from 2023 and 2024
df_filtered_2023_2024 = df[(df['year'] == 2023) | (df['year'] == 2024)]

# Creating the Histogram for articles from 2023 and 2024
fig = px.histogram(
    df_filtered_2023_2024, 
    x='length', 
    color='year', 
    title='Distribution of Article Lengths (2023 and 2024)',
    labels={'length': 'Article Length (in Tokens)', 'year': 'Publication Year'},
    nbins=20
)

# Adding annotation for an interesting feature
fig.add_annotation(
    x=200, y=300,
    text='Notice the dip in 2023 and 2024!',
    showarrow=True,
    arrowhead=2
)

# Adding ticks and improving axis labels
fig.update_xaxes(ticks='inside', tickwidth=2)
fig.update_yaxes(title_text='Frequency')

# Displaying the figure
fig.show()

# Filtering the DataFrame for articles from October, November, and December 2023
df_filtered_oct_dec_2023 = df[(df['year'] == 2023) & (df['month'].isin([10, 11, 12]))]

# Creating the Histogram for articles from Oct, Nov, Dec 2023
fig = px.histogram(
    df_filtered_oct_dec_2023, 
    x='length', 
    color='month', 
    title='Distribution of Article Lengths (Oct-Dec 2023)',
    labels={'length': 'Article Length (in Tokens)', 'month': 'Publication Month'},
    nbins=20
)

# Adding annotation for an interesting feature
fig.add_annotation(
    x=500, y=330,  # Adjust these values based on your data range
    text='gradual decline afterwards!',
    showarrow=True,
    arrowhead=2
)

# Adding ticks and improving axis labels
fig.update_xaxes(ticks='inside', tickwidth=2)
fig.update_yaxes(title_text='Frequency')

# Displaying the figure
fig.show()

