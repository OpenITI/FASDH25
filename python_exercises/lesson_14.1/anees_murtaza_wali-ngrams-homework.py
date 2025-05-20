import pandas as pd
import plotly.express as px

# Step 1: Load the CSV file containing the 1-gram data
df = pd.read_csv('data/1-gram.csv')
print(df.head())  # Display the first few rows to understand the structure

# Step 2: Define a basic list of common stop words 
# (words like "the", "and", "is" that don't add much meaning)
stop_words = {
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 
    'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 
    'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 
    'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 
    'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 
    'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 
    'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 
    'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 
    'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 
    'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 
    'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 
    'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 
    'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 
    'just', 'don', 'should', 'now'
}

# Step 3: Remove rows where the word (1-gram) is a stop word
# We only want meaningful words, not filler words
df = df[~df['1-gram'].isin(stop_words)]

# Step 4: Find the top 5 most frequent words (unigrams) across all the data
top_5_unigrams = df.groupby('1-gram')['count'].sum().nlargest(5).reset_index()
print("Top 5 Unigrams Globally:")
print(top_5_unigrams)

# Step 5: Filter the DataFrame to include only these top 5 words
# This will help us focus only on the most important terms
df_top5 = df[df['1-gram'].isin(top_5_unigrams['1-gram'])]

# Step 6 Create a new 'date' column from the year, month, and day 
# Use .loc to avoid the Setting With Copy Warning
#chat GPT work
df_top5 = df_top5.copy()  
df_top5.loc[:, 'date'] = pd.to_datetime(df_top5[['year', 'month', 'day']])


# Step 7: Group by date and word to get the total count for each word on each day
# This lets us track how often each word appears over time
df_evolution = df_top5.groupby(['date', '1-gram'])['count'].sum().reset_index()

# Step 8: Plot the results as a line graph
# We'll see how the usage of these top 5 words changes over time
fig = px.line(
    df_evolution, 
    x='date', 
    y='count', 
    color='1-gram',
    title='Top 5 Unigrams Evolution Over Time',
    labels={'count': 'Frequency', 'date': 'Date', '1-gram': 'Word'}
)

# Step 9: Display the plot
fig.show()
