import pandas as pd

# Correcting the file path using raw string (r"") or double backslashes (\\)
csv_path = r"C:\Users\aienullah.beg\Downloads\FASDH25\python_exercises\lesson_13.1\data\title.csv"

# Reading the CSV file
df = pd.read_csv(csv_path)

# Printing column names
print(df.columns)


maximum_length = df['length'].max()
print("Maximum Value in length:", maximum_length)


# Locating the row with the maximum length
longest_article_row = df[df['length'] == maximum_length]

# Printing the title of the longest article
print("Title of the Longest Article:", longest_article_row.iloc[0]['title'])

#Sum of all the articles length
total_length_sum = df['length'].sum()
print("Sum of length:", total_length_sum)

# Sorting the DataFrame by 'length' in descending order and selecting the top 20 rows
top_20_longest_articles = df.sort_values(by='length', ascending=False).head(20)

# Defining the output file path
output_csv_path = r"outputs/ali-hasnain-top20.csv"

# Exporting the DataFrame to CSV without the index column
top_20_longest_articles.to_csv(output_csv_path, index=False)

print(f"The top 20 longest articles have been exported to: {output_csv_path}")

# Creating the new 'date' column in the desired format as strings
df['date'] = df['year'].astype(str) + '-' + df['month'].astype(str) + '-' + df['day'].astype(str)

# Displaying the DataFrame with the new column
print(df[['year', 'month', 'day', 'date']].head())

# Filtering the DataFrame for articles written in the first 6 months of 2023
articles_6m_2023 = df[(df['year'] == 2023) & (df['month'] <= 6)]

# Defining the output CSV file path
output_csv_path = r"outputs/ali-hasnain-6m2023.csv"

# Exporting the filtered DataFrame to CSV without the index column
articles_6m_2023.to_csv(output_csv_path, index=False)

print(f"CSV file with articles from the first 6 months of 2023 has been saved at: {output_csv_path}")
