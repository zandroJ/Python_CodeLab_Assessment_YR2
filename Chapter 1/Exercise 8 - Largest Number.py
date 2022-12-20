num1 = input('enter first number: ' )
num2 = input('enter second number: ' )
num3 = input('enter third number: ' )

result = print('Largest number: ' + str(num1)) if num1 > num2 and num1 > num3 else print('Largest number: ' + str(num2)) if num2 > num3 else print('Largest number: ' + str(num3))

