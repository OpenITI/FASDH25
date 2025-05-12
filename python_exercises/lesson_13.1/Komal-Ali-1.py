import pandas as pd

#reads the csv file
df = pd.read_csv("data/title.csv")

#prints the title column of the DataFrame
print(df["title"])

#find the maximum value in the length column
max_length = df["length"].max()

#filters the rows having the maximum length
longest_title= df[df["length"] == max_length]


#print the title of the longest articles
print("The longest article title is:")
print(longest_title["title"].values[0])


# add the total length of all the articles and print 
total_length = df["length"].sum()

print("The total length of all articles:", total_length)


#sorting the DataFrame based on values in the length column
top_20_articles = df.sort_values(by="length", ascending=False).head(20)

#exporting the top 20 longest articles to a csv file
top_20_articles.to_csv("outputs/Komal-Ali-top20.csv", index=False)


#Create a new column with the combination of year, month and day columns
df["date"] = (
    df["year"].astype(str) + "-" +
    df["month"].astype(str).str.zfill(2) +"-" +
    df["day"].astype(str).str.zfill(2)
    )

#print the few rows showing the new date and title 
print(df[["date", "title"]].head())

#filter the DataFrame for articles from the first 6 months of 2023
filtered_df_2023 = df[
    (df["year"] == 2023) &  #articles from the year 2023
    (df["month"] >= 1) &    #from January 
    (df["month"] <= 6)      # to June
]

#Export the filtered Dataframe to a csv file
filtered_df_2023.to_csv("outputs/Komal-Ali-6m2023.csv", index=False)
