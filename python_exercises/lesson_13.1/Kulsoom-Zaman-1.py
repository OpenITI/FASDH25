import pandas as pd

# reads the csv file
df=pd.read_csv("data/title.csv")

#prints the title column
print(df["title"])

#looking for the column with leghth and returning the max value in that column
max_length= df["length"].max()

# filtering operATION: selecting only rows where lenghth is equal to max lenghth
longest_title=df[df["length"]== max_length]

#gets the title column from filtered row                 
print("Longest title of article:", longest_title['title'].values[0])

# adding the values in length column
total_length=df['length'].sum()

#Print the total length
print("All articles total length:", total_length)

#sorting the dataframe based on values in the length column
top_20= df.sort_values(by='length', ascending=False).head(20)


#exporting the top 20 longest artcile to a csv
top_20.to_csv('outputs/Kulsoom-Zaman-20.csv', index=False)

# Create a new column 'date' by combining the 'year', 'month', and 'day' columns
# First, convert each column to a string type and format the month and day with leading zeroes if needed
df['date'] = df['year'].astype(str) + '-' + df['month'].astype(str).str.zfill(2) + '-' + df['day'].astype(str).str.zfill(2)

# filtering the articles with specific year and month
first_half_2023 = df[
    (df['year'] == 2023) & # Filter articles written in 2023
    (df['month'] >= 1) & # Filter articles written from January (month 1) onwards
    (df['month'] <= 6)  # Filter articles written until June (month 6)
]

#exporting the top filtered articles to a csv
first_half_2023.to_csv('outputs/Kulsoom-Zaman-half2023.csv', index=False)

 
