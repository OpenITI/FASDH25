# pull in pandas
import pandas as pd
#pull in title columns
df=pd.read_csv('data/title.csv')
print(list(df.columns))

#print longest artcile, code aided by ChatGPT

max_length = df["length"].max()
longest_article_title = df[df["length"] == max_length]["title"].values[0]
print("\nTitle of the Longest Article:")
print(longest_article_title)

    
#sum of all articles
total_length = df["length"].sum()
print("\nSum of All Article Lengths:")
print(total_length)

#export 20 articles to csv, code aided by ChateGPT
top20_df = df.sort_values(by="length", ascending=False).head(20)
top20_df.to_csv("outputs/Shaharyar-Morani-top20.csv", index=False)

#combine year month and date
df["date"] = df["year"].astype(str) + "-" + df["month"].astype(str).str.zfill(2) + "-" + df["day"].astype(str).str.zfill(2)

# filter for articles from first 6 months of 2023
df_2023_6m = df[(df["year"] == 2023) & (df["month"] <= 6)]
df_2023_6m.to_csv("outputs/Shaharyar-Morani-6m2023.csv", index=False)
