import pandas as pd
import plotly.express as px

#load the csv file.
df = pd.read_csv("data/1-gram.csv")

# print the first 10 rows
print(df.head(10))



filter = df["1-gram"].isin(["peace", "agreement", "truce"])
df2 = df[ filter ]

print(df2)

s



