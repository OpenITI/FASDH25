# import pandas library
import pandas as pd
#read csv data
df = pd.read_csv("data/title.csv")

#print title column
print(df['title'])

#print title of the longest article
max_length = df['length'].max() #find maximum value
longest_article = df[df['length'] == max_length] #filtering the row now
print(longest_article['title'].values[0]) #getting the title now


#print the sum of all article length
total_length = df['length'].sum()
print("total length of All Articles:", total_length)

#exporting the top 20 longest articles to CSV
top20 = df.sort_values(by='length' , ascending=False).head(20)
top20.to_csv("outputs/mubashir-hassan-top20.csv", index=False)

#adding year, month, day into the new column (combined)
df['date'] = pd.to_datetime(df[['year', 'month', 'day']]).dt.strftime('%Y-%m-%d')

#exporting articles published from the first 6 months of 2023
df_6m_2023 = df[(df['year'] == 2023) & (df['month'] <= 6)]
df_6m_2023.to_csv("outputs/mubashir-hassan-6m2023.csv", index=False)
