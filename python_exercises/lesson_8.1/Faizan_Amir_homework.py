import re  # Import the regular expressions module

# Define the folder and filename
folder = "aljazeera_articles"
filename = "2024-01-15_10035.txt"

# Create the file path using an f-string
file_path = f"{folder}/{filename}"

# Open the file and read its contents into the variable 'text'
with open(file_path, mode="r", encoding="utf8") as file:
    text = file.read()

# Define the regular expression pattern to match 'Gaza' and 'Gazan'
pattern = r"Gaza[n]?"

# Split the text into title and body using the provided pattern
splitter_pattern = r"\n+-+\n+"  # Matches a line of hyphens separating sections
split_text = re.split(splitter_pattern, text)

title = split_text[0]  # Extract the title from the first section

# Search for matches in the title only
matches = re.findall(pattern, title)
n_matches = len(matches)  # Count the number of matches

# Print the formatted output
print(f"The file {filename} contains {n_matches} matches for the regex {pattern}.")
