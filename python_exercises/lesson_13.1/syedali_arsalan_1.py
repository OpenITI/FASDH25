import pandas as pd

# Loading the CSV file
df = pd.read_csv("data/title.csv")

# Printing the 'title' column
print("All article titles:")
print(df["title"])

# Printinh the title of the longest article
# Assuming there's a 'length' column that holds the length of articles
longest_article = df[df["length"] == df["length"].max()]
print("\nLongest article title:")
print(longest_article["title"].values[0])  # .values[0] gets the string from the series

# Printing the sum of all article lengths
print("\nTotal length of all articles:")
print(df["length"].sum())

# Exporting top 20 longest articles
top20 = df.sort_values(by="length", ascending=False).head(20)
top20.to_csv("outputs/syedali-arsalan-top20.csv", index=False)

# Creating a 'date' column from year, month, day
df["date"] = df["year"].astype(str) + "-" + df["month"].astype(str).str.zfill(2) + "-" + df["day"].astype(str).str.zfill(2)

# Filtering articles from first 6 months of 2023
mask_6months_2023 = (df["year"] == 2023) & (df["month"] <= 6)
df_6months = df[mask_6months_2023]
df_6months.to_csv("outputs/syedali-arsalan-6m2023.csv", index=False)
