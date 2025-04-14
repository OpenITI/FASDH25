'''This is your starting script for today's Python class.

In this Python class we will explore a collection of articles from
the website Al Jazeera English about Israel and Palestine.

You will find the articles in the "aljazeera_articles" subfolder.

The collection of articles we are going to look at is only a selection
of a larger dataset published by Inacio Vieira on Kaggle,
a repository for data and code for machine learning.
https://www.kaggle.com/datasets/inaciovieira/al-jazeera-english-israel-gaza-war-from-7th-oct-23

The selection criteria of the subset we are working on today are:
1. The articles were written from 2023 onwards
2. The articles contain at least 9 place names in Gaza

'''
import re
import os

# define which folder to use:
# NB: these are different articles than in the previous weeks
folder = "aljazeera_articles"  

# define the patterns we want to search:
path = "gazetteers/geonames_gaza_selection.tsv"
with open(path, encoding="utf-8") as file:
    data = file.read()

print(data)

patterns = {}
rows = data.split("\n")
print(rows)
for row in rows:
    columns = row.split("\t")
    name = columns[0]
    print(name)
    patterns[name] = 0

print(patterns)



    
for filename in os.listdir(folder):
    # build the file path:
    file_path = f"{folder}/{filename}"
    print(f"The path to the article is: {file_path}")

    # load the article (text file) into Python:
    with open(file_path, encoding="utf-8") as file:
        text = file.read()

    # find all the occurences of the patterns in the text:
    for pattern in patterns:
        matches = re.findall(pattern, text)
        n_matches = len(matches)
        patterns[pattern] += n_matches


for pattern in patterns:
    count = patterns[pattern]
    if count >= 1:
        print(f"found {pattern} {count} times")
    
