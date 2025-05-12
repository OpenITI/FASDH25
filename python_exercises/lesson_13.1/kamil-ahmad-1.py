import pandas as pd

# Load the dataset from the folder
df = pd.read_csv("data/title.csv")

# Display all the article titles
print(df['title'])

# Identify and print the title of the article with the greatest length
longest_article = df[df['length'] == df['length'].max()]
print("Title of the longest article:")
print(longest_article['title'].values[0])

# Compute and display the total length across all articles
total_length = df['length'].sum()
print("Combined length of all articles:", total_length)

# Select the top 20 articles based on length and save them to a CSV file
top20 = df.sort_values(by='length', ascending=False).head(20)
top20.to_csv("outputs/kamil-ahmad-top20.csv", index=False)

# Create a new date column formatted as 'YYYY-MM-DD'
df['date'] = df['year'].astype(str) + '-' + df['month'].astype(str).str.zfill(2) + '-' + df['day'].astype(str).str.zfill(2)

# Extract articles published from January to June 2023
df_2023_6m = df[(df['year'] == 2023) & (df['month'] <= 6)]
df_2023_6m.to_csv("outputs/kamil-ahmad-6m2023.csv", index=False)
