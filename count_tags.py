import os
import re


start = "mARkdown"
for folder in os.listdir(start):
    group_folder = os.path.join(start, folder)
    print("***************")
    print(group_folder)
    for fn in os.listdir(group_folder):
        if fn.endswith(".yml"):
            continue
        fp = os.path.join(group_folder, fn)
        if os.path.isdir(fp):
            continue
        try:
            with open(fp, mode="r", encoding="utf-8") as file:
                text = file.read()
                n_pages = len(re.findall("PageV", text))
                if 0 < n_pages < 180:
                    n_tags = len(re.findall("### *\|+", text))
                    print(n_tags, fn)
        except:
            print("READ ERROR", fp)
