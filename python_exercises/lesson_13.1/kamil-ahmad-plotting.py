# Import the necessary modules

import plotly.express as px
import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("../lesson_13.1/data/title.csv")

# Display the first few entries of the DataFrame
print(df.head())

# Step 1. Generate a histogram to visualize article lengths
fig = px.histogram(
    df,
    x='length',  # specify the column for the x-axis
    title='Article Length Distribution in Gaza Corpus',
    color='year',
    labels={'length': 'Article Length'}  # define label for the x-axis
)

# Step 2. Set x-axis ticks (optional customization)
fig.update_xaxes(
    tickmode='linear',  # enable evenly spaced ticks
    tick0=0,            # set the starting tick value
    dtick=200           # specify the interval between ticks
)

# Step 3. Update the y-axis label to reflect frequency count
fig.update_yaxes(title_text='Frequency')  # direct label update for y-axis

# Step 4. Display the final visualization
fig.show()
