import  pandas  as pd
import plotly.express as px

data_path = "data/1-gram.csv"

# Read titles.csv as a pandas dataframe
df = pd.read_csv(data_path)

# Print the first ten rows
print(df.head(10))

# Sort by the 'frequency' column in descending order and print the top 10 rows
df_sorted = df.sort_values(by='count', ascending=False)
print(df_sorted.head(10))

# Create a subset with only the specified 1-grams
df2 = df[df['1-gram'].isin(["peace", "agreement", "truce"])]
# Print the new subset
print(df2)

# Creating line graph
fig = px.line(
    df2, 
    x='month', 
    y='count', 
    color='1-gram', 
    title='Frequency of Unigrams Over Time',
    labels={'month': 'Month', 'count': 'Counts', '1-gram': 'Unigram'}
)

#Show graph
fig.show()


