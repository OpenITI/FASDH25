filename = "1285Ghalib.Diwan.FASDH2025021-urd1"
with open(filename, 'r', encoding='utf8')as file:
    line = file.readlines()
    print(line[:10])

matching_lines = []
for heading in line:
    if "###" in heading:
        matching_lines.append(heading)
        
print("\nFirst three headings:")
for heading in matching_lines[:3]:
    print(heading)

word_counts = []
for heading in matching_lines:
    print("\nCurrent heading:", heading)
    words = heading.split()

    count_words = len(words)
    print("Count of words in this line: 10", count_words)
    word_counts.append(count_words)
    for word in words:
        print(f"Length of '{word}': {len(word)}")

first_level_headings = [heading for heading in matching_lines if heading.count("|") == 1]
print("\nFirst-level headings (contain exactly one '|'):")
print(first_level_headings)
