filename= "middle_ground.txt"
with open(filename, 'r', encoding='utf-8') as file:
    lines= file.readlines()
matching_lines= []
for heading in lines:
        if "###" in heading:
            matching_lines.append(heading) 
for heading in matching_lines[:3]:
    print(heading)

word_count= []
for heading in matching_lines:
    word= heading.split()
    count_words= len(word)
    print("count words in this line;", count_words)
