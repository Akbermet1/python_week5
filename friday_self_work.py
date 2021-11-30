"""
1) Реализуйте программу по следующему описанию. Есть классы WhatsApp, SnapChat, Telegram.
При регистрации в WhatsApp и SnapChat необходимо передавать свой номер телефона, который должен быть int.
При регистрации в Telegram необходимо передавать номер телефона и username. Во всех классах есть метод send,
в WhatsApp он принимает только text и выдает строку “I am sending a text ...” и вместо … должен быть сам текст
сообщения. В SnapChat send принимает image и text, при этом image должен быть булевым типом данных.
Если image True, то выдается сообщение “I am sending a text … with some image ”,
если  False - сообщение “I am sending a text … without image”.
В Telegram метод send принимает voice message в виде строки и выдает сообщение “I am sending a voice message ...”.
Создайте объекты от этих классов и вызовите метод send у всех объектов.
"""
class WhatsApp:
    def __init__(self, phone_number: int):
        self.phone_number = phone_number

    def send(self, text: str):
        print(f"I am sending a text: {text}")


class SnapChat:
    def __init__(self, phone_number: int):
        self.phone_number = phone_number

    def send(self, text: str, image: bool):
        if image:
            print(f"I am sending a text: {text} with some image")
        else:
            print(f"I am sending a text: {text} without an image")


class Telegram:

    def __init__(self, phone_number: int, username: str):
        self.phone_number = phone_number
        self.username = username

    def send(self, voice_msg: str):
        print(f"I am sending a voice message {voice_msg}")

user_whats = WhatsApp(79900111)
user_whats.send("hi there")

user_whats = Telegram(999111777, "lalala")
user_whats.send("greeting")

user_whats = SnapChat(79900111)
user_whats.send("see ya", False)

"""
2) Создайте два класса A и B. В обоих классах есть метод count. В классе A он подсчитывает,
сколько гласных букв в слове, которое передается в качестве аргумента в методе count,
а в классе B он подсчитывает количество согласных. Создайте объекты от этих классов
и вызовите этот метод у каждого объекта.
"""
class A:
    def count(self, string):
        vowels = "eyuioa"
        vovels_count = 0

        for char in string:
            if char in vowels:
                vovels_count += 1
        
        return vovels_count

a1 = A()
print(f'the word beautiful contains {a1.count("beautiful")} vowels')

class B:
    def count(self, string):
        vowels = "eyuioa"
        consonant_count = 0

        for char in string:
            if char not in vowels and char.isalpha():
                consonant_count += 1
        
        return consonant_count


b1 = B()
print(f'the word beautiful contains {b1.count("beautiful")} consonants')


'''2'''
class Dog:
    def voice(self):
        print("Гав")


class Cat:
    def voice(self):
        print("Мяу")

def to_pet(animal):
    animal.voice()

barsik = Cat()
rex = Dog()

to_pet(barsik)
to_pet(rex)


'''3'''
'''this implementation didn't get accepted'''
from abc import ABC, abstractmethod
from math import pow, pi

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        raise NotImplementedError

class Triange(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return (self.height*self.base)/2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pow(self.radius, 2) * pi


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def get_area(self):
        return pow(self.length, 2)

triangle = Triange(3, 4)
square = Square(3)
circle = Circle(4)

print(triangle.get_area()) 
print(square.get_area()) 
print(circle.get_area()) 