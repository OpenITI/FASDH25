import pandas as pd
import plotly.express as px

#loading the csv
df=pd.read_csv("data/topic-model.csv")

#printing the first few rows to understand the structure
print(df.head())

#printing the first five artciles titles to set a suitable a topic label
print(df[df['Topic'] == 0]['title'].head(5))

