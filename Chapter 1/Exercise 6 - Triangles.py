print("Enter three sides of triangle")
side1 = int(input("Enter first side: ")) # x
side2 = int(input("Enter second side: ")) # y
side3 = int(input("Enter third side: ")) # z

comb_side = side2 + side1
if side3 <= comb_side:
    print('it is a triangle.')
else:
    print('not a triangle')
if side1 == side2 == side3:
    print("The triangle type is: Equalateral")
elif side1 != side2 == side3 or side2 != side1 == side3 or side3 != side1 == side2:
    print("The triangle type is: Isosceles")
else:
    print("The triangle type is: Scalene")