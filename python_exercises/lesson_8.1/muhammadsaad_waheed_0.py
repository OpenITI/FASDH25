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

# Define the folder and filename
folder = "aljazeera_articles"
filename = "2024-03-28_9276.txt"

# Combine them into a file path
file_path = f"{folder}/{filename}"

# Load the text file
with open(file_path, mode="r", encoding="utf8") as file:
    text = file.read()

# Define regex pattern (case insensitive)
pattern = r"Israeli?"  # Matches "Israel" and "Israeli"

# Count occurrences
count = len(re.findall(pattern, text, re.IGNORECASE))

# Print result
print(f"Israel/Israeli: {count}")
