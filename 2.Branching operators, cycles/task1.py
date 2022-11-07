 #Задание 1
# #Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводитна экран сумму трёх чисел или произведение трёх чисел.
# a = int(input("Enter your first number: "))
# b = int(input("Enter your second number: "))
# c = int(input("Enter your third number: "))
# v = input("What you want\n1.(+)\n2.(*)\nEnter what you want: ")
# if v == "1":
#     print(a+b+c)
# else:
#     print(a*b*c)
#Задание 2
#Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит на экран максимум из трёх, минимум из трёх или среднеарифметическое трёх чисел
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
c = int(input("Enter your third number: "))
v = input("(1).largest number\n(2).smallest number\n(3).Avg\nEnter What you want")
if v == "1":
    if a < b and c < b:
        print("b is bigger ->", b)
    elif b < a and c < a:
        print("a is bigger ->", a)
    else:
        print("c is bigger ->", c)

elif v == "2":
    if a > b and c > b:
        print("b is smallest ->", b)
    elif b > a and c > a:
        print("a is smalles ->", a)
    else:
        print("c is smalles->", c)
elif v == "3":
    print("Avg:",(a+b+c)/3)
# Задание3
#Пользователь вводит с клавиатуры количество метров. В зависимости от выбора пользователя программа переводит метры в мили, дюймы или ярды.
# m = int(input("Enter required number of meters:"))
# print("yards",m * 1.094)
# print("Inch",m * 39.37)
# print("Miles",m / 1609 )