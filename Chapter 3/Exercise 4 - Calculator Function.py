print("Menu: \n 1. Addition\n 2. Subtraction \n 3. Multiplication \n 4. Division\n 5. Floor Division \n 6. Modulo \n 6. Power")
num1 = int(input("Input first number: "))
num2 = int(input("Input 2nd number: "))
op = int(input("Input operation number from menu: "))

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
def floor(num1, num2):
    return num1 // num2
def mod(num1, num2):
    return num1 % num2
def pow(num1, num2):
    return num1 ** num2

if op == 1:
    ans = add(num1,num2)
    print("Operation used: Addition \n answer: " + str(ans))
elif op == 2:
    ans = subtract(num1,num2)
    print("Operation used: Subtraction \nanswer: " + str(ans))
elif op == 3:
    ans = multiply(num1,num2)
    print("Operation used: Multiplication \nanswer: " + str(ans))
elif op == 4:
    ans = divide(num1,num2)
    print("Operation used: Division \nanswer: " + str(ans))
elif op == 5:
    ans = floor(num1,num2)
    print("Operation used: Floor Division \nanswer: " + str(ans))
elif op == 6:
    ans = mod(num1,num2)
    print("Operation used: Modulos \nanswer: " + str(ans))
elif op == 7:
    ans = pow(num1,num2)
    print("Operation used: Power \nanswer: " + str(ans))
else:
    print("invalid input")



