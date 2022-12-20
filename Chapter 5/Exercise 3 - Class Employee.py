class Employee:
  def __init__(self, name, age, id, salary):
    self.name = name
    self.age = age
    self.id = id
    self.salary = salary

  def setData(self):
    self.name = input("Enter name: ")
    self.age = int(input("Enter age: "))
    self.id = input("Enter id: ")
    self.salary = int(input("Enter salary: "))

  def getData(self):
    print(f"Name: {self.name}")
    print(f"Age: {self.age}")
    print(f"ID: {self.id}")
    print(f"Salary: {self.salary}")

employee_list = []

for i in range(5):
  employee = Employee("", 0, "", 0)
  employee.setData()
  employee_list.append(employee)

for employee in employee_list:
  employee.getData()
  print()