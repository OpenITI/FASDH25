import pandas as pd

# Load the dataset containing article information
data = pd.read_csv("data/title.csv")

# Display all the article titles
print("List of Article Titles:")
print(data["title"])

# Identify the article with the maximum length
max_len = data["length"].max()
longest = data[data["length"] == max_len]
print("\nTitle of the Longest Article:")
print(longest["title"].values[0])  # Extract title string

# Calculate the cumulative length of all articles
total_len = data["length"].sum()
print("\nCombined Length of All Articles:", total_len)

# Extract the top 20 articles with the highest lengths
top_twenty = data.sort_values(by="length", ascending=False).head(20)
top_twenty.to_csv("outputs/kamran-abid-top20.csv", index=False)

# Construct a proper date column in the format YYYY-MM-DD
data["date"] = (
    data["year"].astype(str) + "-" +
    data["month"].astype(str).str.zfill(2) + "-" +
    data["day"].astype(str).str.zfill(2)
)

# Filter articles published in the first half of the year 2023 (Jan–Jun)
first_half = data[(data["year"] == 2023) & (data["month"] <= 6)]
first_half.to_csv("outputs/kamran-abid-6m2023.csv", index=False)

print("\nFiltered articles from Jan to Jun 2023 saved to 'kamran-abid-6m2023.csv'.")
