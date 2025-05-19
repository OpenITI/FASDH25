#import libraries

import pandas as pd
import plotly.express as px
import nltk
from nltk.corpus import stopwords

#Download Stopwords
nltk.download('stopwords')


# Load the csv file
df = pd.read_csv("../lesson_14.1/data/1-gram.csv") 


#get list of stopwords
stop_words = set(stopwords.words('english'))


#filter out where the corpus is an English stop word
df = df[~df['1-gram'].isin(stop_words)]
print("After removing stopwords:")
print(df.head(10))


# Group by '1-gram', then sum counts for finding the most frequent unigrams globally
top5_unigrams = df.groupby('1-gram')["count"].sum().nlargest(5)
print("Top 5 most frequent non-stopwords 1-grams:")
print(top5_unigrams)

#filter the original data to get the top5 1-grams

df_top5 = df[df["1-gram"].isin(top5_unigrams.index.tolist())].copy() 
print("Filtered DataFrame (top 5 1-grams):")
print(df_top5.head(10))

#print
print("Top 5 unigrams:", top5_unigrams)


#create a datetime column
df_top5['date'] = pd.to_datetime({
    'year': df_top5['year'],
    'month': df_top5['month'],
    'day': df_top5['day']
})

#create month_year column
df_top5["month_year"] = df_top5["date"].dt.to_period("M")

# Group by month and 1-gram, summing the counts
grouped = df_top5.groupby(["month_year", "1-gram"])["count"].sum().reset_index()


#print top five unigrams
print(df_top5)



#convert period back to timestamp for plotting
grouped['month_year'] = grouped['month_year'].dt.to_timestamp()

#create line plot
fig = px.line(
    grouped,
    x="month_year",
    y="count",
    color="1-gram",
    title="Evolution of Top 5 Unigrams in News Corpus(Stopwords Excluded)",
    markers=True,
    labels={'month_year': 'Date', 'count': 'Frequency'}
)
#save the figure as html
fig.write_html("Zehrish_Top5_Unigrams_Evolution.html")


