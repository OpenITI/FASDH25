# Import libraries
import pandas as pd

#read the path 
path_csv = "C:/Users/HP/Downloads/FASDH25/python_exercises/lesson_13.1/data/title.csv"
df = pd.read_csv(path_csv)
print(df.columns)
column_title = df["title"]
print(column_title)

# Get the index of the longest article based on 'length' column
longest_index = df['length'].idxmax()

# Use that index to get the full row and print the title
print("Title of the longest article:", df.loc[longest_index]['title'])

# Get the sum of all article lengths in the 'length' column
total_length = df['length'].sum()

# Print the total length of all articles
print("Sum of all article lengths:", total_length)

# Sort the DataFrame by the 'length' column in descending order and select the top 20
top_20_articles = df.sort_values(by='length', ascending=False).head(20)

# Export the top 20 articles to a CSV file
top_20_articles.to_csv('outputs/sarir-ahmad-top20.csv', index=False)

# Assuming the columns are named 'year', 'month', and 'day'
df['date'] = df['year'].astype(str) + '-' + df['month'].astype(str).str.zfill(2) + '-' + df['day'].astype(str).str.zfill(2)

# Print the updated DataFrame to check the new 'date' column
print(df[['year', 'month', 'day', 'date']].head())

# Filter articles written in the first 6 months of 2023
filtered_articles = df[(df['year'] == 2023) & (df['month'] <= 6)]

# Export the filtered articles to a CSV file
filtered_articles.to_csv('outputs/naveera-taj-6m2023.csv', index=False)



