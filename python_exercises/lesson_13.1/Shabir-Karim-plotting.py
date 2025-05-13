# import necessary libraries

import plotly.express as px
import pandas as pd

# load csv file as a df
df = pd.read_csv("../lesson_13.1/data/title.csv")

# print head of a data frame
print(df.head())

# Step 1: Create the histogram
fig = px.histogram(
    df,
    x='length',  # column to use for histogram
    title='Distribution of Article Lengths in Gaza Corpus',
    color = 'year',
    labels={'length': 'Article Length'}  # set custom x-axis label
)

# Step 2: Add tick marks to the x-axis (optional - customize as needed)
fig.update_xaxes(
    tickmode='linear',  # show ticks at regular intervals
    tick0=0,             # where to start
    dtick=200           # distance between ticks
)

# Step 3: Change the y-axis label to 'Frequency'
fig.update_yaxes(title_text='Frequency')  # This cannot be done via labels in px.histogram

# Step 4: Show the plot
fig.show()






