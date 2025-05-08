# import necessary libraries

import pandas as pd
# Step 3: Read the CSV and print the titles column
df = pd.read_csv("data/title.csv")
print(df["title"])

# Step 4: Print the title of the longest article
longest_article = df[df["length"] == df["length"].max()]
print("Title of the longest article:")
print(longest_article["title"].values[0])

# Step 5: Print the sum of all article lengths
total_length = df["length"].sum()
print("Sum of all article lengths:", total_length)

# Step 6: Export top 20 longest articles
top20 = df.sort_values(by="length", ascending=False).head(20)
top20.to_csv("outputs/atiqa_rani_top20.csv", index=False)

# Step 7: Combine year, month, day into a new column
df["date"] = df["year"].astype(str) + "-" + df["month"].astype(str).str.zfill(2) + "-" + df["day"].astype(str).str.zfill(2)

# Step 8: Export articles from the first 6 months of 2023
df_2023_6m = df[(df["year"] == 2023) & (df["month"] <= 6)]
df_2023_6m.to_csv("outputs/atiqa_rani-6m2023.csv", index=False)
