import re       # imports re module or regular expressions

folder = "aljazeera_articles" #defining folder and filename
filename = "2024-01-15_10035.txt"

file_path = f"{folder}/{filename}" #creates full file path


#Open the file and read its content
with open(file_path, mode="r", encoding="utf8") as file: #opens the file in read mode with utf8 encoding
    text = file.read()  #Reads the entire content of the file into the variable "text"                

#definr the regular expression to match 'Gaza' and 'Gazan'
pattern = r"Gazan?"    

#Split the text into title and body based on a separator pattern
splitter_pattern = r"\n+-+\n+"   # Regex pattern to detect a separator (new lines with dashes)
split_text = re.split(splitter_pattern, text) # Split the text into parts


#Extract the title and body from the split text
title = split_text[0] # Splits first part as title
body = split_text[1]   #Splits second part as body 





#Find all the accurances of the pattern "Gazan?" in the title 
matches = re.findall(pattern, title) #Finds all occurances of the pattern in the title
n_matches = len(matches) #counts the number of matches in the title 
print(f"The file {filename} contains {n_matches} matches for the regex {pattern}.") #prints the output



