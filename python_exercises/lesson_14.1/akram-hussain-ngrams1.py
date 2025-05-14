#import libraries
import pandas as pd
import plotly.express as px


#load the csv file4

path = "data/1-gram.csv"

df = pd.read_csv(path)

#print the first 10 rows
print(df.head(10))
#sort the first rows 

#sort_freq = df.sort_values (by ="frequency")

#filter the first 10 rows
filter = df ["1-gram"].isin(["peace", "agreement", "truce"])
df2 = df  [ filter ]

print(df2)

#plot the line graph

fig = px.line(df2, x="month", y= "count", color= "1-gram")

fig.show()          
