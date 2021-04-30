# def hello_decorator(func):
#     def inner1():
#         print("this is before function execution")
#         func()
#         print("this is after function execution")
#     return inner1
#
#
# def function_to_be_used():
#     print("this is inside the function")
#
#
# function_to_be_used = hello_decorator(function_to_be_used)
# function_to_be_used()
#
#
# def function_new():
#     print("this is new function")
#
#
# function_new = hello_decorator(function_new)
# function_new()


from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthDate(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person("rajan", 21)
person2 = Person.fromBirthDate("rajan", 1991)

print(person1.age)
print(person2.age)

print(Person.isAdult(22))
