import pandas as pd
import plotly.express as px

#load the data set
df = pd.read_csv("data/1-gram.csv")

#print the first 10 rows
print(df.head(10))

# Create a subset containing only rows with 1grams values: peace, agreement,or truce
filter = df["1-gram"].isin(["peace", "agreement", "truce"])
df2 = df[ filter ]
print(df2)




