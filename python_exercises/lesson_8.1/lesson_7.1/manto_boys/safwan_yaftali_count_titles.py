
filename = "1374SacadatHassanMantu.Anarkly.FASDH2025020-urd1"

with open(filename, 'r', encoding='utf8') as file:
    lines = file.readlines()

print("First 10 lines:")
print(lines[:10])

# Filter lines that contain ###
heading_lines = []
for heading in lines:
    if "###" in heading:
        heading_lines.append(heading)

print("First 3 headings:")
print(heading_lines[:3])

word_counts = []
for heading in heading_lines:
    print("\nCurrent heading:", heading)
    words = heading.split()
    count_words = len(words)
    print("Count of words in this heading:", count_words)
    word_counts.append(count_words)
    for word in words:
        print(len(word))

first_level_headings = []
for heading in heading_lines:
    if heading.count('|') == 1:
        first_level_headings.append(heading)

print("\nFirst-level headings:")
print(first_level_headings)
