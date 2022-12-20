word_input = str(input("Please enter word: "))
vowel = 0
consonant = 0

for i in word_input:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
           vowels=vowel+1; #vowel counter is incremented by 1
    else:
        consonant=consonant+1
#consonant counter is incremented by 1
print(f'Total number of letters: {len(word_input)}')
print("The number of vowels:",vowels)
print("The number of consonant:",consonant)