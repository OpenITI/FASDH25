import pandas as pd

# Read the CSV file
df = pd.read_csv("data/title.csv")

# Print the 'title' column
print(df['title'])

# Print the title of the longest article
# Assuming there is a 'length' column representing article length
longest_article = df[df['length'] == df['length'].max()]
print("Longest article title:")
print(longest_article['title'].values[0])

# Print the sum of all article lengths
total_length = df['length'].sum()
print("Total length of all articles:", total_length)

# Export the 20 longest articles
top20 = df.sort_values(by='length', ascending=False).head(20)
top20.to_csv("outputs/abdus-salam-top20.csv", index=False)

# Combine year, month, day into a new column called 'date'
df['date'] = df['year'].astype(str) + '-' + df['month'].astype(str).str.zfill(2) + '-' + df['day'].astype(str).str.zfill(2)

# Filter articles from Jan to June 2023
df_2023_6m = df[(df['year'] == 2023) & (df['month'] <= 6)]
df_2023_6m.to_csv("outputs/abdus-salam-6m2023.csv", index=False)

