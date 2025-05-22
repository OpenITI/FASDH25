import pandas as pd
import plotly.express as px

# load the unigram frequency data from csv
df = pd.read_csv("data/1-gram.csv")
print(df.head()) #print header to check the data loaded correctly

#Define stopwords
#stop words from NLTK list to check in the corpus
stop_words = { 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 
    'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 
    'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 
    'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 
    'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 
    'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 
    'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 
    'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 
    'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 
    'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 
    'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 
    'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'al', 'said', 'don', 'should', 'now'}

# filter the stop words from the corpus
df_words = df[~df["1-gram"].isin(stop_words)].copy()

# finding the top 5 most frequent meaningful words in the corpus(group by 1-gram and sum count)
top5 = df_words.groupby("1-gram")["count"].sum().nlargest(5).index.tolist()
print("Top five n-grams:", top5)

#top five unigrams in the corpus
df_top5 = df[df['1-gram'].isin(top5)].copy() #.copy to avoid warning
print(df_top5)


# creating date column for proper time series
df_top5["date"] = pd.to_datetime(df_top5[["year", "month", "day"]])

# Group data by month and unigram to get total monthly frequency
df_monthly = df_top5.groupby(["year", "month", "1-gram"])["count"].sum().reset_index()

# Create a comibned time column for x-axis
df_monthly["time"] = pd.to_datetime(df_monthly[["year", "month"]].assign(day=1))

#plot the data as a line chart using plotly

fig = px.line(
    df_monthly,
    x= "time", # time axis (month-year)
    y= "count", 
    color="1-gram", 
    title="Top 5 most frequent n-grams over time in al-jazeera corpus",
    labels={"count": "frequency", "time": "Year"},
    markers=True #add markers for clarity
)
    #save the plot as an interactive HTML file
fig.write_html("top_5_n-grams_over_time.html")
fig.show()
