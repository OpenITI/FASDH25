import re
import os

# define which folder to use:
# NB: these are different articles than in the previous weeks
folder = "aljazeera_articles"  

# define the patterns we want to search:
path = "gazetteers/geonames_gaza_selection.tsv"
with open(path, encoding="utf-8") as file:
        data = file.read()

print(data)

patterns = {}
rows = data.split("\n")
print(rows)
for row in rows:
    columns = row.split("\t")
    name = columns[0]
    print(name)
    patterns[name] = 0



for filename in os.listdir(folder):
    # build the file path:
    file_path = f"{folder}/{filename}"
    print(f"The path to the article is: {file_path}")

    # load the article (text file) into Python:
    with open(file_path, encoding="utf-8") as file:
        text = file.read()

    # find all the occurences of the patterns in the text:
    for pattern in patterns:
        matches = re.findall(pattern, text)
        n_matches = len(matches)
       # print(n_matches, pattern)
        patterns[pattern] += n_matches

for pattern in patterns:
    count = patterns[pattern]
    if count >=1 :
        print(f"found {pattern} {count} times")
