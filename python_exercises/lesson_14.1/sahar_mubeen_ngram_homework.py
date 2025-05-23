import pandas as pd
import plotly.express as px

# Load the CSV data into a DataFrame

df = pd.read_csv('data/1-gram.csv')
print(df.head())

# List of common English stopwords (taken from NLTK)
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

# Keep only rows where '1-gram' is a stopword
df = df[~df['1-gram'].isin(custom_stopwords)]

# Find the top 5 most frequent stopwords by total count across all dates
top_unigrams = df.groupby('1-gram')['count'].sum().nlargest(5).index.tolist()
print("Top 5 unigrams:", top_unigrams)

# Filter data for these top 5 unigrams only
df_top5 = df[df['1-gram'].isin(top_unigrams)]
print(df_top5)

# Create a proper datetime column from year, month, and day columns
df_top5['date'] = pd.to_datetime(df_top5[['year', 'month', 'day']])

# Sum counts for each date and unigram to prepare for plotting time series
df_plot = df_top5.groupby(['date', '1-gram'])['count'].sum().reset_index()

# Aggregate counts monthly by unigram for visualization
df_top5['year_month'] = pd.to_datetime(df_top5[['year', 'month']].assign(day=1))
df_monthly = df_top5.groupby(['year_month', '1-gram'])['count'].sum().reset_index()

# Plot the monthly frequency trends of the top 5 stopwords
fig = px.line(
    df_monthly,
    x='year_month',
    y='count',
    color='1-gram',
    title='Monthly Frequency of Top 5 unigrams in the Corpus',
    labels={'count': 'Frequency', 'year_month': 'Month'},
    markers=True
)
fig.show()
# saving file
fig.write_html("sahar_unigram_monthly_trends.html")
print("the code is complete here")
