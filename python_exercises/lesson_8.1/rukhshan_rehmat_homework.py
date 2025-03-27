import re # Importing the Regex (regular expressions) library

folder = "aljazeera_articles" # Folder where the file is located
filename = "2024-01-15_10035.txt" # Name of the file
file_path = f"{folder}/{filename}" # Creating the full file path
# Opening the file in read mode with UTF-8 encoding
with open(file_path, mode="r", encoding="utf8") as file: 
    text = file.read() # Reading the entire file content into the variable 'text'

pattern = r"Gazan?" # Regex pattern: Matches "Gaza" or "Gazan"

splitter_pattern = r"\n+-+\n+"   # Pattern that identifies the separator
split_text = re.split(splitter_pattern, text)  # Splitting text at the separator to extract the title 
title = split_text[0] # The first part of the split text is assumed to be the article title
matches = re.findall(pattern, title) # Searching for occurrences of 'Gaza' or 'Gazan' in the title
n_matches = len(matches) # Counting the number of matches found

print(f"The file {filename} contains {n_matches} matches for the regex '{pattern}'.") # Prints the output in the required format
