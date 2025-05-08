import pandas as pd

df = pd.read_csv("data/title.csv")

print (df['title'])

# find the length of the longest article
max_length = df['length'].max()

# filter the rows with max length ## boolean true/false
longest_article = df[df['length'] == max_length]

# print the title of the longest article
print(longest_article['title'].values[0])

# print the sum of all article length
print("total length of articles:", df['length'].sum())

# export top 20 longest articles
top20 = df.sort_values(by='length', ascending=False).head(20)
# df.sort_values (by='length', ascending=False) sorts the dataframe by the length of column from from largest to samllest as ascending is false
# .head(20) takes the first 20 rows of sorted dataframe

top20.to_csv('outputs/Faizan-Amir-top20.csv',index=False)

# Combine the year, month and day into a new column “{yyyy}-{mm}-{dd}”
df['date'] = df['year'].astype(str) + '-' + df['month'].astype(str).str.zfill(2) + '-' + df['day'].astype(str).str.zfill(2)

# export articles that were written in the first 6 months of 2023
six_months_2023 = df[(df['year'] == 2023) & (df['month'] <= 6)]
six_months_2023.to_csv('outputs/Faizan-Amir-6m2023.csv', index=False)
