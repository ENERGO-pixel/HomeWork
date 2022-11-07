#Задание 1
#Створіть програму, що містить інформацію про відомихбаскетболістів. Збережіть ПІБ та зріст кожного баскетболіста. Реалізуйте можливість додавати, видаляти, знаходити тазмінювати дані. Використовуйте словник для збереженняінформації.
dict = {
    "LeBron James": "190sm",
    "Kareem Abdul-Jabbar": "192sm",
    "Shaquille O'Neal": "185sm",
    "Michael Jordan": "200sm"
}
print(dict)
v= input("What you want\n1.(Find)\n2.(Delete)\n3.(Add)\n4.(replace)\n:")


if v=="1":
        a=input("Find your man")
        print(dict.get(a))
elif v=="2":
        c=input("Delete any gamer")
        dict.pop(c)
        print(dict)
elif v=="3":
        d=input("Add any gamers")
        f=input("Add growth")
        dict[d]=f
        print(dict)
elif v=="4":
    con=input("Replace any gamers")
    f=input("Add any gamers")
    l = input("And growth")
    dict.pop(con)
    dict[f]=l
    print(dict)
#Задание 2
#Створіть програму «Англо-французький словник». Збережіть слово англійською та його переклад на французьку.Реалізуйте можливість додавати, видаляти, знаходити тазмінювати дані. Використовуйте словник для збереженняінформації.
# dict = {
#     "Hello": "Bonjour",
#     "Cat": "Chat",
#     "Tree": "arbre",
#     "Window": "la fenêtre",
#     "Human": "Humaine"
# }
# print(dict)
# v= input("What you want\n1.(Find)\n2.(Delete)\n3.(Add)\n4.(replace)\n:")
#
#
# if v=="1":
#         a=input("Find your word")
#         print(dict.get(a))
# elif v=="2":
#         c=input("Delete any word")
#         dict.pop(c)
#         print(dict)
# elif v=="3":
#         d=input("Add any words")
#         f=input("And translate in french")
#         dict[d]=f
#         print(dict)
# elif v=="4":
#     con=input("Replace any words")
#     f=input("Add any words")
#     l = input("And translate in french")
#     dict.pop(con)
#     dict[f]=l
#     print(dict)
#Задание 3
#Створіть програму «Фірма», яка зберігає інформацію про працівників: ПІБ, телефон, корпоративний email, назва посади, номер кабінету, Skype. Реалізуйте можливість додавати, видаляти, знаходити та змінювати дані. Використовуйте словник для збереження інформації.
# dict={}
# v=0
# while(v!=7):
#     v= input("What you want\n1.(Find)\n2.(Delete)\n3.(Add)\n4.(replace)\n:")
#     if v=="1":
#         c=input("Find Name")
#         f=input("what you want see 1.(phone number)\n2.(email)\n3.(position)\n4.(cabinet)\n5.(skype)")
#         if f=="1":
#             print("Phone:",dict[c]["phone number"])
#         elif f == "2":
#             print("email:", dict[c]["email"])
#         elif f == "3":
#             print("position:", dict[c]["position"])
#         elif f == "4":
#             print("cabinet:", dict[c]["cabinet"])
#         elif f == "5":
#             print("skype:", dict[c]["skype"])
#     elif v=="2":
#         c = input("Enter name")
#         f = input("what you want delete 1.(phone number)\n2.(email)\n3.(position)\n4.(cabinet)\n5.(skype)\n6.(all)")
#         if f == "1":
#             dict[c]["phone number"]=""
#         elif f == "2":
#             dict[c]["email"]=""
#         elif f == "3":
#             dict[c]["position"]=""
#         elif f == "4":
#             dict[c]["cabinet"]=""
#         elif f == "5":
#             dict[c]["skype"]=""
#         elif f == "6":
#             dict.pop(c)
#     elif v=="3":
#             d=input("Add any name")
#             f=input("Add  phone number")
#             h=input("Add email")
#             cub=input("Add cub")
#             nam=input("Add position")
#             skype=input("Add skype")
#             dict[d]={"phone number":f,"email":h,"position":nam,"cabinet":cub,"skype":skype}
#             print(dict)
#     elif v=="4":
#         c = input("Enter Name")
#         f = input("what you want replace 1.(phone number)\n2.(email)\n3.(position)\n4.(cabinet)\n5.(skype)")
#         if f == "1":
#             d=input("Enter phone  number")
#             dict[c]["phone number"]=d
#             print(dict)
#         elif f == "2":
#             d = input("Enter email")
#             dict[c]["email"] = d
#             print(dict)
#         elif f == "3":
#             d = input("Enter position")
#             dict[c]["position"] = d
#             print(dict)
#         elif f == "4":
#             d = input("Enter cabinet")
#             dict[c]["cabinet"] = d
#             print(dict)
#         elif f == "5":
#             d = input("Enter skype")
#             dict[c]["skype"] = d
#             print(dict)
#Завдання 4
#Створіть програму «Книжкова колекція», яка зберігає інформацію про книги: автор, назва книги, жанр, рік випуску, кількість сторінок, видавництво. Реалізуйте можливість додавати, видаляти, знаходити та змінювати дані. Використовуйте словник для збереження інформації.
# dict={}
# v=0
# while(v!=7):
#     v= input("What you want\n1.(Find)\n2.(Delete)\n3.(Add)\n4.(replace)\n:")
#     if v=="1":
#         c=input("Find author Name")
#         f=input("what you want see 1.(name book)\n2.(genre)\n3.(graduation year)\n4.(number of pages)\n5.(publishing house)")
#         if f=="1":
#             print("name book:",dict[c]["name book"])
#         elif f == "2":
#             print("genre:", dict[c]["genre"])
#         elif f == "3":
#             print("graduation year:", dict[c]["graduation year"])
#         elif f == "4":
#             print("number of pages:", dict[c]["number of pages"])
#         elif f == "5":
#             print("publishing house:", dict[c]["publishing house"])
#     elif v=="2":
#         c = input("Enter name")
#         f = input("what you want delete 1.(name book)\n2.(email)\n3.(graduation year)\n4.(number of pages)\n5.(publishing house)\n6.(all)")
#         if f == "1":
#             dict[c]["name book"]=""
#         elif f == "2":
#             dict[c]["genre"]=""
#         elif f == "3":
#             dict[c]["graduation year"]=""
#         elif f == "4":
#             dict[c]["number of pages"]=""
#         elif f == "5":
#             dict[c]["publishing house"]=""
#         elif f == "6":
#             dict.pop(c)
#     elif v=="3":
#             d=input("Add any name")
#             f=input("Add  name book")
#             h=input("Add genre")
#             cub=input("Add number of pages")
#             nam=input("Add graduation year")
#             skype=input("Add publishing house")
#             dict[d]={"name book":f,"genre":h,"graduation year":nam,"number of pages":cub,"publishing house":skype}
#             print(dict)
#     elif v=="4":
#         c = input("Enter Name")
#         f = input("what you want replace 1.(name book)\n2.(genre)\n3.(graduation year)\n4.(number of pages)\n5.(publishing house)")
#         if f == "1":
#             d=input("Enter name book")
#             dict[c]["name book"]=d
#             print(dict)
#         elif f == "2":
#             d = input("Enter genre")
#             dict[c]["genre"] = d
#             print(dict)
#         elif f == "3":
#             d = input("Enter graduation year")
#             dict[c]["graduation year"] = d
#             print(dict)
#         elif f == "4":
#             d = input("Enter number of pages")
#             dict[c]["number of pages"] = d
#             print(dict)
#         elif f == "5":
#             d = input("Enter publishing house")
#             dict[c]["publishing house"] = d
#             print(dict)