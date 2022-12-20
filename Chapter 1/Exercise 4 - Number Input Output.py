print("Enter three numbers.")
num_limit = 3
num_count = 1
numlist = []
while num_count <= num_limit:
    num = int(input(f"Number {num_count}: "))
    numlist.append(num)
    num_count+=1

print("Your numbers forward:")
for values in (numlist):
    print(values) 
print("your numbers reversed:")
for values in reversed(numlist):
    print(values) 

