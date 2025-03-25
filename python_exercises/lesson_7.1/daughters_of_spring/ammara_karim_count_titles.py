filename= "1184MirAmmann.BaghBahar.FASDH2025003-urd1"
with open(filename, 'r' , encoding='utf8') as file:
    lines=file.readlines()
    print(lines)
print(lines[:5])
word_counts = []
matching_lines = []
for heading in lines:
    if "###" in heading:
        print(heading)
        matching_lines.append(heading)

#print(matching_lines[:5])

for heading in matching_lines:
    print("heading: ", heading)
    words = heading.split()
    count_words = len(words)
    print("count of the words in heading; ", count_words)
