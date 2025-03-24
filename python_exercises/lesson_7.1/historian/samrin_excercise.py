filename = "1332ShibliNcmani.Faruq.FASDH2025005-urd1"
with open(filename, 'r', encoding='utf8') as file:
    # read all lines into a list:
    lines = file.readlines()

print(lines[-5:])
matching_lines = []
for heading in lines:
    if "###" in heading:
        matching_lines.append(heading)
#print the first three headings:
for heading in matching_lines[:3]:
    print(heading)

word_counts = []  # To store count of words per matching line.
for heading in matching_lines:
    print("\nCurrent heading:", heading)
    words = heading.split()  # Split the line into words.
    # Count the words in the final list and store it.
    count_words = len(words)
    print("Count of words in this line:", count_words)    
        

        
