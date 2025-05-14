import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("data/title.csv")

# Print all the article titles
print("All article titles:")
print(df["title"])

# Find the maximum value in the 'length' column
max_length = df["length"].max()

# Find the row where the article has the maximum length
longest_article = df[df["length"] == max_length]

# Print the title of the longest article
print("Longest article title:", longest_article['title'].values[0])

# Calculate the total length of all articles combined
total_length = df['length'].sum()
print("Total length of all articles:", total_length)

# Sort the articles by length in descending order and get the top 20 longest articles
top_20 = df.sort_values(by='length', ascending=False).head(20)

# Save the top 20 longest articles to a new CSV file
top_20.to_csv('outputs/Arsalan-Danish-top20.csv', index=False)

# Create a new column called 'date' by combining the year, month, and day columns in "yyyy-mm-dd" format
df['date'] = (
    df['year'].astype(str) + '-' +
    df['month'].astype(str).str.zfill(2) + '-' +
    df['day'].astype(str).str.zfill(2)
)

# Filter the DataFrame to include only articles from the first half of 2023 (January to June)
first_half_2023 = df[
    (df['year'] == 2023) &
    (df['month'] >= 1) &
    (df['month'] <= 6)
]

# Export this filtered DataFrame to a new CSV file
first_half_2023.to_csv('outputs/Arsalan-Danish-6m2023.csv', index=False)

