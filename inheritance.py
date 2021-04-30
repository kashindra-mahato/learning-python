# class Base():
#     pass
#
#
# class Derived(Base):
#     pass
#
#
# print(issubclass(Derived, Base))
# print(issubclass(Base, Derived))
#
# b = Base()
# d = Derived()
#
# print(isinstance(b, Derived))
# print(isinstance(d, Base))
#
#
# class Base():
#     def __init__(self, x):
#         self.x = x
#
#
# class Derived(Base):
#     def __init__(self, x, y):
#         super().__init__(x)
#         #Base.x = x
#         self.y = y
#
#     def printXY(self):
#         print(self.x, self.y)  # Base.x use garna paiyena
#
#
# d = Derived(10, 20)
# d.printXY()
#
#
# class Base1():
#     def __init__(self):
#         self.str1 = "Str1"
#         print("base1")
#
#
# class Base2():
#     def __init__(self):
#         self.str2 = "str2"
#         print("base2")
#
#
# class Derived(Base1, Base2):
#     def __init__(self):
#         Base1.__init__(self)
#         Base2.__init__(self)
#         print("Derived")
#
#     def printStr(self):
#         print(self.str1, self.str2)
#
#
# ob = Derived()
# ob.printStr()
#
#
# class Person(object):
#     def __init__(self, name):
#         self.name = name
#
#     def getName(self, name):
#         self.name = name
#         return self.name
#
#     def isEmployee(self):
#         return False
#
#
# class Employee(Person):
#     def isEmployee(self):
#         return True
#
#
# emp = Person()
# print(emp.getName("Rajan"), emp.isEmployee())
#
# emp = Employee()
# print(emp.getName("kapil"), emp.isEmployee())
#
#
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#
#     def __repr__(self):
#         return f"{self.name} is a {self.species}"
#
#     def make_sound(self, sound):
#         print(f"this animal says {sound}")
#
#
# class Cat(Animal):
#     def __init__(self, name, breed, toy):
#         super().__init__(name, species="cat")
#         self.breed = breed
#         self.toy = toy
#
#     def play(self):
#         print(f"{self.name} plays with {self.toy}")
#         print(f"{self.species} is {self.breed}")
#
#
# blue = Cat("Blue", "scottish fold", "String")
# blue.play()

class Aquatic:

  def __init__(self,name):
    print("AQUATIC INIT!")
    self.name = name


  def swim(self):
    return f"{self.name} is swimming"


  def greet(self):
    return f"I am {self.name} of the sea!"


class Ambulatory:
  def __init__(self,name):
    print("AMBULATORY INIT!")
    self.name = name


  def walk(self):
    return f"{self.name} is walking"


  def greet(self):
    return f"I am {self.name} of the land!"


class Penguin(Ambulatory, Aquatic):
  def __init__(self, name):
    print("PENGUIN INIT!")
    super().__init__(name=name)
    # Ambulatory.__init__(self,name=name)
    # Aquatic.__init__(self, name=name)


jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")


print(captain_cook.swim())
print(captain_cook.walk())
print(captain_cook.greet())


print(f"captain_cook is instance of Penguin: {isinstance(captain_cook, Penguin)}")
print(f"captain_cook is instance of Aquatic: {isinstance(captain_cook, Aquatic)}")
print(f"captain_cook is instance of Ambulatory: {isinstance(captain_cook, Ambulatory)}")


# jaws.swim() # 'Jaws is swimming'
# jaws.walk() # AttributeError: 'Aquatic' object has no attribute 'walk'
# jaws.greet() # 'I am Jaws of the sea!'


# lassie.swim() # AttributeError: 'Ambulatory' object has no attribute 'swim'
# lassie.walk() # 'Lassie is walking'
# lassie.greet() # 'I am Lassie of the land!'

# captain_cook.swim() # 'Captain Cook is swimming'
# captain_cook.walk() # 'Captain Cook is walking'
# captain_cook.greet() # ??

