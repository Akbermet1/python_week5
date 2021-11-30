'''OOP: Inheritance'''

'''
the fuction super()   -> returns all methods of the immediate parent class
'''

"""parent classes are also called super class"""
class A:
    attr1 = 'a'

    def method1(self):
        print("Hello")


"""child classes are also called subclass class"""
class B(A):
    pass

'''
isinstance() -> checks if an object is an object/instance of a class
issubclass() -> checks if a class is a subclass of another class
type()
'''

'''
subclasses can redeclare attributes and methods that they inherited

subclasses can also extend inherited methods 
'''

class C:
    attr1 = "a"

    def method1(self):
        print("AAAAA")

    def method2(self):
        return self.attr1.upper()


class D(C):
    attr1 = 'b'

    def method1(self):
        print("AAAA")

    def method2(self):
        res_a = super().method2()
        # you can extend the logic by adding more steps/actions, e.g.:
        return res_a + 'B'

'''
NOTE: when declaring classes on the same level, leave 2 empty lines between them,
and 1 empty line between methods
'''

class AA():
    attr1 = "a"


class BB(AA):
    attr1 = "b"


class CC(BB):
    attr1 = "c"


class DD(CC):
    attr1 = "d"


class Engine:
    def __init__(self, fuel, volume, power):
        self.fuel = fuel
        self.volume = volume
        self.power = power


v8 = Engine("gasoline", 5, 350)
v6 = Engine("diesel", 3, 200)


class Car():
    def __init__(self, model: str, year: int, color: str, engine: Engine):
        self.model = model
        self.year = year
        self.color = color
        self.engine = engine

car1 = Car("Toyota Camry", 2009, "black", v8)


class Category():
    def __init__(self, name, id):
        self.name = name
        self.id = id


category1 = Category("electronics", 1)
category2 = Category("appliances", 2)

class Product():
    def __init__(self, name, description, price, category):
        self.name = name
        self.description = description
        self.price = price
        self.category = category


p1 = Product("Apple watch", "...", 1000, category1)
p2 = Product("Bosch blender", "...", 4500, category2)


class User():
    def __init__(self, email, address, phone_number):
        self.email = email
        self.address = address
        self.phone_number = phone_number

user1 = User("blabla@gmail.com", "Avenue str. 133", "99677711666")


class Order():
    def __init__(self, id, user, date, total_sum, products):
        self.id = id
        self.user = user
        self.date = date
        self.total_sum = total_sum

order1 = Order(1, user1, "10.11.2022 18:30")


class OrderItem():
    def __init__(self, order_id, product, quantity):
        self.order_id = order_id
        self.product = product
        self.quantity = quantity

order_item1 = OrderItem(order1.id, p1, 2)
order_item2 = OrderItem(order1.id, p2, 4)



'''----------------------------------------------------------'''


class V:
    instance_count = 0
    # __new__ creates objects
    def __new__(class_):
        class_.instance_count += 1
        return super().__new__(class_)

v1 = V()
v2 = V()
print(V.instance_count) # 2

'''
what happens when?????:
def func(list_ = [])
'''