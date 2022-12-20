class Dog:
  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age
  def woof(self):
    print("Woof!")
dog_one = Dog("Riyahd", "Japanese Spitz", 1)
dog_two = Dog("Policedog", "K9", 5)
print(f"{dog_one.name} is a {dog_one.breed} and is {dog_one.age} years old.")
print(f"{dog_two.name} is a {dog_two.breed} and is {dog_two.age} years old.")
if dog_one.age > dog_two.age:
  oldest_dog = dog_one
else:
  oldest_dog = dog_two
print(f'{oldest_dog.name} is older therefore,') ; oldest_dog.woof()
