filename = "1285Ghalib.Diwan.FASDH2025021-urd1"
with open(filename, 'r' , encoding='utf8') as file:
    lines = file.readlines()
    print(lines)
#print(lines[:5])


matching_lines = []
for heading in lines:
    if '###' in heading:
        #print(heading)
        matching_lines.append(heading)
        
#print(matching_lines[:5])

for heading in matching_lines:
    print("current heading: ", heading)
    words = heading.split()
    count_words = len(words)
    print("count of the words in heading: ", count_words)
