import re

folder='aljazeera_articles'
filename='2023-10-07_7606.txt'
filepath=f'{folder}/{filename}'

with open(filepath, mode='r', encoding='utf8') as file:
    text=file.read()
          
splitter=r'\n+-+\n+'
split_text=re.split(splitter, text)
title=split_text[0]
body=split_text[1]
          

pattern=r'Gazan?'
matches=re.findall(pattern, title)
no_of_matches=len(matches)

print (f'The file {filename} contains {no_of_matches} matches for the regex {pattern}.')
