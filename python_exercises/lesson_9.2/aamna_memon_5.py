import re
import os

folder = "aljazeera_articles"  
gazetteer_path="gazetteers/geonames_gaza_selection.tsv"

with open(gazetteer_path, encoding="utf-8") as file:
    data = file.read()
print(data,'\n')

print('------------------------------------------------')

dictionary= {r'Israeli?':0,
           r'Palestine|Palestinian':0,
           r'Gazan?':0}

for filename in os.listdir(folder):
    file_path = f"{folder}/{filename}"
    
    print(f"The path to the article is: {file_path}")
    

    with open(file_path, encoding="utf-8") as file:
        text = file.read()

    for pattern_key in dictionary:
        matches = re.findall(pattern_key, text)
        no_of_matches = len(matches)
        print(no_of_matches, pattern_key, '\n')
        dictionary[pattern_key] += no_of_matches
        
for pattern_key, count in dictionary.items():
    print(f"found {pattern_key} {count} times")

