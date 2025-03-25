# Open and read the markdown file
file_path = "python_exercises/session7.1/Qudrat_ka_nizam/"

with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Print the first 10 lines
print("First 10 lines of the file:")
for line in lines[:10]:
    print(line.strip())

# Extract markdown headings (lines containing '###')
heading_lines = [line.strip() for line in lines if '###' in line]

# Print the first 3 headings
print("\nFirst 3 headings:")
for heading in heading_lines[:3]:
    print(heading)

# Count and print the number of words in each heading
print("\nWord count in each heading:")
for heading in heading_lines:
    word_count = len(heading.split())
    print(f"Count of words in this heading: {word_count}")

# Print the length of each word in each heading
print("\nLength of each word in each heading:")
for heading in heading_lines:
    words = heading.split()
    lengths = [len(word) for word in words]
    print(f"Heading: {heading}")
    print(f"Word lengths: {lengths}")

# Extract first-level headings (contain exactly one '|')
first_level_headings = [heading for heading in heading_lines if heading.count('|') == 1]

# Print first-level headings
print("\nFirst-level headings:")
for heading in first_level_headings:
    print(heading)

          
          
          
