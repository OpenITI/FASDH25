
# a. Import the plotly and pandas libraries
import pandas as pd
import plotly.express as px

# b. Load the CSV file using the full path

df = pd.read_csv("data/1-gram.csv")

# c. Print the first 10 rows of the dataframe
print(df.head(10))

# sort the data by frequency


