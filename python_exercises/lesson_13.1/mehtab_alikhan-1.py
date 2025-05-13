import os
import pandas as pd

df = pd.read_csv('data/title.csv')

print(df['title'])

longest = df['title'].str.len().idxmax()
print("Longest title:", df.loc[longest, 'title'])

print("Total length of all titles:", df['title'].str.len().sum())

