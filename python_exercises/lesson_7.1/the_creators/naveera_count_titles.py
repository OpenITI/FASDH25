filename = "1330DiptiNazirAhmad.MiratCurus.FASDH2025014-urd1"
with open(filename, 'r', encoding='utf8') as file:
    lines = file.readlines()
    print(lines[:5])
#print(lines[:5])

matching_lines =[]
for heading in lines:
    if "###" in heading:
        matching_lines.append(heading)
        print(heading)
        print(matching_lines[:5])
#print(matching_lines[:5])

for heading in matching_lines:
    print("heading: ", heading)
    words = heading.split()
    count_words = len(words)
    print("Count of the words in heading ", count_words)
    
