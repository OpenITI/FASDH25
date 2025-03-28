import re  # Import the regular expressions module

# Define the file path
file_path = "../../aljazeera_articles/2024-01-15_10035.txt"  # Adjust path if needed

# Define the regex pattern to match 'Gaza' or 'Gazan'
pattern = r'\bGaza[n]?\b'

# Open the file and read its contents
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()  # Read all lines into a list

# Extract the article title (assuming it's in the first line)
title = lines[0].strip() if lines else ""

# Count the number of matches in the title
matches = len(re.findall(pattern, title))

# Print the output
print(f'The file {file_path} contains {matches} matches for the regex {pattern}.')

