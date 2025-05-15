# Importing the libraries
import pandas as pd
import plotly.express as px

# Loading the CSV file 
df = pd.read_csv("data/1-gram.csv")

# Printing the first 10 rows 
print(df.head(10))

# Filtering: subset of the dataframe
filter = df["1-gram"].isin(["peace","agreement","truce"])

df2 = df[filter]

print(df2)

# Ploting line graph

fig = px.line(df2, x= "month" , y = "count" , color = "1-gram")

fig.show()
