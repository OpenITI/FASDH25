# importing necessary libraires

import pandas as pd
import os
# read the csv file into a dataframe
df = pd.read_csv("../lesson_13.1/data/title.csv")

# print the titles column
print("All article titles:")
print(df["title"])

# write a code to find and print the title of lonngest article
# First, find the maximum length
max_length = df["length"].max()

# Now filter the DataFrame to get the rows with this length
longest_article = df[df["length"] == max_length]

# Get the title from the filtered row
longest_title = longest_article["title"].values[0]
print("The longest article title is:")
print(longest_title)

# Step 4: Print the sum of all article lengths
total_length = df["length"].sum()
print("The total length of all articles is:")
print(total_length)

# Step 5: Export the 20 longest articles
# Sort the DataFrame by length in descending order
sorted_df = df.sort_values(by="length", ascending=False)

# Get the top 20 longest articles
top_20 = sorted_df.head(20)

# Make sure the "outputs" folder exists
os.makedirs("outputs", exist_ok=True)

# Save the top 20 articles to a new CSV file
top20_filename = "../lesson_13.1/outputs/sahar_mubeen_top20.csv"
top_20.to_csv(top20_filename, index=False)

print("Top 20 longest articles saved to:")
print(top20_filename)

# Step 6: Create a new column with date formatted as yyyy-mm-dd
# Convert year, month, and day to strings
year_str = df["year"].astype(str)
month_str = df["month"].astype(str).str.zfill(2)  # pad month with 0 if needed
day_str = df["day"].astype(str).str.zfill(2)      # pad day with 0 if needed

# Combine into a new "date" column
df["date"] = year_str + "-" + month_str + "-" + day_str

# Step 7: Filter articles from the first 6 months of 2023
first_half_2023 = df[(df["year"] == 2023) & (df["month"] <= 6)]

# Save this filtered data to another CSV file
filename_6months = "../lesson_13.1/outputs/sahar_mubeen_6m2023.csv"
first_half_2023.to_csv(filename_6months, index=False)

print("Articles from Jan to Jun 2023 saved to:")
print(filename_6months)



