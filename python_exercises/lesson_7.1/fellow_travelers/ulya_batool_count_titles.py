filename = "1332ShibliNucmani.SafarnamaRumMisrSham.FASDH2025019-urd1"
with open(filename, 'r', encoding='utf8') as file:
    lines = file.readlines()
    
for line in lines[:10]:
        print(line.strip())
heading_lines= []
for heading in lines:
    if "###" in heading:
       heading_lines.append(heading)
for heading in heading_lines[:3]:
    print(heading)
    
word_counts = []

for heading in heading_lines:
    print("Heading:", heading)  
    words = heading.split()  
    count_words = len(words)  
    word_counts.append(count_words)  
    print("Count of words in this heading:", count_words)

    for word in words:  
        print("Length of word:", word, len(word))
        
first_level_headings = []  

for heading in heading_lines:
    if heading.count("|") == 1:  
        first_level_headings.append(heading)  
print(first_level_headings)  
