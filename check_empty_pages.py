import os
import re


start = "mARkdown"
for folder in os.listdir(start):
    group_folder = os.path.join(start, folder)
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
                n_empty = len(re.findall("!\[image filename.+[\n#~ ]+Page", text))
            if n_empty > 2:
                print(fp)
                print(f"{n_empty}/{n_pages} pages empty")
            if n_pages < 200:
                print(fp)
                print("only", n_pages, "pages in this text!")
        except:
            print("READ ERROR", fp)
