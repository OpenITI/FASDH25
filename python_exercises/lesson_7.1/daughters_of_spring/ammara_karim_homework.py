


with open("1184MirAmmann.BaghBahar.FASDH2025003-urd1", "r", encoding="utf-8") as file:
    lines = file.readlines()

print("First 10 lines of the file:")
for line in lines[:10]:
    print(line.strip())

heading_lines = [line.strip() for line in lines if "### " in line]

print("\nFirst 3 markdown headings:")
for heading in heading_lines[:3]:
    print(heading)

print("\nWord count for each heading:")
for heading in heading_lines:
    word_count = len(heading.split())
    print(f"Count of words in this heading: {word_count}")

print("\nLength of each word in each heading:")
for heading in heading_lines:
    words = heading.split()
    word_lengths = [len(word) for word in words]
    print(f"Heading: {heading}")
    print("Word lengths:", word_lengths)

first_level_headings = [line for line in heading_lines if line.count("|") == 1]

print("\nFirst-level headings:")
for heading in first_level_headings:
    print(heading)
