filename = "1374SacadatHasanMantu.MantuKaySawBhatrinAfsanay.FASDH2025002-urd1.txt"
with open(filename, 'r', encoding='utf8') as file:
    lines = file.readlines()
matching_lines = []
for headings in lines:
    if "###" in headings:
        matching_lines.append(headings)
        
for heading in matching_lines[:3]:
    print(heading)

words_counts = []
for heading in matching_lines:
          word = heading.split()
          count_words = len(word)
          print("count of words in this line;", count_words)

