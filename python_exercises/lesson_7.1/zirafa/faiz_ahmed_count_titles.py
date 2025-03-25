filename= "1285Ghalib.Diwan.FASDH2025021-urd1"
with open(filename, 'r', encoding='utf8') as file:
    lines= file.readlines()
    print(lines)
print(lines[:5])

matching_lines=[]
for heading in lines:
    if '###' in heading:
        matching_lines.append(heading)
        print(heading)

word_counts=[]
for heading in matching_lines:
    print('Current Heading;', heading)
    words = heading.split()
    count_words= len(words)
    print('count words in this line;', count_words)
