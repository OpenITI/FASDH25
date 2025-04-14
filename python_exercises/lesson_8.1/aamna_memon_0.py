# Task 0. Open a single article
folder = "aljazeera_articles"
filename = "2024-03-28_9276.txt"
file_path = f"{folder}/{filename}"
print(f"The path to the article is: {file_path}")
print('---------------------------\n')


with open(file_path, mode="r", encoding="utf8") as file: #load the text file into Python
    text = file.read()
print(text[:100])                                        #print the first 100 characters
print('---------------------------\n')                   #of the text


import re
pattern=r"Israeli?"
matches= re.findall(pattern, text)
print(matches)
n_matches=len(matches)
print(f"{filename} contains {pattern} {n_matches} times in the article")
print('---------------------------\n')


splitter_pattern=r"\n+-+\n+"
split_text=re.split(splitter_pattern, text)
title=split_text[0]
body=split_text[1]

pattern=r"Israeli?"
matches=re.findall(pattern, body)
n_matches=len(matches)
print(f"{filename} contains {pattern} {n_matches} times in the body")

pattern=r"Israeli?"
matches= re.findall(pattern, title)
print(matches)
n_matches=len(matches)
print(f"{filename} contains {pattern} {n_matches} times in the title")

patterns=[r"Israeli?", r"Palestine|Palestinian", r"Gazan?"]
for pattern in patterns:
    matches=re.findall(pattern, body)
    print(matches)
    n_matches=len(matches)
    print(f"{filename} contains {pattern} {n_matches} times")
    
