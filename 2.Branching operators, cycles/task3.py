#Задание 1
#Пользователь вводит с клавиатуры два числа (начало и конец диапазона). Требуется проанализировать всечисла в этом диапазоне по следующему правилу: есличисло кратно 7, его надо выводить на экран.
# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# for c in range(a,b+1):
#     if c%7==0:
#         print(c)
#Задание 2
#Пользователь вводит с клавиатуры два числа (начало и конец диапазона). Требуется проанализировать всечисла в этом диапазоне. Нужно вывести на экран:\#2. Все числа диапазона в убывающем порядке;#3. Все числа, кратные 7;#4. Количество чисел, кратных 5.
# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# v = input("1.(all numbers)\n2.(all numbers appear in descending order\n3.(all numbers divisible by 7)\n4.(Number of multiples of 5)\nEnter what you want:")
# if v == "1":
#  for c in range(a,b+1):
#         print(c)
# elif v == "2":
#     if a<b:
#         for c in range(b, a - 1,-1):
#             print(c)
#     elif b<a:
#         for c in range(a, b - 1,-1):
#             print(c)
# elif v == "3":
#     for c in range(a, b + 1):
#         if c%7==0:
#             print(c)
# elif v == "4":
#     d=0
#     for c in range(a, b +1):
#         if c % 5 == 0:
#             d+=1
#     print(d)
#Задание 3
#Пользователь вводит с клавиатуры два числа (началои конец диапазона). Требуется проанализировать все числав этом диапазоне. Вывод на экран должен проходить поправилам, указанным ниже.Если чсло кратно 3 (делится на 3 без остатка) нужновывести слово Fizz. Если число кратно 5 нужно выве
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
for c in range(a,b+1):
        if c%5==0 and c%3==0:
            print(c,"Fizz Buzz")
        elif c%3==0:
            print(c,"Fizz")
        elif c%5==0:
            print(c,"Buzz")
        else:
            print(c)