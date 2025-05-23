import os
import re

folder= "aljazeera_articles"
filename= "2024-01-15_10035.txt"

file_path= f"{folder}/{filename}"

pattern=r"Gazan?"

with open(file_path, mode="r", encoding="utf8") as file:
    text = file.read()

splitter_pattern= r"\n+-+\n+"
split_text = re.split(splitter_pattern, text)
title = split_text[0]
body = split_text[1]

matches= re.findall(pattern,title)

n_matches = len(matches)

print("Title: ",title)
print(f"The file {filename} contains {n_matches} matches for the regex {pattern}.")
