import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('data/title.csv')

# Print the 'title' column
print(df['title'])

# Print the title of the longest article
longest_article = df[df['length'] == df['length'].max()]
print("Longest Article Title:", longest_article['title'].values[0])

# Print the sum of all the article lengths
print("Total Length of Articles:", df['length'].sum())

# Export the top 20 longest articles
top20 = df.sort_values(by='length', ascending=False).head(20)
top20.to_csv('outputs/Samrin-Alam-top20.csv', index=False)

# Combine year, month, and day into a new column formatted as "yyyy-mm-dd"
df['date'] = df['year'].astype(str) + '-' + df['month'].astype(str).str.zfill(2) + '-' + df['day'].astype(str).str.zfill(2)

# Export articles written in the first 6 months of 2023
six_months_2023 = df[(df['year'] == 2023) & (df['month'] <= 6)]
six_months_2023.to_csv('outputs/Samrin-Alam-6m2023.csv', index=False)

