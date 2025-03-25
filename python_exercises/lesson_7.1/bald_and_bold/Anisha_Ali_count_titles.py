with open("1374SacadatHasanMantu.GanjayFarishtay.FASDH2025006-urd1", 'r', encoding='utf8') as file:  
    lines = file.readlines()

matching_lines = []

for heading in lines:
    if "###" in heading:
       matching_lines.append(heading)  


for heading in matching_lines[:3]:  
    print(heading)

word_counts = []  # To store count of words per matching line.
for heading in matching_lines:
    print("\nCurrent heading:", heading)
    words = heading.split()  # Split the line into words.
    # Count the words in the final list and store it.
    count_words = len(words)
    print("Count of words in this line:",count_words)
