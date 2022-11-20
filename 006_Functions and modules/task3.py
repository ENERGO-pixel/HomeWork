# Написать рекурсивную функцию нахождения наи-
# большего общего делителя двух целых чисел.
from random import randint
# def dela(a, b):
#     # rannum = [randint(1, 50) for i in range(1)]
#     while a != 0 and b != 0:
#         if a > b:
#            a = a % b
#         elif a < b:
#             b= b % a
#     return (a + b)
# print(dela(int(input("Take number 1: ")),(int(input("Take number 2: ")))))
#
# def nds(a, b):
#     # rannum = [randint(1, 50) for i in range(1)]
#     if (b == 0):
#         return a
#     if a > b:
#        return nds(b, a % b)
#     else:
#         return nds(a, b % a)
# print(dela(int(input("Take number 1: ")),(int(input("Take number 2: ")))))

# Написать игру «Быки и коровы». Программа «за-
# гадывает» четырёхзначное число и играющий должен
# угадать его. После ввода пользователем числа программа
# сообщает, сколько цифр числа угадано (быки) и сколько
# цифр угадано и стоит на нужном месте (коровы). После
# отгадывания числа на экран необходимо вывести коли-
# чество сделанных пользователем попыток. В программе
# необходимо использовать рекурсию.

# def game(a,b):
#     rannum = [randint(1, 9) for i in range(a)]
#     count, count2 = 0, 0
#     print(rannum)
#     sty = [b,b,b,b]
#     print(sty)
#     while count != 4:
#         adnum = int(input("Take number! "))
#         if adnum in rannum:
#            print(sty)
#            sty.remove(b)
#            sty.append(adnum)
#            print("Number in case try again!")
#            count += 1
#            # sty.remove()
#         elif adnum == rannum:
#             print("Success! - ", rannum)
#             break
#         elif adnum not in rannum:
#            print(sty)
#            print("Don't number in case try again!")
#            count2 += 1
#         else:
#               print("Game is over")
#     print("Count for right try!", count)
#     print("Count for false try!", count2)
#     print("Number is - ", rannum)
# game(int(input("Take count number?: ")),input("Take symbol: "))
# from random import randint
# def korov(magik, count):
#     count1,count2 = 0,0
#     print(magik)
#     string = input("enter your number: ")
#     if string == str(magik):
#         return count
#     else:
#          for i in string:
#              if i in str(magik):
#                  count1 += 1
#                  print(i)
#              else:
#                  count2 += 1
#          print("Count for right try: ", count1)
#          print("Count for false try: ", count2)
#          return korov(magik, count+1)
# print(korov(([randint(1000, 9999)]), 0))

# Игра Пятнашки
#
# from random import randint
#
# nl = [1,2,3,4,5,6,7,8]
# nl.insert(randint(1,8)," ")
# move = " "
# fl = [1,2,3,4,5,6,7,8," "]
# while move != "5":
#     count = 0
#     for i in nl:
#        print(i, end=" ")
#        count += 1
#        if count % 3 == 0:
#           print(end="\n")
#     if nl != fl:
#       move = input("Where you want to move? : 1 - Up, 2 - Down, 3 - Left, 4 - Right!, 5 - Exit! - ")
#       if move == "1":
#             nl_ind = nl.index(" ")
#             if nl_ind != 0 and nl_ind != 1 and nl_ind != 2:
#                 number = nl[nl_ind - 3]
#                 nl[nl_ind] = number
#                 nl[nl.index(number)] = " "
#       elif move == "2":
#             nl_ind = nl.index(" ")
#             if nl_ind != 6 and nl_ind != 7 and nl_ind != 8:
#                 number = nl[nl_ind + 3]
#                 nl[nl_ind + 3] = " "
#                 nl[nl_ind] = number
#       elif move == "3":
#             nl_ind = nl.index(" ")
#             if nl_ind != 0 and nl_ind != 3 and nl_ind != 6:
#                 number = nl[nl_ind - 1]
#                 nl[nl_ind] = number
#                 nl[nl.index(number)] = " "
#       elif move == "4":
#             nl_ind = nl.index(" ")
#             if nl_ind != 2 and nl_ind != 5 and nl_ind != 8:
#                 number = nl[nl_ind + 1]
#                 nl[nl_ind + 1] = " "
#                 nl[nl_ind] = number
#     else:
#         print("You win! ")
#         break