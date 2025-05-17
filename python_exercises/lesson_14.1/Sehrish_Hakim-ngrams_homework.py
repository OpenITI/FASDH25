#Import libraries for data handling and plotting
import pandas as pd
import plotly.express as px

#Import stopwords from NLTK to filter out common words
#taken help from https://www.tutorialkart.com/nlp/nlp-stop-word-removal/
import nltk
from nltk.corpus import stopwords

#Download the stopwords list 
nltk.download('stopwords')

#Load the list of English stopwords
stop_words = set(stopwords.words('english'))

#Load the CSV file into a DataFrame
path = "data/1-gram.csv"
df = pd.read_csv(path)

#Print the first 10 rows to understand the structure
print("First 10 rows of the dataset:")
print(df.head(10))

#Combine year and month into a proper date column for time-series plotting 

df["date"] = pd.to_datetime(df[["year", "month"]].assign(day=1))

#Remove stopwords from the 1-gram column
#This helps us focus on more meaningful content words
df = df[~df["1-gram"].isin(stop_words)]

#Group by 1-gram to get total frequency across the corpus
#summing across all months to get the overall frequency
total_freq = df.groupby("1-gram")["count"].sum().reset_index()

#Sort to find the top 5 most frequent unigrams
top5 = total_freq.sort_values(by="count", ascending=False).head(5)
print("\nTop 5 most frequent unigrams (excluding stopwords):")
print(top5)

#Filter the main dataframe to include only those top 5 unigrams
df2 = df[df["1-gram"].isin(top5["1-gram"])]

#Group the filtered data by month and 1-gram
df_monthly = df2.groupby(["date", "1-gram"])["count"].sum().reset_index()


# Creating a line plot using Plotly Express
fig = px.line(
    df_monthly,                  # Data source
    x="date",                   # X-axis: time
    y="count",                   # Y-axis: frequency
    color="1-gram",              # Separate lines per unigram
    title="Evolution of Top 5 Unigrams in News Corpus",  # Title of the chart
    labels={"count": "Frequency", "month": "Time"},      # Axis labels
    markers=True                 # Adds markers to each point on the line
)

#Save the graph as html file
fig.write_html("top5_unigrams_trend.html")

#Display the graph 
fig.show()

