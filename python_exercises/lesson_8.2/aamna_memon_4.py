print ('Finding 1+ expressions in multiple files of a folder. \n')
import re
import os                           
folder='aljazeera_articles'


patterns = [r"Israeli?", r"Gazan?", r"Palestine|Palestinian"]
n_patterns=len(patterns)
total = [0,0,0]


for filename in os.listdir(folder):
    file_path= os.path.join(folder, filename)          #can also do manually with f"{folder}/{filename}"
                                                       #but to reduce error, use os.path.join
    with open(file_path, encoding="utf-8") as file:     
        text = file.read()
        
    for pattern_number in range(n_patterns):                     #this nested loop counts the occurences of Israeli? in n_patterns[0+,0,0]
        pattern = patterns[pattern_number]                       #then adds the counts of Palestine|Palestinian in n_patterns[0,0+,0]
        matches = re.findall(pattern, text)                      #then adds the counts of Gazan? in n_patterns[0,0,0+]
        n_matches = len(matches)                                 #it keeps on going until the last folder/filename
        print(f"{filename} contains {pattern} {n_matches} times in the article")
        total[pattern_number] += n_matches
        print(f"until now we found {total} matches")             #when we reach the last iteration, it'll give the total of ALL occurences in ALL filenames

print(f"Found {total} matches in the whole corpus")
for pattern_number in range(n_patterns):
    pattern = patterns[pattern_number]
    n_matches = total[pattern_number]
    print(f"we found {n_matches} matches for {pattern} in all texts")  #this loop has the same result as the last iteration
                                                                       #of the nested loop, it is counting ALL the occurences
                                                                       #in one attempt
