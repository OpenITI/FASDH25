filename = "1225MirTqyMir.DianMir.FASDH2025018-urd1"
with open(filename, "r", encoding="utf8") as file:
    lines = file.readlines()

heading_lines = [line.strip() for line in lines if "###" in line]

print("\nFirst 3 headings:")
print("\n".join(heading_lines[:3]))

word_counts = []
print("\nWord count in each heading:")
for heading in heading_lines:
    print("\nCurrent heading:", heading)
    words = heading.split()
    count_words = len(words)
    print("Count of words in this line:", count_words)
    word_counts.append(count_words)
    for word in words:
        print(len(word))

first_level_headings = [heading for heading in heading_lines if heading.count("|") == 1]

print("\nFirst-level headings:")
print("\n".join(first_level_headings))
