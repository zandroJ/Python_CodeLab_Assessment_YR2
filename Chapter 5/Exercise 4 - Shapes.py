import math

class Shape:
  def inputSides(self):
    self.side1 = float(input("Enter side 1: "))
    self.side2 = float(input("Enter side 2: "))

class Circle(Shape):
  def area(self):
    return math.pi * self.side1 ** 2

class Rectangle(Shape):
  def area(self):
    return self.side1 * self.side2

class Triangle(Shape):
  def area(self):
    return self.side1 * self.side2 / 2

shape = Shape()
shape.inputSides()

circle = Circle()
circle.side1 = shape.side1
print(f"Circle area: {circle.area():.2f}")

rectangle = Rectangle()
rectangle.side1 = shape.side1
rectangle.side2 = shape.side2
print(f"Rectangle area: {rectangle.area():.2f}")

triangle = Triangle()
triangle.side1 = shape.side1
triangle.side2 = shape.side2
print(f"Triangle area: {triangle.area():.2f}")