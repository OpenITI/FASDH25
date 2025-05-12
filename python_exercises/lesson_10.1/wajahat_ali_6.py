import re
import os
import pandas as pd

# fix this function!
def write_tsv(data, column_list, path):
    """This function converts a dictionary to a tsv file.

    It takes three arguments:
        data (dict): the dictionary
        column_list (list): a list of column names
        path (str): the path to which the tsv file will be written
    """
    # turn the dictionary into a list of (key, value) tuples:
    items = list(data.items())
    # create a dataframe from the items list:
    df = pd.DataFrame.from_records(items, columns=column_list)
    # write the dataframe to tsv:
    df.to_csv(path, sep="\t", index=False)


# define which folder to use:
folder = "aljazeera_articles"

# load the gazetteer from the tsv file:
path = "gazetteers/geonames_gaza_selection.tsv"
with open(path, encoding="utf-8") as file:
    data = file.read()

# build a dictionary of patterns from the place names in the first column:
patterns = {}
rows = data.split("\n")
for row in rows[1:]:
    if row.strip() == "":
        continue
    columns = row.split("\t")
    name = columns[0]
    patterns[name] = 0

# count the number of times each pattern is found in the entire folder:
for filename in os.listdir(folder):
    file_path = f"{folder}/{filename}"
    with open(file_path, encoding="utf-8") as file:
        text = file.read()

    for pattern in patterns:
        matches = re.findall(pattern, text)
        n_matches = len(matches)
        patterns[pattern] += n_matches

# print the frequency of each pattern:
for pattern in patterns:
    count = patterns[pattern]
    if count >= 1:
        print(f"found {pattern} {count} times")

# call the function to write your tsv file:
columns = ["asciiname", "frequency"]
tsv_filename = "frequencies.tsv"
write_tsv(patterns, columns, tsv_filename)
