print("Enter three numbers.")
num_limit = 5
num_count = 1
numlist = []
while num_count <= num_limit:
    num = int(input(f"Number {num_count}: "))
    numlist.append(num)
    num_count+=1

result = str(numlist)[1:-1] #remove bracket
print(f'Numbers you entered: {result}')

