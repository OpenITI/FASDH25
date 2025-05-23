import pandas as pd
import plotly.express as px
import nltk
from nltk.corpus import stopwords

# Download stopwords (only needed the first time)
nltk.download("stopwords")

# Step 1: Load the CSV file
csv_path = "data/1-gram.csv"
df = pd.read_csv(csv_path)

# Step 2: Create a datetime column
df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
df['year_month'] = df['date'].dt.to_period('M').dt.to_timestamp()

# Step 3: Remove stopwords using NLTK's list
stop_words = set(stopwords.words("english"))
df = df[~df['1-gram'].isin(stop_words)]

# Step 4: Aggregate total counts per unigram
unigram_totals = df.groupby("1-gram")["count"].sum()

# Step 5: Identify the top 5 most frequent unigrams overall
top_5_unigrams = unigram_totals.nlargest(5).index

# Step 6: Filter the DataFrame for only these top 5 unigrams
df_top5 = df[df["1-gram"].isin(top_5_unigrams)]

# Step 7: Group by month and unigram, summing the counts
monthly_counts = df_top5.groupby(['year_month', '1-gram'])['count'].sum().reset_index()

# Step 8: Create a line chart
fig = px.line(
    monthly_counts,
    x="year_month",
    y="count",
    color="1-gram",
    title="Top 5 Most Frequent Unigrams per Month",
    labels={
        "year_month": "Month",
        "count": "Frequency",
        "1-gram": "Unigram"
    }
)

# Step 9: Save and show the plot
fig.write_html("syedali_arsalan_top_5_unigrams.html")
fig.show()

print("Plot has been saved as 'syedali_arsalan_top_5_unigrams.html'")
