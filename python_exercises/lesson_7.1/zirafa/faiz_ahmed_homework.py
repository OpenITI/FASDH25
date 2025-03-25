#Excercise 1
markdown_file='1285Ghalib.Diwan.FASDH2025021-urd1'
with open(markdown_file,'r', encoding='utf8') as file:
    lines = file.readlines()
for line in lines[:10]:
    print(line.strip())

#Excercise 2
heading_lines = [line.strip() for line in lines if "###" in line]
print("First 3 headings:")
for heading in heading_lines[:3]:
    print(heading)

#Excercise 3
print("Word count for each heading:")
for heading in heading_lines:
    word_count = len(heading.split())  
    print(f"Count of words in this heading: {word_count}")

#Excercise 4
print("Word lengths in each heading:")
for heading in heading_lines:
    print(f"Heading: {heading}")  
    words = heading.split() 
    print("Word lengths:", end=" ") 
    for word in words:
         print(len(word), end=" ")  
    print()  

#Excercise 5
first_level_headings = [heading for heading in heading_lines if heading.count("|") == 1]

print("First-level headings:")
print(first_level_headings)
