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
filename = "2024-03-28_9276.txt"


patterns = [r"Israel\b", r"Palestine|Palestinian", r"Gazan?"]

total = [0,0,0]

for filename in os.listdir(folder):
    # build the file path:
    #file_path = f"{folder}/{filename]"
    file_path = os.path.join(folder, filename)
    file_path = f"{folder}/{filename}"
    print(f"The path to the article is: {file_path}")

    # load the article (text file) into Python:
    with open(file_path, encoding="utf-8") as file:
        text = file.read()

    # load the article (text file) into Python:
    with open(file_path, encoding="utf-8") as file:
        text = file.read()

    # find all the occurences of Israel or Israeli in the text:
    #for pattern in patterns:
    for pattern_number in range(len(patterns)):
        pattern = patterns[pattern_number]
        print(pattern_number, pattern)
        matches = re.findall(pattern, text)
        n_matches = len(matches)
        print(f"{filename} contains {pattern} {n_matches} times in the article")
        total[pattern_number] += n_matches

print(f"we found {total} matches in the corpus!")
for pattern_number in range(len(patterns)):
        pattern = patterns[pattern_number]
        n_times = total[pattern_number]
        print(f"we found {pattern} {n_times} times")
