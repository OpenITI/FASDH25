import pandas as pd
import plotly.express as px

df = pd.read_csv("data/1-gram.csv")
print(df.head(10))

filter = df["1-gram"].isin(["peace", "agreement", "truce"])
df2 = df[ filter ]
print(df2)

fig = px.line(
    df2,
    x="month",
    y="count",
    title="Monthly Frequency of Selected Unigrams",
    labels={"month": "Month", "frequency": "Frequency", "1-gram": "Unigram"}
)


fig.show()


