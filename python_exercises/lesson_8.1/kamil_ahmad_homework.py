import re

#Open the file: 2024-01-15_10035.txt

folder = "aljazeera_articles"
filename = "2024-01-15_10035.txt"

#Combining the folder and filename to create a path

file_path = f"{folder}/{filename}"

print(f"The path to the article is: {file_path}")

#loading the text file into Python:
with open(file_path, mode="r", encoding="utf8") as file:
    text = file.read()

#Splitting the text into title and body through the separator 
splitter_pattern = r"\n+-+\n+"
split_text = re.split(splitter_pattern, text)
title = split_text[0]
body = split_text[1]
print("title: ", title)
print("body: ", body)

#Regular expression to match both 'Gaza' and 'Gazan' and searching for matches
pattern = r"Gazan?"
matches = re.findall(pattern, title)
print(matches)
n_matches = len(matches)
print(n_matches)
print(f"The file {filename} contains {n_matches} matches for the regex '{pattern}'.")

