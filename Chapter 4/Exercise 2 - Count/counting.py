f = open("sentence.txt","r")
for line in enumerate(f):
    pass
    for line in f:
        sent = sentence.split()
        words = line.split()
        for i in words:
            if(i==sent):
                count=count+1
    print("Occurrences of the word", sentence, ":", count)
f.close()