import re
# Task 0. Open a single article :

folder = "aljazeera_articles"
filename = "2024-01-15_10035.txt"


file_path = f"{folder}/{filename}"

print(f"The path to the article is: {file_path}")


# load the text file into Python:
with open(file_path, mode="r", encoding="utf8") as file:
    text = file.read()

# EXERCISE: print the first 100 characters of the text:
print(text[:100])

pattern = r"Israeli?"
matches = re.findall(pattern, text)
print(matches)
n_matches = len(matches)
print(n_matches)
print(f"There are {n_matches} of {pattern} in the atricle {filename}")



splitter_pattern = r"\n+-+\n+"
split_text = re.split(splitter_pattern, text)
title = split_text[0]
body = split_text[1]
#print("title: ", title)
#print("body: ", body)

matches = re.findall(pattern, text)
n_matches = len(matches)
print(f"There are {n_matches} of {pattern} in the article text {filename}")

matches = re.findall(pattern, body)
n_matches = len(matches)
print(f"There are {n_matches} of {pattern} in the article body {filename}")

matches = re.findall(pattern, title)
n_matches = len(matches)
print(f"There are {n_matches} of {pattern} in the article title {filename}")
