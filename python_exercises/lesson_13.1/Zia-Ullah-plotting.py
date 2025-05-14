import pandas as pd 
import plotly.express as px
import os

# Ensure the 'outputs' directory exists
os.makedirs("outputs", exist_ok=True)

# Load the data
df = pd.read_csv("data/title.csv")

# Filter for short articles
df_short = df[df['length'] < 300]

# Plot 1: Short articles by year
fig1 = px.histogram(df_short, x='length', color='year', title='Article Lengths < 300 words by year')
fig1.update_layout(xaxis_title='Length', yaxis_title='Frequency')
fig1.write_html("outputs/zia-ullah-short-articles.html")
print("succesfully saved")

# Filter for recent years
df_recent = df[df['year'].isin([2023, 2024])]

# Plot Articles in 2023 and 2024
fig2 = px.histogram(df_recent, x='length', color='year', title='Article Length in 2023 & 2024')
fig2.update_layout(xaxis_title='Length', yaxis_title='Frequency')
fig2.add_annotation(
    x=100,
    y=20,
    text="Spike at 100 words",
    showarrow=True,
    arrowhead=1
)
fig2.write_html("outputs/zia-ullah-2023-2024.html")
print("successfully saved")

# Filter for Q4 of 2023
df_q4 = df[(df['year'] == 2023) & (df['month'].isin([10, 11, 12]))]

# Plot 3 Q4 articles by month
fig3 = px.histogram(df_q4, x='length', color='month', title='Article Lengths in Q4 2023')
fig3.update_layout(xaxis_title='Length', yaxis_title='Frequency')
fig3.add_annotation(
    x=250,
    y=10,
    text="Longer articles in December",
    showarrow=True,
    arrowhead=1
)
fig3.write_html("outputs/zia-ullah-q4-2023.html")
print("successfully saved")


   
