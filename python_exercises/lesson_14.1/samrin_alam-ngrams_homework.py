import pandas as pd
import nltk
from nltk.corpus import stopwords
import plotly.express as px

# Downloading stopwords from NLTK
nltk.download('stopwords')


# Load the data
df = pd.read_csv("data/1-gram.csv")
print(df.head())


# Creating column for date and time
df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
df['year_month'] = df['date'].dt.to_period('M').dt.to_timestamp() # I learn timestamp from chatgpt

# Remove stopwords
stop_words = set(stopwords.words('english'))

df = df[~df['1-gram'].isin(stop_words)]

# finding top 5 unigrams 
top_5_df = df.groupby("1-gram")["count"].sum().sort_values(ascending=False).head(5)
print("Top 5 most frequent non-stopword 1-grams:")
print(top_5_df)

# Filter to only top 5 unigrams
top5_words = top_5_df.index.tolist()
filter = df["1-gram"].isin(top5_words)
df_top5 = df[filter].copy()  
print("Filtered DataFrame (top 5 words):")
print(df_top5.head(10))

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
fig.write_html("samrin_samrin_top_5_unigrams_plot.html")
fig.show()


  

