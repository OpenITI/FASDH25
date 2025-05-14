import pandas as pd

df = pd.read_csv("data/title.csv")
print(df.head())
print(df["title"])

#find the maximum length of the articles
max_length = df["length"].max()

#filter the dataframe to rows with that length
longest_article = df[df["length"] == max_length]

#print the title
print(longest_article["title"].values[0])

#finding the sum of all the article lengths
sum_of_lengths = df["length"].sum()
print(sum_of_lengths)

#exporting to csv the 20 longet articles
sorted_df = df.sort_values(by="length", ascending=False)
top20 = sorted_df.head(20)
top20.to_csv("outputs/ayesha-munshi-top20.csv", index=False)

#creating a new column to combine year, month and day
df["year"] = df["year"].astype(str)
df["month"] = df["month"].astype(str).str.zfill(2)  
df["day"] = df["day"].astype(str).str.zfill(2)     
df["date"] = df["year"] + "-" + df["month"] + "-" + df["day"]
print(df[["year", "month", "day", "date"]].head())

#exporting csv to a dataframe containing articles written in the first 6 months of 2023
df["year"] = df["year"].astype(int)
df["month"] = df["month"].astype(int)
first_half_2023 = df[(df["year"] == 2023) & (df["month"] <= 6)]
first_half_2023.to_csv("outputs/firstname-lastname-6m2023.csv", index=False)
