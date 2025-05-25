# atiya-kiyani-1.py

import pandas as pd

# Step 1: Read the CSV file
df = pd.read_csv("data/title.csv")

# Step 2: Print the title column
print(df["title"])

# Step 3: Print the title of the longest article
longest_article = df[df["length"] == df["length"].max()]
print("Longest article title:", longest_article["title"].values[0])

# Step 4: Print the sum of all article lengths
total_length = df["length"].sum()
print("Sum of all article lengths:", total_length)

# Step 5: Export the 20 longest articles to a new CSV
top20 = df.sort_values(by="length", ascending=False).head(20)
top20.to_csv("outputs/atiya-kiyani-top20.csv", index=False)

# Step 6: Create a new date column in yyyy-mm-dd format
df["date"] = df["year"].astype(str) + "-" + df["month"].astype(str).str.zfill(2) + "-" + df["day"].astype(str).str.zfill(2)

# Step 7: Export articles written in the first 6 months of 2023
six_months_2023 = df[(df["year"] == 2023) & (df["month"] <= 6)]
six_months_2023.to_csv("outputs/atiya-kiyani-6m2023.csv", index=False)
