import plotly.express as px
import pandas as pd

#load tsv file into dataframe
df = pd.read_csv("data/1-gram.csv")

#print first 10 rows
print(df.head(10))

#sorting the top 10 frequency
top_10= df.sort_values(by='count', ascending=False).head(10)
#printing row with the 10 highest frequencies
print(top_10)

#subset of the dataframe containing the 1-grams
df2 = df[df["1-gram"].isin( ["peace" , "agreement" , "truce"])]
print(df2)


# plot line graph
fig = px.line(
    df2,
    x="month",
    y="count",
    color="1-gram",
    title="Monthly Frequency of Selected Unigrams",
    labels={"month": "Month", "frequency": "Frequency", "1-gram": "Unigram"}
)

fig.show()
