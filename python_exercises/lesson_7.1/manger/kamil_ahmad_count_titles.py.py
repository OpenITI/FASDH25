filename = "1350MirzaHadiyRuswa.AmrawJanAda.FASDH2025010-urdu1" 

with open(filename, 'r', encoding='utf8') as file:
    lines = file.readlines()

print("First 10 lines of the file:")
print("".join(lines[:10]))

word_counts = []
matching_lines = []

for heading in lines:
    if "###" in heading:
        matching_lines.append(heading.strip())

print("First 3 headings:")
print("\n".join(matching_lines[:3]))

for heading in matching_lines:
    print("heading:", heading)
    words = heading.split()
    count_words = len(words)
    word_counts.append(count_words)
    print("count of the words in heading:", count_words)

    print("Word lengths:", [len(word) for word in words])
    
first_level_headings = [heading for heading in matching_lines if heading.count('|') == 1]

print("\nFirst-level headings:")
print("\n".join(first_level_headings))
