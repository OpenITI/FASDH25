import plotly.express as px
import pandas as pd
df = pd.read_csv("1-gram.csv")
print(df.head(10))
filter = df["1-gram"].isin(["peace", "agreement", "truce"])
df2 = df[filter ]
print(df2)

fig = px.line(
