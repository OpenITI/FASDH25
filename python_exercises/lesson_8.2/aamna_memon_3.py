import re
import os                           #os helps to run functions of
folder='aljazeera_articles'         #OPERATING SYSTEM
                                    #eg creating or deleting new folders, etc


print ('1. Finding the path to all the files in my folder \n')                                   
for filename in os.listdir(folder):  #iterating over all the articles in folder
    file_path=f"{folder}/{filename}"
    print(f"The path to the article is: {file_path}. \n")
print('----------------------------------- \n')



print ('2. Finding 1 expression in all files of a folder. \n') 
for filename in os.listdir(folder):
    file_path=f"{folder}/{filename}"
    with open(file_path, encoding="utf-8") as file:     #indented code means we are loading 
        text = file.read()                              #all the articles at same time
    pattern = r"Israeli?"
    matches = re.findall(pattern, text)
    n_matches = len(matches)
    print(f"{filename} contains {pattern} {n_matches} times in the article")
