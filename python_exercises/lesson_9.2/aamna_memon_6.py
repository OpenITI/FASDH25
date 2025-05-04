import re
import os

folder = "aljazeera_articles"  
gaz_path="gazetteers/geonames_gaza_selection.tsv"
with open(gaz_path, encoding="utf-8") as file:
    data = file.read()


rows = data.split('\n')
print (rows, '\n')

dictionary = {}

for row in rows[1:]:
    columns=row.split('\t')
    name=columns[0]
    print(name)
    dictionary[name]=0
print (dictionary)

print('-------------------------\n')

for filename in os.listdir(folder):
    file_path=f"{folder}/{filename}"
    print(f"The path to the article is {file_path}\n")

    with open(file_path, encoding="utf-8") as file:
        text = file.read()

    # find all the occurences of the patterns in the text:
    for pattern in dictionary:
        matches = re.findall(pattern, text)
        n_matches = len(matches)
        #print(n_matches, pattern)
        dictionary[pattern] += n_matches

       
for pattern in dictionary:
    count = dictionary[pattern]
    if count >=0:
        print(f"found {pattern} {count} times")
