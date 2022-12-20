class Student:
  def __init__(self, name, mark1, mark2, mark3):
    self.name = name
    self.mark1 = mark1
    self.mark2 = mark2
    self.mark3 = mark3

  def calcGrade(self):
    return (self.mark1 + self.mark2 + self.mark3) / 3

  def display(self):
    print(f"{self.name} has an average grade of {self.calcGrade():.2f}")

student1 = Student("Alice", 85, 90, 95)
student1.display()

print("Enter data for student 2:")
name = input("Enter name: ")
mark1 = int(input("Enter mark 1: "))
mark2 = int(input("Enter mark 2: "))
mark3 = int(input("Enter mark 3: "))
student2 = Student(name, mark1, mark2, mark3)
student2.display()