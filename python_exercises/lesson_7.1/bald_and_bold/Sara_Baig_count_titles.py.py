filename = "1374SacadatHasanMantu.GanjayFarishtay.FASDH2025006-urd1"
with open(filename, 'r' , encoding='utf8') as file:
    lines = file.readlines()
    
#print(lines[:5])
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
    print("Count of the words in heading: ", count_words)
    
