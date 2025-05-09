import pandas as pd
import plotly.express as px

# Step 1 & 2: Load the data and create a histogram
df = pd.read_csv("data/title.csv")

# Step 3: Customize the title and x-axis label
fig = px.histogram(
    df,
    x="length",
    title="Distribution of Article Lengths",
    labels={"length": "Article Length"}  # sets x-axis label
)

# Step 4: Add tick marks to the x-axis
fig.update_xaxes(tickmode='linear', tick0=0, dtick=1)

# Step 5: Change the y-axis label to "Frequency"
fig.update_yaxes(title_text='Frequency')

# Step 6: Show the figure
fig.show()
