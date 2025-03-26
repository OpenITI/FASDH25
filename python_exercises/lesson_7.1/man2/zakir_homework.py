filename = '1374SacadatHasanMantu.Katari.FASDH2025015-urd1.'
with open(filename, 'r', encoding= 'utf8')as file:
    lines = file.readlines()
print("First 10 lines:")
for line in lines[:10]:
    print(line, end ="")# used end= "" so the lines are printed as they are keeping spaces and newlines. 
print("")# for separating outputs and clarity

#2. Create a new list, “heading_lines” and, using the list of lines add to the “heading_lines” list only lines that are mARkdown headers (i.e. lines that contain ‘###’). Using the new list, print the first 3 headings.
heading_lines = []
for line in lines:
    if '###' in line:
        heading_lines.append(line)

print("First 3 headings:")
for heading in heading_lines[:3]:
    print(heading, end ="")# again using end ="" so the lines are printed as they are keeping spaces and newlines)
print("")# for separating outputs and clarity

#3. Using the list of heading_lines created in step 2, count the number of words in each heading. For each heading, print: “Count of words in this heading:” plus the word count (e.g. “Count of words in this line: 10”)
print("Word count in each heading:")
for heading in heading_lines:
    words = heading.split()
    print("Count of words in this heading:", len(words))
print("")# for separating outputs and clarity

#4. Building on the loop that you will have used to solve exercise 3, write the code that would print the length of each word in each heading (for this you will need to use a nested loop).
print("Length of each word in each heading:")
for heading in heading_lines:
    words = heading.split()
    print("Heading:", heading)
    for word in words:
        print("  ", word, "-", len(word), "characters")
print("")# for separating outputs and clarity

#5. Create a new list, “first_level_headings”. Then loop through the heading_lines list, and add only those lines to the first_level_headings list that contain exactly one pipe (“|”). (hint: you can use the string’s count() method to count the number of pipes in the heading). Finally, print the first_level_headings list.
first_level_headings = []
for heading in heading_lines:
    if heading.count("|") ==1:
        first_level_headings.append(heading)
