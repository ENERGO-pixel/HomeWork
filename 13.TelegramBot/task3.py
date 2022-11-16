import telebot
import pymysql
from telebot import types
autoriz=False
def menu(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('/add')
    button2 = types.KeyboardButton('/show')
    button3 = types.KeyboardButton('/filter')
    button4 = types.KeyboardButton('/register')
    button5 = types.KeyboardButton('/auto')
    keyboard.add(button1,button2,button3,button4,button5)
    botler.send_message(message.chat.id,'Menu:',reply_markup=keyboard)
try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="IDSharapo_ff220601",
        database="market",
        cursorclass=pymysql.cursors.DictCursor )
    print("Okay")
    try:
        config = {
                    'name': 'BotlerFromBot_bot',
                    'token': '5704144687:AAEZrWiXaWXkXHO9GlQ3b52Zb5f0bg2d2Sg'
                }
        botler = telebot.TeleBot(config['token'])
        @botler.message_handler(commands=['start'])
        def start(message):
            menu(message)
        @botler.message_handler(content_types=['text'])
        def get_text(message):
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
                if message.text == "/add":
                    b = botler.send_message(message.chat.id, "Enter what you want")
                    botler.register_next_step_handler(b, add)
                if message.text == "/filter":
                    b = botler.send_message(message.chat.id, "Enter what you want")
                    botler.register_next_step_handler(b, filter)
                if message.text == "/show":
                    with connection.cursor() as cursor:
                        list = []
                        list1=""
                        select_all = f"select * from Market.Market"
                        cursor.execute(select_all)
                        result = cursor.fetchall()
                        print(result)
                        for row in result:
                            list1+=str(row)
                        cursor.execute(
                            f"SELECT * from `Market`")
                        result = cursor.fetchall()
                        botler.send_message(message.chat.id,"\n".join(
                            [
                                f"Id: {row.get('id')}, Name: {row.get('name')}, count: {row.get('countt')}, money: {row.get('money')}$ "
                                for row in result]))
            else:
                botler.send_message(message.chat.id, "You are not login")
                botler.send_message(message.chat.id, "/auto")
                botler.send_message(message.chat.id, "/register")
        def register(message):
            list = message.text.split(" ")
            with connection.cursor() as cursor:
                select_all = f"select * from Market.userauto where name='{list[0]}' and password ='{list[1]}'"
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
                select_all = f"select * from Market.userauto where name='{list[0]}' and password ='{list[1]}'"
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
        def add(message):
            list = message.text.split(" ")
            list1=[]
            for i in list:
                if i.isdigit():
                    list1.append(int(i))
            with connection.cursor() as cursor:
                insert = f"INSERT INTO `Market` (name,countt,money) VALUES ('{list[0]}',{list1[0]},{list1[1]})"
                cursor.execute(insert)
                connection.commit()
        def filter(message):
            with connection.cursor() as cursor:
                cursor.execute(
                    f"select {message.text} from Market.Market")
                result = cursor.fetchall()
                if message.text=="name":
                    botler.send_message(message.chat.id, "\n".join(
                        [
                            f"Name: {row.get('name')} "
                            for row in result]))
                if message.text=="countt":
                    botler.send_message(message.chat.id, "\n".join(
                        [
                            f"Count: {row.get('countt')} "
                            for row in result]))
                if message.text=="money":
                    botler.send_message(message.chat.id, "\n".join(
                        [
                            f"Money: {row.get('money')}$ "
                            for row in result]))
        botler.polling(none_stop=True, interval=0)
    finally:
            connection.close()
except Exception as error:
    print(error)