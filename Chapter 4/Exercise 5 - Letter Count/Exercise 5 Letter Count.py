import string
file = open("sentences.txt", 'r') 
text = file.read() #read files in sentence.txt
letter_count = {} #empty list for appending chars
for letter in text:
    if letter in string.ascii_letters: #ascii letters include both lower and uppercase only, not including numbers and whitespace
        if letter in letter_count: #incrementing the value if letter is present multiple times
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

for letter, letter_count in letter_count.items(): 
    print(f'{letter}: {letter_count}')


