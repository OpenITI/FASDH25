
filename = "1184MirAmmann.BaghBahar.FASDH2025003-urd1"
with open(filename, "r", encoding="utf8") as file:
    lines = file.readlines()

print("\nFirst 10 lines of the file:")
print("".join(lines[:10]))  

heading_lines = [line.strip() for line in lines if "###" in line]

print("\nFirst 3 headings:")
print("\n".join(heading_lines[:3]))

print("\nWord count in each heading:")
for heading in heading_lines:
    words = heading.split()
    count_words = len(words)
    print(f"\nCurrent heading: {heading}")
    print(f"Count of words in this heading: {count_words}")
    
    print("Lengths of words in this heading:", [len(word) for word in words])

first_level_headings = [heading for heading in heading_lines if heading.count("|") == 1]


print("\nFirst-level headings:")
print("\n".join(first_level_headings))

