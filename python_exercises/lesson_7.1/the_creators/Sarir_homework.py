filename = "1330DiptiNazirAhmad.MiratCurus.FASDH2025014-urd1"
with open(filename, 'r', encoding='utf8') as file:
    line = file.readlines()
    print(line[:10])
word_counts=[]
heading_lines= []
first_level_headings= []
for heading in line:
    if "###" in heading:
        heading_lines.append(heading)
        print(heading)
        print(heading_lines[:3])

for heading in heading_lines:
    print("heading:", heading)
    words=heading.split()
    count_words =len(words)
    print("count of the words in heading: ", count_words)

for heading in heading_lines:
    if heading.count("|") == 1:
        first_level_headings.append(heading)
        print("\nFirst Level Headings:")

for heading in first_level_headings:
    print(heading.strip())
