import pandas as pd

data_path = "data/title.csv"

# Read titles.csv as a pandas dataframe
df = pd.read_csv(data_path)

# Print the titles column
titles_df = df["title"]
print(titles_df)

print("------") # separation between the tasks

# Print the title of the longest article
# Find the maximum length using the .max()method
max_length = df["length"].max()
# Locate the title corresponding to the maximum length
longest_title = df.loc[df["length"] == max_length, "title"].values[0]
print(f"The title of the longest article is: {longest_title}")

print("------") # separation between the tasks

# print the sum of all the articles length
sum_articles_length = df["length"].sum()
print(f"The sum of all the articles length is: {sum_articles_length}")

print("------") # separation between the tasks

# export to a csv a dataframe containing the 20 longest articles (Give dataframe the name: outputs/yasir_rauf_top20.csv)
# Sort the DataFrame by 'length' in descending order and get the top 20 rows
top20_df = df.sort_values(by="length", ascending=False).head(20)
# Export the top 20 articles to a new CSV file
output_path = "../lesson_13.1/outputs/zainab_murtazaali_top20.csv"
top20_df.to_csv(output_path, index=False)

print("------") # separation between the tasks

# Combine the year, month and day into a new column, separated as follows "{yyyy}-{month}-{dd}"
# Convert year, month, and day columns to strings and concatenate them in the desired format
df['date'] = df['year'].astype(str) + '-' + df['month'].astype(str).str.zfill(2) + '-' + df['day'].astype(str).str.zfill(2)
# Print the new dataframe with the 'date' column
print(df[['year', 'month', 'day', 'date']].head())  # Shows the first few rows with the new column

print("------") # separation between the tasks

# export to csv a dataframe containing the articles written in the first 6 months of 2023. (give csv file the name: outputs/yasir_rauf_6m2023.scv)
# Filter the articles from the first 6 months of 2023
filtered_df = df[(df['year'] == 2023) & (df['month'] <= 6)]

# Export the filtered DataFrame to a new CSV file
output_path = "outputs/zainab_murtazaali_6m2023.csv"
filtered_df.to_csv(output_path, index=False)


