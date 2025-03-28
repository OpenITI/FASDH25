import re

folder = "aljazeera_articles"
filename = "2024-01-15_10035.txt"

file_path = f"{folder}/{filename}"   #it will open the file

with open(file_path, mode="r", encoding="utf-8") as file:
    text = file.read()             #it will loads the text file in python

pattern = r"Gazan?"
matches = re.findall (pattern, text)
print(matches)

splitter_pattern=r"\n+-+\n+"
split_text= re.split(splitter_pattern, text)    # this will split the text in to body
title=split_text[0]
body=split_text[1]

matches = re.findall(pattern, title)
print(matches)
n_matches=len(matches)
print(n_matches)
print(f"This file {filename} contains {n_matches} of {pattern} in the article's title.")
