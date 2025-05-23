#import libraries

import pandas as pd
import plotly.express as px

# reads the csv file
df=pd.read_csv("data/title.csv")

#plot the histogram

fig = px.histogram(df, x='length',
                   nbins=10,
                   title='Distribution of Title Lengths',
                   labels={'length': 'lenght in tokens'})

#add ticks to x-axis
xaxis=dict(
        tickmode='linear',   # evenly spaced ticks
        tick0=0,             # start from 0
        dtick=1              # show a tick every 1 unit
    )


# updat y-label to frequency
fig.update_layout(
    xaxis_title='Title Length (in words)',
    yaxis_title='Frequency',
    title_font_size=20,
    xaxis_tickangle=0,
    bargap=0.1,)
