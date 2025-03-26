import re

#Opening the file: 2024-01-15_10035.txt

folder = "aljazeera_articles"
filename = "2024-01-15_10035.txt"

#Creating the file path:

file_path = f"{folder}/{filename}"
print(f"The path to the article is: {file_path}")
 
#loading the text file into python:
with open(file_path, mode='r', encoding="utf8") as file:
      text = file.read()

#split title from body using regular expressions
splitter_pattern = r"\n+-+\n+"
split_text = re.split(splitter_pattern, text)
title = split_text[0]
body = split_text[1]
print("title: ", title)
print("body: ", body)

# using the regular expression to see occurrences of 'Gazan' and 'Gaza' and searching for their matches:
pattern = r"Gazan?"
matches = re.findall(pattern, body)
print(matches)
n_matches = len(matches)
print(n_matches)
print(f"{filename} contains {pattern} {n_matches} matches for the regex '{pattern}'.")

