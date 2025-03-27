import re  # Imports re module for regular expressions

# Define folder and filename
folder = "aljazeera_articles"
filename = "2024-01-15_10035.txt"

# Create full file path
file_path = f"{folder}/{filename}"

# Open the file and read its content
with open(file_path, mode="r", encoding="utf8") as file:
    text = file.read()  # Reads the entire content of the file into "text"

# Define the regular expression to match 'Gaza' and 'Gazan'
pattern = r"\bGaza\b|\bGazan\b"

# Split the text into title and body based on a separator pattern
splitter_pattern = r"\n+-+\n+"  # Detects separators like "----" between title and body
split_text = re.split(splitter_pattern, text)

# Extract the title and body safely
title = split_text[0] if len(split_text) > 0 else ""  # First part as title
body = split_text[1] if len(split_text) > 1 else ""  # Second part as body

# Find all occurrences of the pattern in the title
matches = re.findall(pattern, title)
n_matches = len(matches)  # Count the number of matches in the title

# Print output using an f-string
print(f"The file {filename} contains {n_matches} matches for the regex '{pattern}'.")
