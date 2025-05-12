#importing pandas
import pandas as pd

# Reading the CSV file
df = pd.read_csv('data/title.csv')

#Printing the title column
print(df['title'])

# Printing the title of the longest article
longest_title = df.loc[df['length'].idxmax(), 'title']
print("Longest article title:", longest_title)

# Printing the sum of all article lengths
total_length = df['length'].sum()
print("Total length of all articles:", total_length)

# Exporting top 20 longest articles to csv dataframe
top20 = df.sort_values(by='length', ascending=False).head(20)
top20.to_csv('outputs/rifat-jahan-top20.csv', index=False)

# Combining year, month, and day into a new column
df['date'] = df['year'].astype(str) + '-' + df['month'].astype(str).str.zfill(2) + '-' + df['day'].astype(str).str.zfill(2)

# Exporting articles from first 6 months of 2023
df['date'] = pd.to_datetime(df['date'])
first_half_2023 = df[(df['date'] >= '2023-01-01') & (df['date'] <= '2023-06-30')]
first_half_2023.to_csv('outputs/rifat-jahan-6m2023.csv', index=False)
