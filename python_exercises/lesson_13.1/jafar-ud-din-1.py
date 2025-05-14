
import pandas as pd

#read csv file
df = pd.read_csv("data/title.csv")

#print the title column
print(df["title"])

#finding the longest article based on length of colum
max_length = df["length"].max() #for max length
longest_article = df[df["length"] == max_length] #filter rows with max length

#print title of longest article
print("Title of longest article:")
print(longest_article["title"].values[0])

#select the length column and add the values in it
total_length = df['length'].sum()
#print the sum
print('Total number of words in all articles:', total_length)

#sorting the dataframe based on values in the lenth column
top_20_articles = df.sort_values(by='length', ascending=False).head(20)

#exporting the top 20 lingest article to a csv
top_20_articles.to_csv('outputs/Jafar-Uddin-20.csv', index=False)

#combine year, month and day into column in format yyy-mm-dd
df['date'] = (
    df['year'].astype(str) + '-' +
    df['month'].astype(str).str.zfill(2) + '-' +
    df['day'].astype(str).str.zfill(2)
)
#checking if it worked
print(df[['year', 'month', 'day', 'date']].head())

#filtering the articles with spcific year and month
first_half_2023 = df[(df['year'] == 2023) & (df['month'] <=6)]

#export to csv
first_half_2023.to_csv("outputs/Jafar-Uddin-half2023.csv", index=False)
