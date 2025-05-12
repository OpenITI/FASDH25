import pandas as pd

# Read the CSV file
df = pd.read_csv('data/title.csv')

# print the title column

print(df['title'])

# print the title of the longest article

longest_article = df[df['length'] == df['length'].max()]
print("longest article title is")
print(longest_article['title'].values[0])


# Print the sum of all articles’ lengths

total_length = df['length'].sum()
print("Total length of all articles is", total_length)

# Sort by length and get top 20
top_20 = df.sort_values(by='length', ascending=False).head(20)

# Export to CSV in the outputs folder
top_20.to_csv('outputs/mehtab-alikhan-top20.csv', index=False)


# Convert each part to string and combine them
df['date'] = df['year'].astype(str) + '-' + df['month'].astype(str).str.zfill(2) + '-' + df['day'].astype(str).str.zfill(2)

# Print the new column
print(df['date'])

# Filter rows where year is 2023 and month is 1 to 6
first_half_2023 = df[(df['year'] == 2023) & (df['month'] <= 6)]

# Save to CSV
first_half_2023.to_csv('mehtab-alikhan-6m2023.csv', index=False)
