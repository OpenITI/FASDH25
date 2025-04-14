print('1. I AM LOADING THE MARKDOWN FILE & PRINTING 1st TEN LINES \n')
filename='_________________________________________________'
with open (filename, 'r', encoding='utf8') as file:
    lines=file.readlines()                          #with function closes the file            
    for line in lines [:10]:                        #automatically after opening it,
        print (line)                                #otherwise we'd have to close it
print ('-------------------\n')                     #with file.close()
                                                    #It saves the file  from resource
                                                    #leaks and keeps the code clean
                                                    #-----------------------
                                                    #'r' means youre opening the
                                                    #file in 'reading' mode.
                                                    #'w' open it in writing mode.
                                                    #it overwrites the actual file
                                                    #so don't do it. instead: use
                                                    #'a' open in append mode
                                                    #-----------------------
                                                    #utf-8 unicode tranformation
                                                    #format - starts at 8 bit blocks
                                                    #it is a way to encode characters
                                                    #so that comouters can display 'em
                                                    #8 bits help wide rangs of char
                                                    #-----------------------
                                                    #\n means I want to add another line
                                                    #after the dashes -------------


print('2. I AM PRINTING ALL THE HEADINGS FROM THE MARKDOWN FILE \n')
heading_lines=[]                                    #creating an empty list
for heading in lines:
    if '###' in heading:     
        heading_lines.append(heading)               #IN THIS STEP, WE ARE ADDING OR
        print(heading)                              #APPENDING ALL THE HEADINGS TOGETHER
print('---------------------\n')                    #IN THE EMPTY LIST heading_lines=[]



    
print("3. I AM PRINTING THE FIRST 7 HEADINGS FROM MARKDOWN FILE \n")
for heading in heading_lines[:7]:                   #miss masoumeh used the variable
    print(heading)                                  #matching_lines in her class.
print('----------------------\n')



print("4. I AM COUNTING NUMBER OF WORDS IN EACH HEADING\n")
word_counts=[]
for heading in heading_lines:
    words=heading.split()
    count_words=len(words)
    print('This heading', heading, 'has', count_words, 'number of word(s) \n')
print('------------------------\n')



print("5. I AM NOW COUNTING THE LENGTH OF EACH WORD INSIDE ALL HEADINGS.")
                                            #(nested loops will be used
                                            #this means: an additional loop will be
                                            #added in step 4 (i.e. of word_counts)
                                            #Length of each word will be
                                            #calculated this way        
word_counts=[]
for heading in heading_lines:
    words=heading.split()
    count_words=len(words)
    print('Heading', heading, 'has', count_words, 'words.')

    for word in words:
        word_counts.append(count_words)
        print(word, 'is', (len(word)),'characters long')
    print('--------------\n')


    
print('6. I am finding 1st level headings (headings with one | only')
first_level_headings=[]                         #.count() is method like .split()
for heading in heading_lines:                   #This .count() method will count
    pipe_count=heading.count('|')               #the pipes in all headings
    if pipe_count==1:
        first_level_headings.append(heading)
    print('This heading ', heading,'has 1 | character \n')


    
