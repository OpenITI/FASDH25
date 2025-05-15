import pandas as pd
import plotly as px


#read and load the csv file
df = pd.read_csv("data/1-gram.csv")

#printing first 10 rows
print(df.head(10))

#sort the dataframe by frequency and print the row with the 10 highest frequencies

#sort the data by frequency

#create a subset
filter = df["1-gram"].isin(["peace", "agreement", "truce"])
df2 = df[ filter ]
print(df2)
