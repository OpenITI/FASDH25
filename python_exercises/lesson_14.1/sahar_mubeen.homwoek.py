# load libraries
import pandas as pd
import plotly.express as px
import nltk
from nltk.corpus import stopwords

# Download the stopwords dataset from NLTK
nltk.download('stopwords')

# Load the CSV data into a DataFrame

df = pd.read_csv('FASDH25\python_exercises\lesson_14.1\data\1-gram.csv')
print(df.head())

# List of common English stopwords (taken from NLTK)
custom_stopwords = set(stopwords.words("english"))

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
