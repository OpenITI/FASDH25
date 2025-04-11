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
# Import the regular expressions module
import re  

# Define folder and file name
folder = "aljazeera_articles"
filename = "2024-01-15_10035.txt"

# Create the file path using an f-string
file_path = f"{folder}/{filename}"


# load the text file into Python:
with open(file_path, mode="r", encoding="utf8") as file:
    text = file.read()

# Splitting the text in body and title using the provided pattern
splitter_pattern= r"\n+-+\n+"
split_text= re.split(splitter_pattern, text)
title = split_text[0]
body= split_text[1]

# Define the regular expression pattern to match 'Gaza' and 'Gazan'
pattern = r"Gazan?"
matches = re.findall(pattern, title)
print(matches)

# Match both 'Gaza' and 'Gazan' in the title only:
matches = re.findall(pattern, title)
n_matches = len(matches)
print(n_matches)
print(f"The file {filename} contains {n_matches} matches for the regex '{pattern}'.")
