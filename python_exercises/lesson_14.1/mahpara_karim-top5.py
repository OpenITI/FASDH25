import pandas as pd
import plotly.express as px

# Reading in the dataset
df = pd.read_csv('data/1-gram.csv') 
print(df.head())

# A manually defined list of common stopwords (based on NLTK) to filter out
custom_stopwords = {
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 
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
    'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now'
}

# Exclude rows where the unigram is found in the stopwords set
df = df[~df['1-gram'].isin(custom_stopwords)]

# Identify the 5 most frequent unigrams across the dataset
top_5_grams = df.groupby('1-gram')['count'].sum().nlargest(5).index.tolist()
df_top5 = df[df['1-gram'].isin(top_5_grams)].copy()
print(df_top5)

# Create a datetime column from year and month for plotting trends
df_top5['date'] = pd.to_datetime(df_top5[['year', 'month']].assign(day=1))

# Aggregate the total monthly frequency for each of the top 5 unigrams
df_top5['year_month'] = pd.to_datetime(df_top5[['year', 'month']].assign(day=1))
df_monthly = df_top5.groupby(['date', '1-gram'])['count'].sum().reset_index()

# Generate a line plot to visualize how the top unigrams vary over time
fig = px.line(
    df_monthly, 
    x="date", 
    y="count", 
    color="1-gram",
    title="Evolution of Top 5 Unigrams in News Corpus",
    labels={"count": "Frequency", "date": "Month"},
    markers=True
)

fig.show()

# Export the plot as an interactive HTML file
fig.write_html("mahpara_karim_top5_evolutions.html")
