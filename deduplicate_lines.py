import re

def simplify(text):
    return re.sub(r"\W+", "", text)

fn = "mARkdown/group_1/7603_group_1"


with open(fn, mode="r", encoding="utf-8") as file:
    text = file.read().splitlines()

new_text = []
prev_line = ""
for line in text:
    # skip identical lines
    if line == prev_line:
        continue
    # empty lines add them
    if simplify(line) == "":
        new_text.append(line)
        prev_line = line
        continue
    # if the current line is part of the previous line: skip it
    if simplify(line) in simplify(prev_line):
        prev_line = line
        continue
    # if the previous line is part of the current line: replace it
    if simplify(prev_line) and simplify(prev_line) in simplify(line):
        new_text = new_text[:-1]
        new_text.append(line)
        print(prev_line)
        print(simplify(prev_line))
        print(line)
        print(simplify(line))
        print("------")
    else:
        new_text.append(line)
    prev_line = line

with open(fn+"_fixed", mode="w", encoding="utf-8") as file:
    file.write("\n".join(new_text))
