"""
1) Создайте класс Languages. В этом классе должен быть атрибут класса, который обозначает количество студентов,
изучающих какой-либо язык программирования. От класса Languages создайте два дочерних класса: Python, JavaScript.
В них  также должны быть атрибуты, указывающие на количество студентов, изучающих тот или иной язык.
При создании объекта-студента от одного из дочерних классов, автоматически количество студентов в классах меняется.
Если студент изучает язык Python, то количество студентов должно увеличиться на один и в классе Python и в классе
Languages. Аналогично со студентами JavaScript. Далее, в дочерних классах должен быть переопределен метод coding,
в классе Python он должен выдавать вам строку “I am Python student. I am coding now.”,
а в классе JavaScript - “I am JavaScript student. I am coding now”. Создайте двух студентов от двух дочерних классов.
Далее программа сама рандомно выбирает студента и предлагает вам угадать, какого студента она выбрала.
После вашего выбора, он вызывает метод coding у загаданного студента и выдает вам результат: если вы отгадали
правильно, пишет “Good job!”, если нет - “No bueno :(”
"""
import random 
class Languages():
    number_of_students = 0

    def __init__(self):
        Languages.number_of_students += 1

    def coding(self):
        raise NotImplementedError
    
    # my implementation:
    # def coding(self, language):
    #     print(f"I am {language} student. I am coding now.")

class Python(Languages):
    number_of_students = 0

    def __init__(self):
        super().__init__()
        Python.number_of_students += 1

    def __str__(self):
        return "Python student"

    def coding(self):
        print("I am Python student. I am coding now.")

        # my implementation:
    # def coding(self):
    #     super().coding("Pyhton")

class JavaScript(Languages):
    number_of_students = 0

    def __init__(self):
        super().__init__()
        JavaScript.number_of_students += 1

    def __str__(self):
        return "JavaScript student"

    def coding(self):
        print("I am JavaScript student. I am coding now.")

    # my implementation:
    # def coding(self):
    #     super().coding("JavaScript")

lang1 = Languages()
lang2 = Languages()
print(Languages.number_of_students)

p_student = Python()
js_student = JavaScript()

chosen_student = p_student if random.randint(0,1) else js_student

your_guess = input("Guess what language is the chosen student learning(Python/JS)? ").lower()

if your_guess ==  "python" and chosen_student == p_student:
    print("Good job!")
elif your_guess ==  "js" and chosen_student == js_student:
    print("Good job!")
else:
    print("No bueno :(")

print(f"the chosen student: {chosen_student},\tyour guess: {your_guess}")

"""
2) Создайте свой класс MyList, который наследуется от list. Переопределите метод списка insert(),
который обычно принимает первым аргументом индекс, а вторым - элемент. В своем классе MyList переопределите
этот метод так, чтобы он принимал аргументы  в обратном порядке: первым - элемент, вторым - индекс
"""

class MyList(list):
    def func(self):
        print(super())
    # def insert(self, element, index):
    #     return super(MyList, list).insert(index, element)

list_ = MyList([1, 4, 5])
print(type(list_))
list_.func()
# print(list_.insert("Makers", 0))
# print(list_)