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

The goal for today's class it to find out how many times
place names like Israel, Gaza, and Palestine are mentioned
in these articles.
'''
import re

# Task 0. Open a single article :

folder = "aljazeera_articles"
filename = "2024-03-28_9276.txt"

# EXERCISE: use an f string to combine the folder and filename variables into a path
#           (remember: a path uses slashes "/" to separate file and folder names)
# NB: you HAVE to use the variable names,
#     DO NOT write f"aljazeera_articles/2024-04-18_406.txt"

file_path = f"{folder}/{filename}"

print(f"The path to the article is: {file_path}")

# load the text file into Python:
with open(file_path, mode="r", encoding="utf8") as file:
    text = file.read()

# EXERCISE: print the first 100 characters of the text:
print(text[:100])

pattern = r"Israeli?"
matches = re.findall(pattern, text)
print(matches)
n_matches = len(matches)
print(n_matches)
