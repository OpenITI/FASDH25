# import libraries
import pandas as pd
# Path to read
path_csv = "C:/Users/HP/Downloads/FASDH25/python_exercises/lesson_13.1/data/title.csv"
# read 
df = pd.read_csv(path_csv)
# Inspect the first few rows to verify column names
print(df.head())
# Print the title column
print(df["title"])

# Print the title column
print (df.columns)
# Find the maximum length value
max_length = df["length"].max()

# Locate the row(s) where the length matches the maximum value
longest_article = df[df["length"] == max_length]["title"]

# Print the title of the longest article
print("Title of the longest article:", longest_article.values[0])

# Calculate the sum of all article lengths
total_length = df["length"].sum()

# Print the sum
print("Total length of all articles:", total_length)

# Sort the dataframe by length in descending order and select the top 20 longest articles
top_20_articles = df.sort_values(by="length", ascending=False).head(20)

# Export the top 20 articles to a CSV file
top_20_articles.to_csv("outputs/syed-azhar-uddin-top20.csv", index=False)

# Combine year, month, and day into a new column 'date'
df["date"] = df["year"].astype(str) + "-" + df["month"].astype(str).str.zfill(2) + "-" + df["day"].astype(str).str.zfill(2)

# Print the new 'date' column to check the result
print(df["date"])

# Filter articles written in the first 6 months of 2023
df_6m2023 = df[df["date"].str.startswith("2023-0")]

# Export the filtered dataframe to a CSV file
df_6m2023.to_csv("outputs/syed-azhar-uddin-6m2023.csv", index=False)
