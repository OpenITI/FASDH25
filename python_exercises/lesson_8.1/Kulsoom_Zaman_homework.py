import re

# Open a single article :
folder = "aljazeera_articles"
filename = "2024-01-15_10035.txt"
# Use an f string to combine the folder and filename variables into a path
file_path = f"{folder}/{filename}"
print(f"The path to the article is: {file_path}")


# load the text file into Python:
with open(file_path, mode="r", encoding="utf8") as file:
    text = file.read()
    
# Using a regular expression that will match both 'Gaza' and 'Gazan':
pattern = r"Gazan?"
matches = re.findall(pattern, text)
print(matches)
n_matches = len(matches)
print(n_matches)
print(f"There are {n_matches} of {pattern} in the article {filename}")

# Splitting the text
splitter_pattern= r"\n+-+\n+"
split_text= re.split(splitter_pattern, text)
title = split_text[0]
body= split_text[1]
print("title: ", title)
print("body: ", body)

# Using a regular expression that will match both 'Gaza' and 'Gazan' in the title only:
matches = re.findall(pattern, title)
n_matches = len(matches)
print(f"The file {filename} contains {n_matches} matches for the regex '{pattern}'.")
