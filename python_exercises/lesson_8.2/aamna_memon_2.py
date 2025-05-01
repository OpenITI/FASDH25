print('1. I am printing the path to the file from a specific folder \n')
folder = "aljazeera_articles"
filename = "2024-03-28_9276.txt"     
file_path = f"{folder}/{filename}"
print (f"The path to the article is: {file_path}")
print('--------------------\n')


print ('2. I am finding all the occurences of Israel or Israeli in the text \n')
import re
with open(file_path, encoding="utf-8") as file:
    text = file.read()       #loading the text in Python
pattern = r"Israeli?"
matches = re.findall(pattern, text)
n_matches = len(matches)
print(f"{filename} contains {pattern} {n_matches} times in the article \n ")
print('--------------------\n')


print ('''3. I am finding all occurences of Israel or Israeli, Gaza or Gazan, 
Palestine or Palestinian in a single article. \n ''')
patterns = [r"Israel?", r"Gazan?", r"Palestine|Palestinian"]
for pattern in patterns:
    matches=re.findall(pattern, text)
    n_matches=len(matches)
    print (f"{filename} contains {pattern} {n_matches} times in the article")
print('--------------------------')
