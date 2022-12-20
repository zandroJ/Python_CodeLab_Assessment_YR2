table = int(input("Enter a number to find the multiplication table: "))
print(f'Multiplication table of: ', table)

for nums in range(1,11):
    ans = table * nums
    print(f'{table} x {nums} = {ans}')