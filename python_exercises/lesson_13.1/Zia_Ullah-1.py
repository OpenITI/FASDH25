# import pandas library
import pandas as pd
# read csv
df = pd.read_csv("data/title.csv")

#print the title column
print(df['title'])

#print the title of the longest article
max_length = df['length'].max() # find max value
longest_article = df[df['length'] == max_length] #filter row
print(longest_article['title'].values[0]) #get the title

#printing sum of all article length
total_length = df['length'].sum()
print("total length of All Articles:", total_length)

#export top 20 longest articles to CSV
top20 = df.sort_values(by='length' , ascending=False).head(20)
top20.to_csv("outputs/zia-ullah-top20.csv", index=False)

#combine year, month, day into new column
df['date'] = pd.to_datetime(df[['year', 'month', 'day']]).dt.strftime('%Y-%m-%d')


#export articles from first 6 month of 2023
df_6m_2023 = df[(df['year'] == 2023) & (df['month'] <= 6)]
df_6m_2023.to_csv("outputs/zia-ullah-6m2023.csv", index=False)
        
