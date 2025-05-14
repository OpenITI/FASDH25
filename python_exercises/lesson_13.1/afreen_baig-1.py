import pandas as pd

# Load the CSV file into a pandas DataFrame
data_path = "data/title.csv"
df = pd.read_csv(data_path)

# Display the titles of all the articles
print("All article titles:\n")
print(df["title"])

print("------")  # Line break to keep output readable

# Find and print the title of the article with the maximum length
max_len = df["length"].max()
longest_article = df.loc[df["length"] == max_len, "title"].values[0]
print(f"Longest article title:\n{longest_article}")

print("------")

# Calculate and print the total length of all articles combined
total_length = df["length"].sum()
print(f"Total word count across all articles: {total_length}")

print("------")

# Sort the data by length and extract the top 20 longest articles
top_20 = df.sort_values(by="length", ascending=False).head(20)

# Save these top 20 articles to a CSV file in the outputs folder
top20_path = "../lesson_13.1/outputs/afreen_baig_top20.csv"
top_20.to_csv(top20_path, index=False)

# Create a new 'date' column formatted as yyyy-mm-dd
df["date"] = (
    df["year"].astype(str) + "-" +
    df["month"].astype(str).str.zfill(2) + "-" +
    df["day"].astype(str).str.zfill(2)
)

# Preview the first few entries with the new date column
print("Preview of combined date column:\n")
print(df[["year", "month", "day", "date"]].head())

print("------")

# Filter out articles published in the first half of 2023 (Jan–June)
first_half_2023 = df[(df["year"] == 2023) & (df["month"] <= 6)]

# Save this filtered data to another CSV file
halfyear_path = "outputs/afreen_baig_6m2023.csv"
first_half_2023.to_csv(halfyear_path, index=False)
