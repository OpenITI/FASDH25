import pandas as pd
import plotly.express as px

csv_path = r"C:\Users\DELL\Downloads\FASDH25\python_exercises\lesson_14.1\data\1-gram.csv"

df = pd.read_csv(csv_path)

print(df.head(10))

filter= df["1-gram"].isin(['peace','agreement','truce'])

df2= df[filter]

print(df2)

fig = px.line(df2, x="month", y="count", color="1-gram")

fig.show()





