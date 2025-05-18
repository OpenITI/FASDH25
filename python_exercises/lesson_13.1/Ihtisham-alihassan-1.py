import pandas as pd

# Load the dataset from the CSV file
df = pd.read_csv("data/title.csv")

# Display all values in the 'title' column
print(df["title"])

# Find the maximum value in the 'length' column
max_length = df["length"].max()

# Select rows where the 'length' is equal to the maximum length found
longest_title = df[df["length"] == max_length]

# Display the title of the article with the maximum length
print("Longest article title:", longest_title['title'].values[0])

# Calculate the total of all values in the 'length' column
total_length = df['length'].sum()

# Display the total length of all articles combined
print("The total length of all articles:", total_length)

# Sort the DataFrame in descending order based on 'length' and select the top 20 articles
top_20 = df.sort_values(by='length', ascending=False).head(20)

# Save the top 20 longest articles to a CSV file
top_20.to_csv('outputs/ihtisham-alihassan-top20.csv', index=False)

# Combine year, month, and day into a single column called 'date' in the format yyyy-mm-dd

# learned from chat gpt
df["date"] = df["year"].astype(str) + "-" + df["month"].astype(str).str.zfill(2)

# Filter articles written in the first 6 months (January to June) of 2023
first_6_months_2023 = df[(df["year"] == 2023) & (df["month"] <= 6)]

# Export the filtered articles to a new CSV file
first_6_months_2023.to_csv('outputs/Ihtisham-alihassan-6m2023.csv', index=False)
