filename = "1350MirzaHadiyRuswa.AmrawJanAda.FASDH2025010-urdu1"
with open(filename, "r", encoding="utf-8") as file:
    lines = file.readlines()

print("First 10 lines of the file:")
print("".join(lines[:10]))

heading_lines = [line.strip() for line in lines if '###' in line]

print("First 3 headings:")
print("\n".join(heading_lines[:3]))

print("\nWord count in each heading:")
word_counts = []
for heading in heading_lines:
    words = heading.split()
    count_words = len(words)
    word_counts.append(count_words)
    print(f"Count of words in this heading: {count_words}")

    print("Word lengths:", [len(word) for word in words])

first_level_headings = [heading for heading in heading_lines if heading.count('|') == 1]

print("\nFirst-level headings:")
print("\n".join(first_level_headings))
