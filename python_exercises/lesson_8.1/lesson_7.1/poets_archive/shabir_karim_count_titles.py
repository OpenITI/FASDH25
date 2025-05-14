filename = "7578_poets_archive.txt"
with open(filename, 'r', encoding='utf8')as file:
    line = file.readlines()

matching_lines = []
for heading in line:
    if "###" in heading:
        matching_lines.append(heading)
        
print("\nFirst three headings:")
for heading in matching_lines[:3]:
    print(heading)

word_counts = []
for heading in matching_lines:
    print("\nCurrent heading:", heading)
    words = heading.split()

    count_words = len(words)
    print("Count of words in this line:", count_words)
    word_counts.append(count_words)
    for word in words:
        print(len(word))
