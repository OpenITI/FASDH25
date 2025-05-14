import pandas as pd

df = pd.read_csv("data/title.csv")

print(df['title'])


longest = df['title'].str.len().idxmax()
print("Longest title:", df.loc[longest, 'title'])
total_length = df['title'].str.len().sum()
print("Total length of all titles:", total_length)
# Load the CSV file
df = pd.read_csv("data/title.csv")

# adding new column for title lengths
df['title_length'] = df['title'].str.len()

# arrange the DataFrame by title length in descending order
sorted_df = df.sort_values(by='title_length', ascending=False)

# selecting top 20 longest titles
top_20 = sorted_df.head(20)

# Export to new CSV
top_20.to_csv("outputs/akram-hussain-top20.csv", index=False)

print("Exported the 20 longest titles to 'outputs/akram-hussain-top20.csv'")

# Assuming the columns are named year, month, and day
df['date'] = df['year'].astype(str) + '-' + df['month'].astype(str).str.zfill(2) + '-' + df['day'].astype(str).str.zfill(2)

# Print the updated DataFrame to check the new 'date' column
print(df[['year', 'month', 'day', 'date']].head())

# Filter articles written in the first 6 months of 2023
filtered_articles = df[(df['year'] == 2023) & (df['month'] <= 6)]

# Export the filtered articles to a CSV file
filtered_articles.to_csv('outputs/akram-hussain-6m2023.csv', index=False)

print("Exported articles from the first 6 months of 2023 to 'outputs/akram-hussain-6m2023.csv'")
