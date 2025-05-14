# Import the necessary libraries
import plotly.express as px
import pandas as pd

# Assign the path to the CSV file
csv_path = "data/title.csv"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_path)

# Create a histogram for the 'length' column
fig = px.histogram(df, x='length', title='Distribution of Article Lengths', color='Pink')

# Customize the axis labels and tick marks
fig.update_layout(
    xaxis_title='Article Length',  # Label for the x-axis
    yaxis_title='Frequency')  # Label for the y-axis

# Show the figure
fig.show()
