filename = "1330DiptiNazirAhmad.MiratCurus.FASDH2025014-urd1"
with open(filename, 'r', encoding='utf8') as file:
    line = file.readlines()
    print(line[:5])
word_counts=[]
matching_lines= []
for heading in line:
    if "###" in heading:
        matching_lines.append(heading)
        print(heading)
        print(matching_lines[:5])

for heading in matching_lines:
    print("heading:", heading)
    words=heading.split()
    count_words =len(words)
    print("count of the words in heading: ", count_words)
    
