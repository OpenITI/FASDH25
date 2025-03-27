# Import the regular expressions module
import re  

# Define folder and file name
folder = "aljazeera_articles"
filename = "2024-01-15_10035.txt"

# Create the file path using an f-string
file_path = f"{folder}/{filename}"


# load the text file into Python:
with open(file_path, mode="r", encoding="utf8") as file:
    text = file.read()

# Splitting the text in body and title using the provided pattern
splitter_pattern= r"\n+-+\n+"
split_text= re.split(splitter_pattern, text)
title = split_text[0]
body= split_text[1]

# Define the regular expression pattern to match 'Gaza' and 'Gazan'
pattern = r"Gazan?"
matches = re.findall(pattern, title)
print(matches)

# Match both 'Gaza' and 'Gazan' in the title only:
matches = re.findall(pattern, title)
n_matches = len(matches)
print(n_matches)
print(f"The file {filename} contains {n_matches} matches for the regex '{pattern}'.")
