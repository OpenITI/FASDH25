import pandas as pd
import nltk
from nltk.corpus import stopwords
import plotly.express as px

# Step 1: Load the CSV file
df = pd.read_csv("C:/Users/Dell/Downloads/FASDH25/python_exercises/lesson_14.1/data/1-gram.csv")

# Step 2: Create a single datetime column
df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
df['year_month'] = df['date'].dt.to_period('M').dt.to_timestamp() # I learn timestamp from chatgpt


# Step 3: Import stop words from NLTK (or a reliable list)

stop_words = set(stopwords.words("english"))

# Step 4: Remove stop words
df = df[~df["1-gram"].isin(stop_words)]

# Step 5: Find 5 most frequent 1-grams in the entire corpus
top5 = df.groupby("1-gram")["count"].sum().nlargest(5).index


# Step 6: Filter the DataFrame for only these 5 unigrams
df_top5 = df[df["1-gram"].isin(top5)]

# Step 7: Group by month and unigram
monthly_counts = df_top5.groupby(['year_month', '1-gram'])['count'].sum().reset_index()
print(monthly_counts) 

# Step 8: Create the line chart using plotly
fig = px.line(
    monthly_counts,
    x="year_month",
    y="count",
    color="1-gram",
    title="Monthly Frequency of Top 5 Unigrams)",
    labels={
        "year_month": "Month",
        "count": "Frequency",
        "1-gram": "Unigram"
    }
)

# Step 9: Show the chart and save it as an HTML file
fig.write_html("Abdus_Salam_top5_plot.html")
fig.show()
