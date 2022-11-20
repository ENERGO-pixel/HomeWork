#Задание 1
#дание 1 Необходимо отсортировать первые две трети списка в порядке возрастания, если среднее арифметическое всех элементов больше нуля; иначе — лишь первую треть. Остальную часть списка не сортировать, а расположить в обратном порядке.
from random import randint
numb = [randint(10,100)for i in range(10)]
d=sum(numb)/len(numb)
print(numb)
print("Avg:",sum(numb)/len(numb))
if d > 0:
    m = len(numb)//3
    left_part = numb[:m]
    center_part = numb[m:m+m]
    right_part=numb[m+m:]
    print("1/3",left_part)
    print("2/3",center_part)
    print("3/3",right_part)
for i in range(len(left_part)-1):
    for j in range(len(left_part)-i-1):
        if left_part[j] < left_part[j+1]:
            number=left_part[j]
            left_part[j]=left_part[j+1]
            left_part[j+1]=number
print(left_part)
for i in range(len(center_part)-1):
    for j in range(len(center_part)-i-1):
        if center_part[j] < center_part[j+1]:
            number=center_part[j]
            center_part[j]=center_part[j+1]
            center_part[j+1]=number
print(center_part)
better_part=left_part+center_part
for i in range(len(better_part)-1):
    for j in range(len(better_part)-i-1):
        if better_part[j] < better_part[j+1]:
            number=better_part[j]
            better_part[j]=better_part[j+1]
            better_part[j+1]=number
print(better_part + right_part)
#Задание 2
#Написать программу «успеваемость». Пользователь вводит 10 оценок студента. Оценки от 1 до 12. Реализовать меню для пользователя: ■ Вывод оценок (вывод содержимого списка); ■ Пересдача экзамена (пользователь вводит номер элемента списка и новую оценку); ■ Выходит ли стипендия (стипендия выходит, если средний бал не ниже 10.7); ■ Вывод отсортированного списка оценок: по возрастанию или убыванию
# list = [int(input("Enter your mark (1-12):")) for i in range(10)]
# v=input("1.(Show all marks)\n2.(retake exame)\n3.(Stependiya)\n4.(sort your marks)\nEnter what you want:")
# if v=="1":
#     print(list)
# elif v=="2":
#     c = int(input("Input place your estimate:"))
#     f = int(input("Input what estimate you want:"))
#     list[c - 1] = f
# elif v=="3":
#     if sum(list)/len(list)>10.7:
#         print("Ye Stependii")
#     else:
#         print("Nema Stependiya")
# elif v =="4":
#     for i in range(len(list)-1):
#         for j in range(len(list)-i-1):
#             if list[j] < list[j+1]:
#                 number=list[j]
#                 list[j]=list[j+1]
#                 list[j+1]=number
# print(list)
# from random import randint
# numb = [randint(10,100)for i in range(10)]
# for i in range(len(numb) - 1):
#     sorted_check = True
#     for j in range(len(numb) - i - 1):
#         if numb[j] < numb[j + 1]:
#             number = numb[j]
#             numb[j] = numb[j + 1]
#             numb[j + 1] = number
#             sorted_check = False
#     if sorted_check== True:
#         break
# print(numb)