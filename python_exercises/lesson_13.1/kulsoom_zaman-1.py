# Import the pandas library for handling data
import pandas as pd 

# Load the CSV file into a DataFrame
df = pd.read_csv("data/title.csv")

# Print the list of all article titles
print("All article titles:")
print(df["title"])

# Determine the maximum article length
max_length = df["length"].max()

# Find the article(s) with the maximum length
longest_title = df[df["length"] == max_length]

# Display the title of the longest article
print("Title of the longest article:", longest_title['title'].values[0])

# Compute the total combined length of all articles
total_length = df['length'].sum()

# Show the total length of all articles
print("Total combined length of all articles:", total_length)

# Identify the top 20 longest articles
top_20 = df.sort_values(by='length', ascending=False).head(20)

# Save the top 20 longest articles to a CSV file
top_20.to_csv('outputs/ulya-batool-top20.csv', index=False)

# Generate a new 'date' column in YYYY-MM-DD format using 'year', 'month', and 'day'
df['date'] = (
    df['year'].astype(str) + '-' +
    df['month'].astype(str).str.zfill(2) + '-' +
    df['day'].astype(str).str.zfill(2)
)

# Filter articles written in the first half (January to June) of 2023
first_half_2023 = df[
    (df['year'] == 2023) &
    (df['month'] >= 1) &
    (df['month'] <= 6)
]

# Save the filtered articles to a new CSV file
first_half_2023.to_csv('outputs/kulsoom-zaman-6m2023.csv', index=False)

# Confirm export of first-half 2023 articles
print("Exported articles from Jan–June 2023 to 'kulsoom-zaman-6m2023.csv'.")
