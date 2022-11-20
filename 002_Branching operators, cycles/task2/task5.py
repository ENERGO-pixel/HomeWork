#Homework
#Задание1
# a = int(input("Enter First  number:"))
# b = int(input("Enter  Second number:"))
# print("a ^ b =",a**b)
#Задание2
# col = 0
# v,b,d=0,0,0
# for c in range(100,999):
#     v=(c // 100) % 10
#     b=(c // 10)%10
#     d=(c % 10)
#     if v == b:
#         col += 1
#     elif b == d:
#         col +=1
#     elif d == v:
#         col+=1
# print(col)
# #Задание3
# col = 0
# v,b,d,f=0,0,0,0
# for c in range(100,9999):
#     f=(c//1000)
#     v=(c // 100) % 10
#     b=(c // 10)%10
#     d=(c % 10)
#     if d !=b and d!=v and d!=f and d!=0:
#         col += 1
#
# print(col)
#Задание4
a = input("Enter   number:")
b = ""
for i in a:
    if i!="6" and i!="3":
        b=b+i
print(b)