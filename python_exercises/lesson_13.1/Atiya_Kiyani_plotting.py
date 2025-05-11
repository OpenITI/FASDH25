import pandas as pd

# Load the CSV file as a DataFrame
df = pd.read_csv("data/title.csv")

# Show the first few rows to confirm it loaded correctly
print(df.head())

import pandas as pd
import plotly.express as px

# Correct Windows-style path
csv_path = "C:/Users/ATIYA/Downloads/FASDH25/python_exercises/lesson_13.1/data/title.csv"

# Load the data
df = pd.read_csv(csv_path)

# Create a histogram of article lengths
fig = px.histogram(df, 
                   x='length', 
                   title='Distribution of Article Lengths', 
                   labels={'length': 'Article Length'})

# Change the y-axis label to 'Frequency'
fig.update_yaxes(title='Frequency')

# Show the figure
fig.show()
