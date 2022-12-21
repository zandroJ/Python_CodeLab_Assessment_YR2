import operator

def calculator():
    print("Calculator Menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Check greater number")
    print("Enter Q to quit")

    while True:
        try:
            choice = input("Enter your choice (1-6): ")
            if choice == "Q" or choice == "q":
                print("closing program")
                break

            choice = int(choice)
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            if choice == 1:
                result = operator.add(num1, num2)
            elif choice == 2:
                result = operator.sub(num1, num2)
            elif choice == 3:
                result = operator.mul(num1, num2)
            elif choice == 4:
                result = operator.truediv(num1, num2)
            elif choice == 5:
                result = operator.mod(num1, num2)
            elif choice == 6:
                result = num1 if num1 > num2 else num2

            print("Result:", result)
        except ValueError:
            print("Invalid input. Please try again.")

calculator()
