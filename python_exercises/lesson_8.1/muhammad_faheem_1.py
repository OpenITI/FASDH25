Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
... 
... # Task 0. Open a single article :
... 
... folder = "aljazeera_articles"
... filename = "2024-03-28_9276.txt"
... 
... # EXERCISE: use an f string to combine the folder and filename variables into a path
... #           (remember: a path uses slashes "/" to separate file and folder names)
... # NB: you HAVE to use the variable names,
... #     DO NOT write f"aljazeera_articles/2024-04-18_406.txt"
... 
... file_path = f"{folder}/{filename}"
... 
... print(f"The path to the article is: {file_path}")
... 
... # load the text file into Python:
... with open(file_path, mode="r", encoding="utf8") as file:
...     text = file.read()
... 
... # EXERCISE: print the first 100 characters of the text:
... print(text[:100])
... 
... pattern = r"Israeli?"
... matches = re.findall(pattern, text)
... print(matches)
... n_matches = len(matches)
... print(n_matches)
... print(f"There are {n_matches} of {pattern} in the article {filename}")
... 
... splitter_pattern = r"\n+-+\n+"
... split_text = re.split(splitter_pattern, text)
... title  = split_text[0]
... body = split_text[1]
... print("title: ", title)
... print("body: ", body)
... 
... matches = re.findall(pattern, body)
... n_matches = len(matches)
print(f"There are {n_matches} of {pattern} in the article body {filename}")

matches = re.findall(pattern, text)
n_matches = len(matches)
print(f"There are {n_matches} of {pattern} in the article title {filename}")

matches = re.findall(pattern, text)
n_matches = len(matches)
print(f"There are {n_matches} of {pattern} in the article  {filename}")


