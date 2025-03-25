filename = "1330NazirAhmd.IbnWaqt.FASDH2025007-urd1.txt"
with open(filename, 'r', encoding='utf8') as file:
    lines = file.readlines()
    
matching_lines = []
for heading in lines:
    if "###" in heading:
        matching_lines.append(heading)
print("\nFirst three headings: ")
for heading in matching_lines[:3]:
    print(heading)

word_counts = []
for heading in matching_lines:
    print("\nCurrent heading:", heading)
    words = heading.split()

count_words = len(words)
print("Count of words in this line:", count_words)
word_counts.append(count_words)
for word in words:
          print(len(word))
          
    
