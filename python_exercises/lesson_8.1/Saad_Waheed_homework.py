import re  # Import the regular expressions module

# Define the folder and filename where the article is stored
folder = "aljazeera_articles"
filename = "2024-01-15_10035.txt"

# Construct the full file path
file_path = f"{folder}/{filename}"

# Define the regex pattern to match 'Gaza' and 'Gazan' (with word boundaries for accuracy)
pattern = r"Gazan?"

# Open the file and read its content
with open(file_path, mode="r", encoding="utf-8") as file:
    text = file.read()  # Load the entire text file into a Python variable

# Define the splitter pattern to separate title and body using a dashed line separator
splitter_pattern = r"\n+-+\n+"
split_text = re.split(splitter_pattern, text)  # Split the text into title and body

# Extract the title (first section of the split text) and body (second section if available)
title = split_text[0]  
body = split_text[1] 

# Search for occurrences of the pattern in the title
matches = re.findall(pattern, title)
n_matches = len(matches)  # Count how many times the pattern appears in the title

# Print the output in the specified format using an f-string
print(f"This file {filename} contains {n_matches} matches for the regex '{pattern}' in the article's title.")
