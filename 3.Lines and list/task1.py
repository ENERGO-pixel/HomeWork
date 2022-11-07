#Задание 1
#Пользователь вводит с клавиатуры строку. Проверьтеявляется ли введенная строка палиндромом. Палиндром — слово или текст, которое читается одинаковослева направо и справа налево. Например, кок; А розаупала на лапу Азора; доход; А буду я у дуба.
a = input("Enter what you want:")
c=a.replace(" ","").lower()
a=c
b=(a[::-1])
if a == b:
    print("Это слово или текст палиндром->")
else:
    print("Это слово или текст Не палиндром->")
#Задание 2
#Пользователь вводит с клавиатуры некоторый текст,после чего пользователь вводит список зарезервированныхслов. Необходимо найти в тексте все зарезервированныеслова и изменить их регистр на верхний. Вывести наэкран измененный текст
# name = input("Enter:")
# fname = input("Enter word:")
# c=fname.upper()
# print(name.replace(fname,c))
#Задание 3
#Есть некоторый текст. Посчитайте в этом тексте количество предложений и выведите на экран полученныйрезультат.
# name ="Lorem ipsum dolor sit amet. \n1consectetur adipiscing elit, sed do 3eiusmod tempor incididunt 4ut labore et dolore magna aliqua. \nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. \nExcepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n"
# print(name)
# print("Все предложений:",name.count("."))