''' Decorators, closure 

Methods, classes can also be decorated

Decorator: a function that takes a an argument another function

Decorators dynaically change the functionality of a function, method, or a class without the use 
of subclasses or the change of the original code of the thing that's being decorated

uses of decorators:

authorization in environment like Python, Flask, Django
logging in
synchronization
measure the time of completion


Important to remember:
functions are also objects, FIRST CLASS OBJECTS!!!
which means that:
1) functions are of object type
2) functions can be strored as a variable(in other words variables can store links to functions)
3) functions can be passed as arguments of other functions
4) functions can be returned from other functions
5) there can be other functions declared inside a function
'''

def decorator(function):

    def wrapper():
        import datetime
        function()
        print(f"Current time: {datetime.now()}")
        print("function end")
    return wrapper

# @decorator
# def func1():
#     print("A")

# # func1 = decorator(func1)

# @decorator
# def func2():
#     print("B")

# @decorator
# def func3():
#     print("C")


# write a decorator(logger) that will write smth into a file, write what function was called, at what time it was called,
# with what parameters. Apply it to 3 functions

def logger(function):
    def wrapper(*args, **kwargs):
        import datetime
        with open("log.txt", "a") as file:
            current = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            function(*args, **kwargs)
            file.write(f"Function {function.__name__} was called at {current}\n")
            file.write("----------------------\n")
    return wrapper


@logger
def func1():
    print("Hello there")

@logger
def func2(a, b):
    print(a*b)

@logger
def func3(list_):
    return sum(list_)

# func1()
# func2(1, 4)
# func3([1, 4, 5, 6])


''' unpacking: '''
def func(a, b, c):
    pass


list1 = [1, 3, 4]
tuple1 = (1, 4, 5)
dict1 = {'a': 4, 'b': 7, 'c': 5}

func(*list1)
func(**dict1) #but if you want to unpack a dict and use it's values, the keys have to be the same as the parameter 
#names of the function to which the dictionary is passed

def decorator1(function):
    def wrapper(*args, **kwargs):
        import datetime
        with open("log.txt", "a") as file:
            current = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            result = function(*args, **kwargs)
            file.write(f"Function {function.__name__} was called at {current}\n")
            file.write("----------------------\n")
        return result
    return wrapper

@decorator1
def multiply(i, j):
    return i*j

# what's happening:
# multiply = logger(multiply)
# multiply = wrapper()
'''
то есть, с помощью декоратора враппер сохраняется в функции к которой применяется декоратор
'''

'''write a decorator(timer) that measures how long a function gets executed: '''
# def timer(function):
#     def wrapper(*args, **kwargs):
#         import time
#         start = time.time()
#         result = function(*args, **kwargs)
#         end = time.time()
#         execution_time = end - start
#         print(f"Execution time: {execution_time * 1000} in milliseconds")
#         return execution_time
#     return wrapper

# @timer
# def func1():
#     print("Hello there")

# @timer
# def func2(a, b):
#     print(a*b)

# @timer
# def func3(list_):
#     return sum(list_)

# func1()
# func2(1, 4)
# func3([1, 4, 5, 6, 8, 0])

'''
write a decorator(timer) that measures the average time of how long a function gets executed, when executed n times
'''
def timer(n):
    def decorator(function):
        def wrapper(*args, **kwargs):
            import time
            total_time = 0
            for _ in range(n):
                start = time.time()
                result = function(*args, **kwargs)
                end = time.time()
                execution_time = end - start
                total_time += execution_time

            average_time = total_time / n
            print(f"Average execution time: {average_time * 1000} in milliseconds")
            return result
        return wrapper
    return decorator


@timer(100)
def func1():
    print("Hello there")

@timer(100)
def func2(a, b):
    print(a*b)

@timer(100)
def func3(list_):
    return sum(list_)

func1()
func2(1, 4)
func3([1, 4, 5, 6, 8, 0])

# print(multiply(10, 10))

# def decorator(func):
#     print("I'm a decorator function")

#     def wrapper():
#         print("I'm a wrapper function")
#         print("Calling the function that's being  wrapped")
#         func()
#         print("exiting the function that's being  wrapped")
#         return func

#     return wrapper

# @decorator
# def hello_makers():
#     print("Hello makers")


# hello_makers()

# def check_info(func):
#     def wrapper(param):
#         return func(param).strip()
    
#     return wrapper


# @check_info
# def get_info(param):
#     return param

# param = input('Enter your info: ')
# print(get_info(param))

''' biult-in decorators in django:

@classmethod
@staticmethod
@property
@setter

@login_required
@action
'''