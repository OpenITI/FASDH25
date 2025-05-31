import pandas as pd

df = pd.read_csv("data/title.csv")

print(df['title'])

longest = df['title'].str.len().idxmax()
print("longest title:", df.loc[longest, 'title'])
