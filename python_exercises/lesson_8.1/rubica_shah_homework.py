import re  # Import the regular expressions module

# Define the folder and filename
folder = "aljazeera_articles"
filename = "2024-01-15_10035.txt"

# Construct the full file path using an f-string
file_path = f"{folder}/{filename}"

# Open and read the file
with open(file_path, mode="r", encoding="utf8") as file:
    text = file.read()

# Split the text to extract the title (assuming the title is before the first separator)
splitter_pattern = r"\n+-+\n+"  # Regular expression for section breaks
split_text = re.split(splitter_pattern, text)

# Extract the title (first section of the article)
if split_text:  
    title = split_text[0]  # The title is assumed to be the first section
else:
    title = ""  # Set an empty string if the split fails

# Define the regular expression to match 'Gaza' and 'Gazan'
pattern = r"\bGaza\b|\bGazan\b"

# Find matches in the article title only
matches = re.findall(pattern, title)
n_matches = len(matches)  # Count the number of matches

# Print the output using an f-string
print(f"The file {filename} contains {n_matches} matches for the regex '{pattern}'.")
