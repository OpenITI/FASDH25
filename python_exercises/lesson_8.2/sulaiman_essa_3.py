'''This is your starting script for today's Python class.

In this Python class we will explore a collection of articles from
the website Al Jazeera English about Israel and Palestine.

You will find the articles in the "aljazeera_articles" subfolder.

The collection of articles we are going to look at is only a selection
of a larger dataset published by Inacio Vieira on Kaggle,
a repository for data and code for machine learning.
https://www.kaggle.com/datasets/inaciovieira/al-jazeera-english-israel-gaza-war-from-7th-oct-23

The selection criteria of the subset we are working on today are:
1. The articles were written from 7 October 2023 onwards
2. The articles are at least 15Kb in size

The goal for today's class is to find out how many times
place names like Israel, Gaza, and Palestine are mentioned
in these articles.
'''
import re
import os

# define which folder and filename to use:
folder = "aljazeera_articles"

patterns = [r"Israeli?", r"Palestine|Palestinian", r"Gazan?"]
total = 0
for filename in os.listdir(folder):

    # build the file path:
    file_path = f"{folder}/{filename}"
    print(f"The path to the article is: {file_path}")

    # load the article (text file) into Python:
    with open(file_path, encoding="utf-8") as file:
        text = file.read()

    # find all the occurences of Israel or Israeli in the text:
    for pattern in patterns:
        matches = re.findall(pattern, text)
        n_matches = len(matches)
        print(f"{filename} contains {pattern} {n_matches} times in the article")
        total += n_matches
        print(f"until now we dound {total} matches")

print(f"Found {total} matches in the whole corpus")

