import pandas as pd

df = pd.read_csv("data/title.csv")

print(df['title'])


longest = df['title'].str.len().idxmax()
print("Longest title:", df.loc[longest, 'title'])

# adding the values in length column
total_length=df['length'].sum()

#printing the total length of all articles
print("The total length of  all articles:", total_length)

#sorting the dataframewhich are based on values in the length column
top_20= df.sort_values(by='length', ascending=False).head(20)


#exporting the top 20 longest artcile to a csv
top_20.to_csv('outputs/ali_zain-top20.csv', index=False)

# Creating a new column for 'date' by combining the 'year', 'month', and 'day' columns
# First, convert each column to string type and format the month and day with leading zeroes if needed
df['date'] = df['year'].astype(str) + '-' + df['month'].astype(str).str.zfill(2) + '-' + df['day'].astype(str).str.zfill(2)

# filtering the articles with specific year and month
first_half_2023 = df[
    (df['year'] == 2023) & # Filter articles written in 2023
    (df['month'] >= 1) & # Filter articles written from January (month 1) onwards
    (df['month'] <= 6)  # Filter articles written until June (month 6)
]

#exporting the top filtered articles to a csv
first_half_2023.to_csv('outputs/ali_zain-6m2023.csv',index=False)
