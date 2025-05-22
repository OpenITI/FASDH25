#import libraries

import pandas as pd
import plotly.express as px

#load the csv
df = pd.read_csv("../lesson_14.1/data/1-gram.csv")

#print the first ten rows
print(df.head(10))

#sort the dataframe
df_sorted = df.sort_values(by='count', ascending=False)

#filter the data
filter = df["1-gram"].isin(["peace", "agreement", "truce"])

df2 = df[filter].copy()

print(df2)

#coombine year, month, and day to create a date column
df2["date"] = pd.to_datetime({
    "year": df2["year"],
    "month": df2["month"],
    "day": df2["day"]
})

#built a new column for just year and month

df2["month_year"] = df2["date"].dt.to_period("M")

#group by month and 1-gram, and sum the counts

grouped = df2.groupby(["month_year", "1-gram"])["count"].sum().reset_index()

#convert month_year back to a full date

grouped["month_year"] = grouped["month_year"].dt.to_timestamp()
    
#plot the line graph

fig = px.line(grouped,
              x="month_year",
              y="count",
              color="1-gram",
              title="Frequency of selected 1-grams by month",
              markers = True, labels={'month_year':'Date', 'count':'Frequency'}
              )
#save the figure as html
fig.write_html("Zehrish_Iqbal_ngram1_plot.html")
fig.show()
