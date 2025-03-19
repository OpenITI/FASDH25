filename = "1330NazirAhmad.TawbaNasuha.FASDH2025016-urd1"
with open(filename, 'r', encoding='utf8') as file:
    lines = file.readlines()
    print(lines)
print(lines[:5])

matching_lines = []
for heading in lines:
    if "###" in heading:
        matching_lines.append(heading)
        print(heading)

print(matching_lines[:5])

for heading in matching_lines:
    print("heading: ", heading)
    words = heading.split()
    count_words = len(words)
    print("Count of the words in heading: ", count_words)
