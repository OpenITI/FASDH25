 
import re

# Open the file '2024-01-15_10035.txt' in read mode and read its contents
with open('aljazeera_articles/2024-01-15_10035.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Define the regular expression pattern that matches both 'Gaza' and 'Gazan'
pattern = r'Gaza[n]?'

# Search for matches in the article title only (assuming title is the first line)
title = text.split('\n')[0]  # Get the first line as the title
matches = re.findall(pattern, title)  # Find all matches of the pattern in the title
 
print(f"The file 2024-01-15_10035.txt contains {len(matches)} matches for the regex {pattern}.")
