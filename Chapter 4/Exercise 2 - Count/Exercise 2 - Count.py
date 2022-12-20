import re
word = "Hello my name is Amster Sani"  
filename = "sentence.txt"

with open(filename, 'r') as file_handler:
    for count, line in enumerate(file_handler):
        pass
    print('Total Lines', count + 1)
    for line in file_handler:
            if(line==word):
                count=count+1
    print("Occurrences of the word", word, ":", count)