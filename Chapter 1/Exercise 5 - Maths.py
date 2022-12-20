print("Sum (+) | Diff (-) | Product (x) | Quotient (/) | Remainder (%)")
num1 = int(input("Input first number: "))
num2 = int(input("Input 2nd number: "))
op = str(input("Input operation number from menu: "))
def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2
def mod(num1, num2):
    return num1 % num2

if op == '+':
    ans = add(num1,num2)
    print("Operation used: Addition \n answer: " + str(ans))
elif op == '-':
    ans = subtract(num1,num2)
    print("Operation used: Subtraction \nanswer: " + str(ans))
elif op == '*':
    ans = multiply(num1,num2)
    print("Operation used: Multiplication \nanswer: " + str(ans))
elif op == '/':
    ans = divide(num1,num2)
    print("Operation used: Division \nanswer: " + str(ans))
elif op == '%':
    ans = mod(num1,num2)
    print("Operation used: Modulo \nanswer: " + str(ans))
else:
    print("invalid input")



