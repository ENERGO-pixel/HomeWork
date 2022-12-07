import telebot
import math
import webbrowser
import json
import os.path
import pymysql
from selenium import webdriver
import time
import os.path
from selenium.webdriver.common.by import By

from telebot import types
autoriz=False
def menu(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('/calc')
    button2 = types.KeyboardButton('/animals')
    button3 = types.KeyboardButton('/count')
    button4 = types.KeyboardButton('/happy')
    button5 = types.KeyboardButton('/statistic')
    button6 = types.KeyboardButton('/commands')
    button7 = types.KeyboardButton('/register')
    button8 = types.KeyboardButton('/auto')
    button9= types.KeyboardButton('/mail')
    keyboard.add(button1,button2,button3,button4,button5,button6,button7,button8,button9)
    botler.send_message(message.chat.id,'Menu:',reply_markup=keyboard)
try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="IDSharapo_ff220601",
        database="Salesfor",
        cursorclass=pymysql.cursors.DictCursor )
    print("Okay")
    try:
        config = {
            'name': 'BotinokForWorklast_bot',
            'token': '5407267874:AAFfMP8CgzCDRB0QYTgYnLCgD8cllKUzgj8'
        }
        botler = telebot.TeleBot(config['token'])

        @botler.message_handler(commands=['start'])
        def start(message):
            menu(message)


        @botler.message_handler(content_types=['text'])
        def get_text(message):
            # Create table
            # with connection.cursor() as cursor:
            #     create_table = "CREATE TABLE `Userauto` (id int AUTO_INCREMENT, name varchar(30),password varchar(100), PRIMARY KEY (id));"
            #     cursor.execute(create_table)
            #     print("well done")
            if message.text == "/auto":
                if not autoriz:
                    c=botler.send_message(message.chat.id, "Enter login and pussword: ")
                    botler.register_next_step_handler(c, auto)
                else:
                    botler.send_message(message.chat.id, "You already authorized")
            elif message.text == "/register":
                if not autoriz:
                    c=botler.send_message(message.chat.id, "Enter login and pussword: ")
                    botler.register_next_step_handler(c, register)
                else:
                    botler.send_message(message.chat.id, "You already authorized")
            elif autoriz:
                if message.text == "/commands":
                    botler.send_message(message.chat.id, "Its you command")
                    botler.send_message(message.chat.id, "/animals")
                    botler.send_message(message.chat.id, "/calc")
                    botler.send_message(message.chat.id, "/count")
                    botler.send_message(message.chat.id, "/happy")
                    botler.send_message(message.chat.id, "/statistic")
                if message.text =="/mail":
                    d=botler.send_message(message.chat.id,"Enter mail,theme,message")
                    botler.register_next_step_handler(d,mail)
                if message.text =="/happy":
                    d = botler.send_message(message.chat.id, "Enter what you want")
                    botler.register_next_step_handler(d, happy)
                if message.text == "/statistic":
                    d = botler.send_message(message.chat.id, "Enter what you want")
                    botler.register_next_step_handler(d, statistic)
                if message.text =="Hello":
                    botler.send_message(message.chat.id,"hello user!")
                if message.text == "/calc":
                    a=botler.send_message(message.chat.id, "Enter what you want")
                    botler.register_next_step_handler(a,cal)
                if message.text == "/count":
                    b=botler.send_message(message.chat.id, "Enter what you want")
                    botler.register_next_step_handler(b,count)
                if message.text == "/register":
                    login = botler.send_message(message.chat.id, "Enter name and password: ")
                    botler.register_next_step_handler(login, register)
                if message.text == "/animals":
                    c = botler.send_message(message.chat.id, "Enter what you want")
                    botler.register_next_step_handler(c, animals)
            else:
                    botler.send_message(message.chat.id, "You are not login")
                    botler.send_message(message.chat.id, "/auto")
                    botler.send_message(message.chat.id, "/register")
        def mail(message):
            driver = webdriver.Chrome(executable_path=r"C:\Users\sergs\PycharmProjects\Selenium\chromedriver.exe")
            list = message.text.split(",")
            try:
                driver.get(url="https://outlook.office.com/mail/")
                time.sleep(1)
                login = driver.find_element(By.CSS_SELECTOR, '#i0116')
                login.send_keys("YourMail")#Your Mail
                time.sleep(1)
                button = driver.find_element(By.XPATH, '''//*[@id="idSIButton9"]''')
                button.click()
                time.sleep(1)
                password = driver.find_element(By.CSS_SELECTOR, '#i0118')
                password.send_keys("Your password")#Your password
                button = driver.find_element(By.XPATH, '''//*[@id="idSIButton9"]''')
                button.click()
                time.sleep(1)
                button = driver.find_element(By.XPATH, '''//*[@id="idSIButton9"]''')
                button.click()
                time.sleep(5)
                button1 = driver.find_element(By.XPATH,
                                              '''//*[@id="innerRibbonContainer"]/div[1]/div/div/div/div[2]/div/div/span/button[1]''')
                button1.click()
                time.sleep(5)

                email = driver.find_element(By.XPATH,
                                            '''//*[@id="docking_InitVisiblePart_0"]/div/div[1]/div[1]/div/div[4]/div/div/div[1]''')
                email.send_keys(list[0])
                time.sleep(1)
                theme = driver.find_element(By.XPATH,
                                            '''/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[3]/div[3]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div/input''')
                theme.send_keys(list[1])
                time.sleep(1)
                mail = driver.find_element(By.XPATH, '//*[@id="editorParent_1"]/div')
                mail.send_keys(list[2])
                time.sleep(2)
                button2 = driver.find_element(By.XPATH,
                                              '''//*[@id="docking_InitVisiblePart_0"]/div/div[3]/div[3]/div[1]/div/div/span/button[1]''')
                button2.click()
                time.sleep(1)
            except Exception as error:
                print(error)

            finally:
                driver.close()
                driver.quit()
        def register(message):
            list = message.text.split(" ")
            with connection.cursor() as cursor:
                select_all = f"select * from Salesfor.userauto where name='{list[0]}' and password ='{list[1]}'"
                cursor.execute(select_all)
                result = cursor.fetchall()
                try:
                    if result[0].get('name') == list[0] and result[0].get('password') == list[1]:
                        botler.send_message(message.chat.id, "Account is already created")
                except:
                    botler.send_message(message.chat.id, "Account is already created")
                insert = f"INSERT INTO `Userauto` (name,password) VALUES ('{list[0]}','{list[1]}')"
                cursor.execute(insert)
                connection.commit()
                botler.send_message(message.chat.id, "Good")
        def auto(message):
            list = message.text.split(" ")
            with connection.cursor() as cursor:
                select_all = f"select * from Salesfor.userauto where name='{list[0]}' and password ='{list[1]}'"
                cursor.execute(select_all)
                result = cursor.fetchall()
                try:
                    if result[0].get('name')==list[0] and result[0].get('password')==list[1]:
                        global autoriz
                        autoriz = True
                        botler.send_message(message.chat.id, "Login success")
                    else:
                        botler.send_message(message.chat.id, "Login Error")
                except:
                    botler.send_message(message.chat.id, "Login or password is failed")
                # botler.send_message(message.chat.id, result)
                # print(result)
        def statistic(message):
            vowels=['a', 'e', 'i', 'o', 'u', 'y']
            consonants=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
            symbols=['!','?','.',',']
            b = 0
            path=os.path.join("Botl","bot.json")
            for i in message.text.split(" "):
                b += 1
            file=open(path,"a")
            json.dump("Words:"+str(b),file)
            #botler.send_message(message.chat.id,"Words:"+str(b))
            a=message.text.replace(" ","")
            a=len(a)
            file = open(path, "a")
            json.dump("Symbols:" +str(a), file)
            #botler.send_message(message.chat.id, "Symbols:" +str(a) )
            vo=0
            bo = message.text.lower()
            for i in bo:
                if i in vowels:
                    vo+=1
            file = open(path, "a")
            json.dump("vowels:" + str(vo), file)
            #botler.send_message(message.chat.id, "vowels:" + str(vo))
            co = 0
            for i in bo:
                if i in consonants:
                    co += 1
            file = open(path, "a")
            json.dump("consonants:" + str(co), file)
            #botler.send_message(message.chat.id, "consonants:" + str(co))
            mark = 0
            for i in bo:
                if i in symbols:
                    mark += 1
            file = open(path, "a")
            json.dump("punctuation marks:" + str(mark), file)
            #botler.send_message(message.chat.id, "punctuation marks:" + str(mark))
            d = 0
            c = 0
            list = []
            for i in message.text:
                if i.isdigit():
                    list.append(int(i))
            for i in list:
                if i % 2 == 0:
                    d += 1
                else:
                    c += 1
            file = open(path, "a")
            json.dump("even:" + str(d), file)
            file = open(path, "a")
            json.dump("odd:" + str(c), file)
            file = open(path, "r")
            botler.send_document(message.chat.id,file)
            #botler.send_message(message.chat.id, "even:" + str(d))
            #botler.send_message(message.chat.id, "odd:" + str(c))
        def happy(message):
            if len(message.text)==8:
                b = int(message.text) // 10000
                one = b // 1000
                two = (b // 100) % 10
                three = (b // 10) % 10
                four = b % 10
                c = int(message.text) % 10000
                five = c // 1000
                six = (c // 100) % 10
                seven = (c // 10) % 10
                eight = c % 10
                if (one + two + three + four) == (five + six + seven + eight):
                    botler.send_message(message.chat.id, "Happy")
                else:
                    botler.send_message(message.chat.id,"Unhappy")
            if len(message.text)==6:
                b = int(message.text) // 1000
                one = b // 100
                two = b % 11
                three = b % 10
                c = int(message.text) % 1000
                four = c // 100
                five = c % 11
                six = c % 10
                if (one + two + three) == (four + five + six):
                    botler.send_message(message.chat.id,"Happy")
                else:
                    botler.send_message(message.chat.id,"Unhappy")
        def cal(message):
                if "+" in message.text:
                    st=message.text
                    message.text = message.text.split("+")
                    message.text = list(map(int, message.text))
                    a=(sum(message.text))
                    botler.send_message(message.chat.id,st+"="+str(a))
                if "*" in message.text:
                    st2 = message.text
                    message.text = message.text.split("*")
                    message.text = list(map(int, message.text))
                    a = (math.prod(message.text))
                    botler.send_message(message.chat.id,st2+"="+str(a))
                if "-" in message.text:
                    st3 = message.text
                    message.text = message.text.split("-")
                    message.text = list(map(int, message.text))
                    a = message.text[0]-message.text[1]
                    botler.send_message(message.chat.id,st3+"="+str(a))
                if "/" in message.text:
                    st4 = message.text
                    message.text = message.text.split("/")
                    message.text = list(map(int, message.text))
                    a = message.text[0] / message.text[1]
                    botler.send_message(message.chat.id,st4+"="+str(a))
        def count(message):
            b = 0
            for i in message.text.split(" "):
                b += 1
            botler.send_message(message.chat.id, b)
        def animals(message):
            if message.text == "Cat":
                a = webbrowser.open('https://cdn.britannica.com/39/7139-050-A88818BB/Himalayan-chocolate-point.jpg')
                botler.send_message(message.chat.id, str(a))
            if message.text == "Dog":
                # b=webbrowser.open('http://t0.gstatic.com/licensed-image?q=tbn:ANd9GcRqMbXvdztEAKJMI7MtP0RuM6rYlOQ1TmLL8vBIGj_PLM0hgE_4ua7_Tw9rtFaBQSAEPXcZEyuYrniOmuA')
                botler.send_message(message.chat.id,'http://t0.gstatic.com/licensed-image?q=tbn:ANd9GcRqMbXvdztEAKJMI7MtP0RuM6rYlOQ1TmLL8vBIGj_PLM0hgE_4ua7_Tw9rtFaBQSAEPXcZEyuYrniOmuA')
        botler.polling(none_stop=True, interval=0)

    finally:
            connection.close()
except:
    print("error")