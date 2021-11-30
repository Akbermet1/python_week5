"""Напишите декоратор repeat, который принимает как именованный аргумент num целое число
(количество выполнения декорированной функции) и запускает декорированную функции указанное количество раз.

Например
```python
@repeat(num=4)
def function(name):
    print(f"{name}")

При вызове function("Python"), вывод должен выглядеть так:
Python
Python
Python
Python
"""
# def repeat(num):
#     def decorator(func):
#         def wrapper(name):
#             for i in range(num):
#                 func(name)
#         return wrapper
#     return decorator


# @repeat(num=3)
# def function(name):
#     print(f"{name}")

# function("delilah")

"""Напишите декоратор countdown, который принимает параметр seconds и отсчитывает
секунды до запуска декорированной функции.

Например:
```python
@countdown(seconds=5)
def func():
    print('Hello world')
```
#вывод
5
4
3
2
1
Hello world!
"""

from typing import Text


def decorator(function):
    def wrapper():
        ...
        # from threading import Timer
        # action = Timer(1.0, )

    return wrapper

def func():
    print('Hello world')


'''task 1'''
# def call_function(func):
#     def wrapper():
#         print(f"Вызываю функцию {func.__name__}")
#         res = func()
#         print(f"Вызов функции {func.__name__} прошёл успешно")
#     return wrapper
    
# @call_function
# def first():
#     print("hello world")
#     return "hello world"
    
# first()


'''task 2'''
# def func_start_time(func):
#     def wrapper():
#         import datetime
#         date = datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
#         print(f"Функция запущена {date}")
#         func()
#     return wrapper
    
# @func_start_time
# def func():
#     print('Hello world')
    
# func()

'''task 3'''
# def make_bold(func):
#     def wrapper():
#         content = func()
#         result = "<b>" + content + "</b>"
#         return result
#     return wrapper


# def make_italic(func):
#     def wrapper():
#         content = func()
#         result = "<i>" + content + "</i>"
#         return result
#     return wrapper


# def make_underline(func):
#     def wrapper():
#         content = func()
#         result = "<u>" + content + "</u>"
#         return result
#     return wrapper


# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return 'Hello world'
 
# print(hello())

'''task 4'''
# read about timer here: https://www.pythonpool.com/python-timer/
# def benchmark(func):
#     def wrapper():
#         import time
#         start = time.time()
#         func()
#         end = time.time()
#         print(f"Время выполнения: {end - start} секунд.")
#     return wrapper
        
        
# @benchmark 
# def fetch_webpage(): 
#   import requests 
#   webpage = requests.get('https://google.com') 

# fetch_webpage()


''' 8 '''
# read about sorted func here: https://www.programiz.com/python-programming/methods/built-in/sorted
# https://stackoverflow.com/questions/10154568/postpone-code-for-later-execution-in-python-like-settimeout-in-javascript
# https://www.artima.com/weblogs/viewpost.jsp?thread=240845#decorator-functions-with-decorator-arguments
# https://www.datacamp.com/community/tutorials/role-underscore-python
def get_length(person):
    return person[2]

# def sort_names(func):
#     def wrapper(people_list: list):
#         prefixed_list = func(people_list)
#         sorted_list = [people_list[i] for i,person in enumerate(people_list)] # fix this
#         # sorted(prefixed_list, key=get_length, reverse=True)
#         print("sorted", sorted_list)

#         return sorted_list
#     return wrapper


# @sort_names
def prefix_name(people_list: list):
    prefixed_list = ["Ms. " + person[0] + " " + person[1] if person[3] == "F" else "Mr. " + person[0] + " " + person[1] for person in people_list]
    # print(prefixed_list)
    return prefixed_list


print("end result:", prefix_name([('Leo', 'Nimoy', 40, 'M', 1),
('Carrie', 'Fisher', 35, 'F', 5),
('Harrison', 'Ford', 38, 'M', 3)]))




            