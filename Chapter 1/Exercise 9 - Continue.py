loop_count = 0
while True:
    ans = input('press y to keep looping: ')
    if ans.lower() != "y" and ans.upper !="Y":
        break
    loop_count += 1

print("The Y is pressed and looped ",(loop_count), "times.")