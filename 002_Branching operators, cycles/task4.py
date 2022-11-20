#Задание 1
#Пользователь вводит с клавиатуры два числа. Нужнопосчитать отдельно сумму четных, нечетных и чисел,кратных 9 в указанном диапазоне, а также среднеарифметическое каждой группы.
# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# d = 0
# v=0
# f=0
# for c in range(a,b+1):
#     if c%2==0:
#         d+=c
# print("Sum Even",d)
# avg=d/c
# print("avg even numbers:",avg)
# for c in range(a,b+1):
#     if c%2==1:
#         v+=c
# print("Sum Odd",v)
# avg1=v/c
# print("avg odd numbers:",avg1)
# for c in range(a,b+1):
#     if c%9==0:
#         f+=c
# print("Sum all numbers divisible by 9:",f)
# avg2=f/c
# print("avg odd numbers:",avg2)
#Задание 2
#Пользователь вводит с клавиатуры длину линии исимвол для заполнения линии. Нужно отобразить наэкране вертикальную линию из введенного символа,указанной длины.Например, если было введено 5 и символ %, тогдавывод на экран будет такой:%
# a = int(input("Enter  number:"))
# b = input("Enter symbol number:")
# c=1
# while a+1>c:
#     print(b)
#     c += 1
#Задание 3
#Пользователь вводит с клавиатуры числа. Если числобольше нуля нужно вывести надпись «Number is positive», если меньше нуля «Number is negative», если равно нулю«Number is equal to zero». Когда пользователь вводитчисло 7 программа прекращает свою работу и выводитна экран надпись «Good bye!»
# while True:
#     a = int(input("Enter first number:"))
#     if a == 7:
#         print("«Good bye!")
#         break
#     elif a>0:
#         print("Number is positive")
#     elif a<0:
#         print("Number is negative")
#     elif a == 0:
#         print("Number is equal to zero")
#Задание 4
#Пользователь вводит с клавиатуры числа. Программа должна подсчитывать сумму, максимум и минимум,введенных чисел. Когда пользователь вводит число 7программа прекращает свою работу и выводит на экраннадпись «Good bye!»
d = 0
a = int(input("Enter your number:"))
max = a
min = a
while a!=7:

    a = int(input("Enter your number:"))
    d += a
    if a == 7:
        print("Good Bye")
        break
    if a > max:
        max = a
    if a < min:
        min = a

print("Its bigger >", max)
print("Its smallest >", min)
print("Its Summ >", d)