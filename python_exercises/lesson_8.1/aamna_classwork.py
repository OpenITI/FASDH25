# Task 0. Open a single article
folder = "aljazeera_articles"
filename = "2024-03-28_9276.txt"
file_path = f"{folder}/{filename}"
print(f"The path to the article is: {file_path}")
print('---------------------------\n')


with open(file_path, mode="r", encoding="utf8") as file:
    text = file.read()         
print(text[:100])
print('---------------------------\n')          


import re

pattern=r"Israeli?"                           #PRINT ALL THE MATCHES FOR
matches= re.findall(pattern, text)            #ISRAEL & ISRAELI 
print(matches)                                
print('---------------------------\n')



                            
n_matches=len(matches)                        #COUNT THE MATCHES (Output=54)         
print(f"{filename} contains {pattern} {n_matches} times in the article/text")
print('---------------------------\n')


splitter_pattern=r"\n+-+\n+"                    #this specific pattern is looking for
split_text=re.split(splitter_pattern, text)     #one or more newlines, followed by
title=split_text[0]                             #one or more hyphens, followed by
body=split_text[1]                              #one or more newlines.

print('TITLE OF THE ARTICLE:', title)
print('BODY OF THE ARTICLE:', body)
print('---------------------------\n')



matches=re.findall(pattern, body)               #FIND ONE PATTERN IN BODY (output=52)
n_matches=len(matches)
print(f"{filename} contains {pattern} {n_matches} times in the body")
print('---------------------------\n')



matches= re.findall(pattern, title)             #FIND ONE PATTERN IN TITLE (output=2)
n_matches=len(matches)
print(f"{filename} contains {pattern} {n_matches} times in the title")
print('---------------------------\n')



patterns=[r"Israeli?", r"Palestine|Palestinian", r"Gazan?"]
for pattern in patterns:                        #FIND ONE+ PATTERN(S) IN TEXT
    matches=re.findall(pattern, text)
    n_matches=len(matches)
    print(f"{filename} contains {pattern} {n_matches} times in the text")
