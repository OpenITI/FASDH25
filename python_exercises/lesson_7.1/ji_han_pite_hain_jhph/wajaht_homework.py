import os

# Correct file path
filename = r"C:\Users\Dell\Downloads\FASDH25\python_exercises\lesson_7.1\ji_han_pite_hain_jhph\1382ShawkatThanwi.JiHanPitayHayn.FASDH2025013-urd1"

# Open and read the markdown file
with open(filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()  # Load the text as a list of lines
# Print the first 10 lines
print("First 10 lines of the file:")
for line in lines[:10]:
    print(line.strip())
# Step 2: Extract markdown headings (lines containing '###')
heading_lines = [line.strip() for line in lines if '###' in line]
# Print the first 3 headings
print("\nFirst 3 markdown headings:")
for heading in heading_lines[:3]:
    print(heading)
# Step 3: Count the number of words in each heading
print("\nWord count in each heading:")
for heading in heading_lines:
    word_count = len(heading.split())  # Split by spaces to count words
    print(f"Count of words in this heading: {word_count}")
# Step 4: Print the length of each word in each heading
print("\nLength of each word in each heading:")
for heading in heading_lines:
    words = heading.split()
    word_lengths = [len(word) for word in words]
    print(f"Heading: {heading}")
    print(f"Word lengths: {word_lengths}")
# Step 5: Extract first-level headings (containing exactly one '|')
first_level_headings = [heading for heading in heading_lines if heading.count('|') == 1]
# Print first-level headings
print("\nFirst-level headings (containing exactly one '|'):")
for heading in first_level_headings:
    print(heading)
