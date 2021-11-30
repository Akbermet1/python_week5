''' Polmorphism '''
a = 8
b = 9
c = 8 + 9

str1 = "1"
str2 = "2"
str3 = str1 + str2

# a1 = [1, 3, 4]
# a2 = [9, 0]
# a3 = a1 + a2


class A:
    def __init__(self, attr1):
        self.attr1 = attr1
    
    def __add__(self, other_obj):
        return self.attr1 + other_obj.attr1


a1 = A(10)
a2 = A(30)
res = a1 + a2  
''' + operation was possible to perform because our own class A defined __add__ which
is called when + is used
'''

'''
Functions in python are polymorphic because arguments are not typed
'''

'''any objects that support +'''
def summarize(a, b):
    print(a + b)


''' len(sequence) '''
b1 = "string"
b2 = [1, 2, 3]
b3 = (1, 2, 3)
b4 = {'a': 1, 'b':2}

len(10) # object_name.__len__()

class Office():
    def __init__(self, employees):
        self.employees = employees

    def __len__(self):
        return len(self.employees)


class Square():
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        from math import pi

        return pi*(self.radius**2)

