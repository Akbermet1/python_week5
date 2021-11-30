# from dataclasses import dataclass
import typing
'''use this module for checking the type'''

'''Intro to OOP '''

'''
Classes:
there are attributes, methods of a class

attributes can be: attributes of a class, attributes of an instance
'''

'''
Methods ALWAYS include self in their declaration as the first parameter 
NOTE about METHODS: even if it doesn't take any arguments, in the declaration, self is always specified 
in the declaration of the method
'''
'''
method __init__() shouldn't be confused with a constructor beacuse it's an initializer!!!
There's another method that's called a constructor
'''

'''
one can also redeclare built-in methods of a class:
e.g.:

class Class_name:
    def __str__(self):
        #body of the redeclaration
'''

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, my name is {self.name} :)")

    def __str__(self):
        return self.name

tim = Person("Tim", 20)
print(tim)
tim.greet()

'''when you do this: hugh = Person("High", 30), this is what actually happens:'''
# hugh = Person.__new__()
# Person.__init__(hugh,"High", 30)


'''
when a method is just declared as def method_name():...
it's called an object/instance method

when a method is just declared as:
@classmethod     <- built-in decorator
def method_name():
    ...
it' called a class method
'''

'''
to check if an object belongs to a class:
isinstance(obj, class)   -> Bool
'''

class Car():
    def __init__(self, model, year, volume, color, fuel):
        self.model = model
        self.year = year
        self.volume = volume
        self.color = color
        self.fuel = fuel

    def __str__(self):
        return f"{self.model} {self.year} {self.color}"

car1 = Car("Toyota Camry", 2018, 2.5, "black", "gasoline")
car2 = Car("Toyota Camry", 2011, 2.5, "grey", "gasoline")
print(car1)
print(car2)



# @dataclass
# class Phone:
#     model: str
#     year: int
#     ram: int
#     color: str

# phone1 = Phone("Apple iPhone 13", 2021, 8, "black")


'''Meta classes are classes that produce classes'''

'''~~~Ingeritance~~~'''
class A():
    attr1 = 'a'

    def method(self):
        print("Hello there")

class B(A):
    ...

'''
child classes can redeclare, add smth to parent methods
'''

class A:
    attr1 = "a"
    attr2 = "b"

    def method1(self):
        print("Hello!!!")


class B(A):
    attr3 = "new"
    attr2 = "value"

    #redefinition of a parent method:
    # def method1():
    #     print("Byeeee")

    # this way we add(not completely redefine it) some functionality to the parent method
    def method1(self):
        super.method1()     #обращение к родительскому классу(прямому предку) 
        print("BBBBBB")

