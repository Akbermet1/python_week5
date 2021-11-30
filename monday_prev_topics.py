# def get_formatted_name(name, middle_name=None ,surname="Wick"):
#     """ Prints a name and a surname """
#     if middle_name:
#         return name + " " + middle_name+ " " + surname
    
#     return name + " " + surname
    

# print(get_formatted_name("John", middle_name="Anthony"))

# m = list(map(int, ['1', '3', '4', '7']))
# print(m)

# a = list(filter(lambda y: y % 2 == 0, [1, 2, 3, 4, 5]))
# print(a)

# d = dict(zip([1, 2, 3], ['a', 'b', 'c']))
# print(d)

# def sum_range(start, end):
#     total = 0

#     if start > end:
#         end, start = start, end

#     return sum(range(start,end +1))

# print(sum_range(7, 1))


# def season(month_number):
#     if month_number < 1 or month_number > 12:
#         raise ValueError(f"There is no month that corresponds with: {month_number}")

#     if month_number == 12 or month_number == 1 or month_number == 2:
#         return "winter"
#     elif month_number >= 3 and month_number <= 5:
#         return "spring"
#     elif month_number >= 6 and month_number <= 8:
#         return "summer"
#     else:
#         return "fall"

# def season_ver2(month_number):
#     if month_number < 1 or month_number > 12:
#         raise ValueError(f"There is no month that corresponds with: {month_number}")

#     if month_number in range(9, 12):
#         return "fall"
#     elif month_number in range(3, 6):
#         return "spring"
#     elif month_number in range(6, 9):
#         return "summer"
#     else:
#         return "winter"

# print(season(8))
# print(season_ver2(3)) 

# comprehention tasks:
#1)
list_numbs = [y for y in range(70, 101) if y % 2]
print(list_numbs)

#3)
names = ["Luke", "Alex", "Tim", "Dominique", "Jameson", "Gregory"]
names_filtered = [name for name in names if len(name) <= 5]
print(names_filtered)

# 4) 
nums = [2, 77, 12, 3, 0, 112, 4, -987]
nums_altered = [num * 2 if num < 5 else num - 2 for num in nums]
print(nums_altered) 

# 5)
# end = int(input("Enter the end of the range: "))
# list_squares = [num*num for num in range(0, end+1)]

# for num in list_squares:
#     print(num)


# 6) 
list_ = [num if num % 2 == 1 else "even" for num in range(1, 11)]
print(list_)


"""7. Дан словарь где ключами являются фрукты, а значением их цены. При помощи dict comprehension создайте
новый словарь где будут только те элементы, значение которых будет чётным."""

fruits = {'apple': 25, 'banana': 40, 'mango': 17, 'orange': 12}
fruits_even = {key: value for key, value in fruits.items() if value % 2 == 0}
print(fruits_even)

"""8. Дан словарь 'a' в котором значениями являются целые числа. Пройдитесь по элементам и запишите в dict_
значения в виде списка чисел от 1 до числа, которое является значением."""

a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}

dict_ = {key: list(range(1, value + 1)) for key, value in a.items()}
print(dict_)