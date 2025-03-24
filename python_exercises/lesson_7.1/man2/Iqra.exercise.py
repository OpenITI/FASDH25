filename = "1374SacadatHasanMantu.Katari.FASDH2025015-urd1."
with open(filename, 'r', encoding='utf8') as file:
    lines = file.readlines()
    print (lines)
    
print(lines[:5])
matching_lines = []
for heading in lines:
    if "### | " in heading:
        print(heading)
        matching_lines.append(heading)
        
print(matching_lines[:5])

word_counts = []
for heading in matching_lines:
    print("Current heading:", heading)
    words = heading.split()
    count_words = len(words)
    print("Count of words in this line:", count_words)
