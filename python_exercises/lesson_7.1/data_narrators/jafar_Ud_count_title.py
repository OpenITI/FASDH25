filename='data_narrators.txt'
with open(filename, 'r',encoding="utf8") as file:
    lines=file.readlines()
matching_lines = []
for heading in lines:
    if '###' in heading:
        matching_lines.append(heading)
for heading in matching_lines[:3]:
    print(heading)

