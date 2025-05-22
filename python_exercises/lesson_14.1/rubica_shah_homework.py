import pandas as pd
import nltk
from nltk.corpus import stopwords
import plotly.express as px

# Load the data
df = pd.read_csv("data/1-gram.csv")
print(df.head()) 

# Create a single datetime column
df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
df['year_month'] = df['date'].dt.to_period('M').dt.to_timestamp() # I learn timestamp from chatgpt

# Remove stopwords
stop_words = set(stopwords.words('english'))

df = df[~df['1-gram'].isin(stop_words)]

# Get top 5 unigrams 
top5 = df.groupby('1-gram')['count'].sum().nlargest(5).index

# Filter to only top 5 unigrams
df_top5 = df[df['1-gram'].isin(top5)]

# Group by month and unigram
monthly_counts = df_top5.groupby(['year_month', '1-gram'])['count'].sum().reset_index()
print(monthly_counts) 

# Create line plot
fig = px.line(
    monthly_counts,
    x='year_month',
    y='count',
    color='1-gram',
    title='Monthly Frequency of Top 5 Unigrams',
    labels={
        'year_month': 'Month',
        'count': 'Frequency',
        '1-gram': 'Unigram'
    }
)

# Save plot to HTML
fig.write_html("Rubica_Shah_top_5_unigrams_plot.html")
fig.show()


  
