import pandas as pd
#upload the data_frame
df = pd.read_csv('data/title.csv')
#shows all the titles in column
print(df['title'])
#get title of longest artical
max_length = df["length"].max()  
longest_artical = df[df["length"] == max_length]['title'].values[0]
print("Title of the longest article:", longest_artical)
#sum the length of longest articals
total_length = df["length"].sum()
print("total length of all articles:", total_length)
top20 = df.sort_values(by='length', ascending=False).head(20) #top20 longest articals
# Save to CSV
top20.to_csv("outputs/rubica-shah-top20.csv", index=False)
 
# new date column formatted as YYYY-MM-DD  
df["date"] = df["year"].astype(str) + "-" + df["month"].astype(str).str.zfill(2) + "-" + df["day"].astype(str).str.zfill(2) #learn from chatgpt
# Filter articles from the first 6 months of 2023
first_half_2023 = df[(df["year"] == 2023) & (df["month"] <6)]

# Export to CSV
first_half_2023.to_csv("outputs/rubica-shah-6m2023.csv", index=False)
