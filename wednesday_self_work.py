"""
1) Напишите программу по следующему описанию. Есть класс "Снайпер". От него создаются два экземпляра.
Каждому устанавливается здоровье в 100 очков. В случайном порядке они стреляют друг в друга. Тот, кто стреляет,
здоровья не теряет. У того, в кого стреляют, оно уменьшается на 20 очков от одного выстрела. После каждого
выстрела надо выводить сообщение, какой снайпер атаковал, и сколько у противника осталось здоровья.
Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.
"""
import random
class Sniper():
    def __init__(self, name):
        self.health = 100
        self.name = name
    
    def get_shot(self):
        self.health -= 20

    def shoot(self, target):
        target.health -= 20

sniper1 = Sniper("Jamine")
sniper2 = Sniper("Alec")

while True:
    if sniper1.health <= 0 or sniper2.health <= 0:
        print(f"\nGame over:\t{attacker.name} won this time")
        break

    attacker = sniper1 if random.randint(0,1) else sniper2
    victim = sniper1 if attacker == sniper2 else sniper2 

    # victim.get_shot()
    attacker.shoot(victim)
    print(f"{attacker.name} attacked, {victim.name}'s health = {victim.health}")

"""
2) Напишите программу по следующему описанию. Есть класс Hogwarts. В нем определены следующие атрибуты-факультеты: 
Gryffindor, Ravenclaw, Hufflepuff, Slytherin. От класса Hogwarts создаются объекты-студенты.
При создании студентов необходимо указать баллы за их следующие качества: courage (храбрость),
intelligence (интеллект), justice (справедливость), ambition (амбиции). У студентов не могут быть
качества одинакового уровня. В зависимости от того, какое качество студента преобладает, метод sorting_hat
будет распределять студента в один из факультетов и выдавать в какой факультет поступил студент.

Примечание: 
Преобладает courage -> Gryffindor
Преобладает intelligence -> Ravenclaw
Преобладает justice -> Hufflepuff
Преобладает ambition -> Slytherin
"""
faculties = ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]

class Hogwarts():
    def __init__(self, name, courage, intelligence, justice, ambition):
        self.name = name
        self.courage = courage
        self.intelligence = intelligence
        self.justice = justice
        self.ambition = ambition

    def sorting_hat(self):
        qualities = [self.courage, self.intelligence, self.justice, self.ambition]
        max_quality = max(qualities)

        if max_quality == qualities[0]:
            self.faculty = faculties[0]
        elif max_quality == qualities[1]:
            self.faculty = faculties[1]
        elif max_quality == qualities[2]:
            self.faculty = faculties[2]
        elif max_quality == qualities[3]:
            self.faculty = faculties[3]

    def get_faculty(self):
        return self.faculty

harry = Hogwarts("Harry", 14, 5, 11, 23) 
harry.sorting_hat()

lizzy = Hogwarts("Lizzy", 19, 100, 101, 2) 
lizzy.sorting_hat()

''' 2 '''
# import math
# class Circle:
#     color = "Синий"
#     pi = 3.14
    
#     def __init__(self, r):
#         self.radius = r
        
#     def get_area(self):
#         return self.pi*math.pow(self.radius, 2)
        
# circle = Circle(2) 
# circle.color = "red"
# circle.get_area()


''' task 3 '''
class BankAccount:
    balance = 0

    
    def withdraw(self, amount):
        self.balance -= amount
        print(f"Ваш баланс: {self.balance} сом")
        return self.balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Ваш баланс: {self.balance} сом")
        return self.balance
        
account = BankAccount()
account.deposit(1000) 
account.withdraw(500)

''' task 4 '''
# class Taxi:
#     def __init__(self, name, cost, cost_km):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km
        
#     def get_total_cost(self, km):
#         total = (km*self.cost_km) + self.cost
#         return f"Такси {self.name}, стоимость поездки: {total} сом"
        
# taxi1 = Taxi("Namba", 5, 10)
# taxi2 = Taxi("Yandex",9, 11)
# taxi3 = Taxi("Jorgo", 4, 20)

# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14)) 

'''task 5'''
class Phone:
    def __init__(self, name, last_name, phone): 
        self.name = name
        self.last_name = last_name
        self.phone = phone

    def get_info(self):
        print(f"Контакт: {self.name} {self.last_name}, телефон: {self.phone}")
        
contact = Phone("Alec", "Benjamin", "+996777111777")
contact.get_info()