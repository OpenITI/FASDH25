with open("1350MirzaHadiyRuswa.AmrawJanAda.FASDH2025010-urdu1", "r", encoding="utf-8") as file:
    lines = file.readlines()


print("First 10 lines:")
print("".join(lines[:10]))


heading_lines = [line.strip() for line in lines if "###" in line]


print("\nFirst 3 headings:")
print("\n".join(heading_lines[:3]))


print("\nWord count in each heading:")
for heading in heading_lines:
    word_count = len(heading.split())
    print(f"Count of words in this heading: {word_count}")


print("\nWord lengths in each heading:")
for heading in heading_lines:
    word_lengths = [len(word) for word in heading.split()]
    print(f"Heading: {heading}")
    print(f"Word lengths: {word_lengths}")

first_level_headings = [heading for heading in heading_lines if heading.count("|") == 1]


print("\nFirst-level headings:")
print("\n".join(first_level_headings))
