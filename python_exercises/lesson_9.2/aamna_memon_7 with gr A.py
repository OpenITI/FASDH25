import re
import os

folder = "aljazeera_articles"  
gaz_path="gazetteers/geonames_gaza_selection.tsv"
with open(gaz_path, encoding="utf-8") as file:
    data = file.read()


rows = data.split('\n')

dictionary = {}

for row in rows[1:]:
    columns=row.split('\t')
    name=columns[0]
    dictionary[name]=0

for filename in os.listdir(folder):
    file_path=f"{folder}/{filename}"

    with open(file_path, encoding="utf-8") as file:
        text = file.read()
    tagged_text=text
    

    for pattern in dictionary:
        matches = re.findall(pattern, text)
        n_matches = len(matches)
        dictionary[pattern]+=n_matches
        tagged_text=re.sub(pattern,'+++' + pattern, tagged_text)
    print(tagged_text)
       
for pattern, count in dictionary.items():
    if count >0:
        print(f"found {pattern} {count} times")
