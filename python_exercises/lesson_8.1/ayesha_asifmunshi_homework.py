import re
import os

folder= 'aljazeera_articles'
filename= '2024-01-15_10035.txt'
file_path = f"{folder}/{filename}"

pattern=r'Gazan?'

with open(file_path, mode="r", encoding="utf8") as file:
    text = file.read()


splitter_pattern=r"\n+-+\n+"
split_text= re.split(splitter_pattern, text)
title=split_text[0]
print('title:', title)

matches=re.findall(pattern,title)
n_matches=len(matches)
print(f"the file {filename} contains {n_matches} matches for the regex {pattern}")
