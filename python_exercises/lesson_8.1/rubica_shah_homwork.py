
import re
# Define the folder and filename
folder = "aljazeera_articles"
filename = "2024-01-15_10035.txt"


# load the text file into Python:# Open the file '2024-01-15_10035.txt' in read mode and read its contents
with open('aljazeera_articles/2024-01-15_10035.txt', mode="r", encoding="utf8") as file:
    text = file.read()
# Define the regular expression pattern that matches both 'Gaza' and 'Gazan'

pattern = r"Gazan?"

# Search for matches in the article title only (assuming title is the first line

splitter_pattern = r"\n+-+\n+"
split_text = re.split(splitter_pattern, text)
title = split_text[0]# Get the first line as the title
# Search for matches in the article title only (assuming title is the first line)

matches = re.findall(pattern, title)  # Find all matches of the pattern in the title
 
print(f"The file 2024-01-15_10035.txt contains {len(matches)} matches for the regex {pattern}.")




