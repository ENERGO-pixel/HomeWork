import pymysql
import os.path
import json
try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="IDSharapo_ff220601",
        database="trash",
        cursorclass=pymysql.cursors.DictCursor)
    print("Okay")
    try:
        # Create DATABASE
        # with connection.cursor() as cursor:
        #     create_table = "CREATE DATABASE `trash`"
        #     cursor.execute(create_table)
        # Create table
        # with connection.cursor() as cursor:
        #     create_table = "CREATE TABLE `User` (id int AUTO_INCREMENT, name varchar(30),password varchar(100), PRIMARY KEY (id));"
        #     cursor.execute(create_table)
        #     print("well done")
        #Create table
        # with connection.cursor() as cursor:
        #     create_table = "CREATE TABLE `friends` (id int AUTO_INCREMENT, name varchar(30),surname varchar(30), PRIMARY KEY (id));"
        #     cursor.exewcute(create_table)
        #     print("well done")

        v=input("1.(Log in)\n2.(Sign in)\n")
        #Insert data
        if v=="2":
            login=input("Enter login: ")
            password=input("Enter password: ")
            with connection.cursor() as cursor:
                insert = f"INSERT INTO `User` (name,password) VALUES ('{login}','{password}')"
                cursor.execute(insert)
                connection.commit()
                while True:
                    th = input("Do you want add exponat to your Museim?(Yes or No.Show,Delete,Update,Clear,Find): ")
                    if th == "No":
                        break
                    if th == "Yes":
                        # Insert data
                        name = input("Enter what you want add: ")
                        surname = input("Enter surname: ")
                        with connection.cursor() as cursor:
                            insert = f"INSERT INTO `friends` (name, surname) VALUES ('{name}','{surname}')"
                            cursor.execute(insert)
                            connection.commit()
                    if th == "Show":
                        with connection.cursor() as cursor:
                            select_all = f"select * from trash.friends"
                            cursor.execute(select_all)
                            result = cursor.fetchall()
                            for row in result:
                                print(row)
                    if th == "Delete":
                        with connection.cursor() as cursor:
                            dele=input("Enter thing what you want delete: ")
                            select_all = f"DELETE FROM `friends` WHERE name='{dele}';"
                            cursor.execute(select_all)
                            result = cursor.fetchall()
                            for row in result:
                                print(row)
                    if th == "Update":
                        with connection.cursor() as cursor:
                            namee=input("Enter thing what you want update: ")
                            idd=int(input("and id is frinds: "))
                            select_all = f"UPDATE `friends` SET name = '{namee}' WHERE id ={idd} ;"
                            cursor.execute(select_all)
                            result = cursor.fetchall()
                            for row in result:
                                print(row)
                    if th=="Find":
                        with connection.cursor() as cursor:
                            na=input("Enter name thing to find:")
                            select_all = f"select * from trash.friends where name='{na}'"
                            cursor.execute(select_all)
                            result = cursor.fetchall()
                            for row in result:
                                print(row)
        # # Select data
        if v=="1":
            conflogin=input("Enter login: ")
            confpassword=input("Enter password: ")
            with connection.cursor() as cursor:
                select_all = f"select * from trash.user where name='{conflogin}' and password ='{confpassword}'"
                cursor.execute(select_all)
                result = cursor.fetchall()
                for row in result:
                    print(row)
                    while True:
                        th = input(
                            "Do you want add friend to your friendlist?(Yes or No.Show,Delete,Update,Clear,Find): ")
                        if th == "No":
                            break
                        if th == "Yes":
                            # Insert data
                            name = input("Enter name: ")
                            surname = input("Enter surname: ")
                            with connection.cursor() as cursor:
                                insert = f"INSERT INTO `friends` (name, surname) VALUES ('{name}','{surname}')"
                                cursor.execute(insert)
                                connection.commit()
                        if th == "Show":
                            with connection.cursor() as cursor:
                                select_all = f"select * from trash.friends"
                                cursor.execute(select_all)
                                result = cursor.fetchall()
                                for row in result:
                                    print(row)
                        if th == "Delete":
                            with connection.cursor() as cursor:
                                dele = input("Enter thing what you want delete: ")
                                select_all = f"DELETE FROM `friends` WHERE name='{dele}';"
                                cursor.execute(select_all)
                                result = cursor.fetchall()
                                for row in result:
                                    print(row)
                        if th == "Update":
                            with connection.cursor() as cursor:
                                namee = input("Enter thing what you want update: ")
                                idd = int(input("and id is frinds: "))
                                select_all = f"UPDATE `friends` SET name = '{namee}' WHERE id ={idd} ;"
                                cursor.execute(select_all)
                                result = cursor.fetchall()
                                for row in result:
                                    print(row)
                        if th == "Find":
                            with connection.cursor() as cursor:
                                na = input("Enter name thing to find:")
                                select_all = f"select * from trash.friends where name='{na}'"
                                cursor.execute(select_all)
                                result = cursor.fetchall()
                                for row in result:
                                    print(row)
        # Drope table
        # with connection.cursor() as cursor:
        #     create_table = "DROP TABLE `things`"
        #     cursor.execute(create_table)

    finally:
        connection.close()
except Exception as error:
        print(error)