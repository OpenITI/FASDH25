filename: "1350MirzaHadiyRuswa.AmrawJanAda.FASDH2025010-urdu1"
with open(filename , 'r', encoding='utf8')as file:
    lines = file.readlines()

matching_lines = []
for heading in lines:
    if "###" in headings:
        matching_lines.append(heading)

for heading in matching_lines[:3]:
    print(heading)

word_counts = []
for heading in matching_lines:
    print("\nCurrent headings: ", count_words)
    words = heading.split()
    count_words = len(words)
    print("Count of words in this line: ", count_words)
    word_counts.append(count_words)
    for word in words:
        print(len(words))
          
