import telebot
import math
import webbrowser
import json
import os.path
config = {
    'name': 'BotinokForWorklast_bot',
    'token': '5407267874:AAFfMP8CgzCDRB0QYTgYnLCgD8cllKUzgj8'
}
botler = telebot.TeleBot(config['token'])

@botler.message_handler(commands=['calc','animals','count','happy','statistic'])

def get_text(message):
    # if message.text =="/happy":
    #     d = botler.send_message(message.chat.id, "Enter what you want")
    #     botler.register_next_step_handler(d, happy)
    # if message.text == "/statistic":
    #     d = botler.send_message(message.chat.id, "Enter what you want")
    #     botler.register_next_step_handler(d, statistic)
    if message.text =="Hello":
        botler.send_message(message.chat.id,"hello user!")
    # if message.text == "/calc":
    #     a=botler.send_message(message.chat.id, "Enter what you want")
    #     botler.register_next_step_handler(a,cal)
    if message.text == "/count":
        b=botler.send_message(message.chat.id, "Enter what you want")
        botler.register_next_step_handler(b,count)
    # if message.text == "/animals":
    #     c = botler.send_message(message.chat.id, "Enter what you want")
    #     botler.register_next_step_handler(c, animals)
# def statistic(message):
#     vowels=['a', 'e', 'i', 'o', 'u', 'y']
#     consonants=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
#     symbols=['!','?','.',',']
#     b = 0
#     path=os.path.join("Botl","bot.json")
#     for i in message.text.split(" "):
#         b += 1
#     file=open(path,"a")
#     json.dump("Words:"+str(b),file)
#     #botler.send_message(message.chat.id,"Words:"+str(b))
#     a=message.text.replace(" ","")
#     a=len(a)
#     file = open(path, "a")
#     json.dump("Symbols:" +str(a), file)
#     #botler.send_message(message.chat.id, "Symbols:" +str(a) )
#     vo=0
#     bo = message.text.lower()
#     for i in bo:
#         if i in vowels:
#             vo+=1
#     file = open(path, "a")
#     json.dump("vowels:" + str(vo), file)
#     #botler.send_message(message.chat.id, "vowels:" + str(vo))
#     co = 0
#     for i in bo:
#         if i in consonants:
#             co += 1
#     file = open(path, "a")
#     json.dump("consonants:" + str(co), file)
#     #botler.send_message(message.chat.id, "consonants:" + str(co))
#     mark = 0
#     for i in bo:
#         if i in symbols:
#             mark += 1
#     file = open(path, "a")
#     json.dump("punctuation marks:" + str(mark), file)
#     #botler.send_message(message.chat.id, "punctuation marks:" + str(mark))
#     d = 0
#     c = 0
#     list = []
#     for i in message.text:
#         if i.isdigit():
#             list.append(int(i))
#     for i in list:
#         if i % 2 == 0:
#             d += 1
#         else:
#             c += 1
#     file = open(path, "a")
#     json.dump("even:" + str(d), file)
#     file = open(path, "a")
#     json.dump("odd:" + str(c), file)
#     file = open(path, "r")
#     botler.send_document(message.chat.id,file)
#     #botler.send_message(message.chat.id, "even:" + str(d))
#     #botler.send_message(message.chat.id, "odd:" + str(c))
# def happy(message):
#     if len(message.text)==8:
#         b = int(message.text) // 10000
#         one = b // 1000
#         print(one)
#         two = (b // 100) % 10
#         print(two)
#         three = (b // 10) % 10
#         print(three)
#         four = b % 10
#         print(four)
#         c = int(message.text) % 10000
#         five = c // 1000
#         six = (c // 100) % 10
#         seven = (c // 10) % 10
#         eight = c % 10
#         if (one + two + three + four) == (five + six + seven + eight):
#             botler.send_message(message.chat.id, "Happy")
#         else:
#             botler.send_message(message.chat.id,"Unhappy")
#     if len(message.text)==6:
#         b = int(message.text) // 1000
#         one = b // 100
#         two = b % 11
#         three = b % 10
#         c = int(message.text) % 1000
#         four = c // 100
#         five = c % 11
#         six = c % 10
#         if (one + two + three) == (four + five + six):
#             botler.send_message(message.chat.id,"Happy")
#         else:
#             botler.send_message(message.chat.id,"Unhappy")
# def cal(message):
#         if "+" in message.text:
#             st=message.text
#             message.text = message.text.split("+")
#             message.text = list(map(int, message.text))
#             a=(sum(message.text))
#             botler.send_message(message.chat.id,st+"="+str(a))
#         if "*" in message.text:
#             st2 = message.text
#             message.text = message.text.split("*")
#             message.text = list(map(int, message.text))
#             a = (math.prod(message.text))
#             botler.send_message(message.chat.id,st2+"="+str(a))
#         if "-" in message.text:
#             st3 = message.text
#             message.text = message.text.split("-")
#             message.text = list(map(int, message.text))
#             a = message.text[0]-message.text[1]
#             botler.send_message(message.chat.id,st3+"="+str(a))
#         if "/" in message.text:
#             st4 = message.text
#             message.text = message.text.split("/")
#             message.text = list(map(int, message.text))
#             a = message.text[0] / message.text[1]
#             botler.send_message(message.chat.id,st4+"="+str(a))
def count(message):
    b = 0
    for i in message.text.split(" "):
        b += 1
    botler.send_message(message.chat.id, b)
# def animals(message):
#     if message.text == "Cat":
#         a = webbrowser.open('https://cdn.britannica.com/39/7139-050-A88818BB/Himalayan-chocolate-point.jpg')
#         botler.send_message(message.chat.id, str(a))
#     if message.text == "Dog":
#         # b=webbrowser.open('http://t0.gstatic.com/licensed-image?q=tbn:ANd9GcRqMbXvdztEAKJMI7MtP0RuM6rYlOQ1TmLL8vBIGj_PLM0hgE_4ua7_Tw9rtFaBQSAEPXcZEyuYrniOmuA')
#         botler.send_message(message.chat.id,'http://t0.gstatic.com/licensed-image?q=tbn:ANd9GcRqMbXvdztEAKJMI7MtP0RuM6rYlOQ1TmLL8vBIGj_PLM0hgE_4ua7_Tw9rtFaBQSAEPXcZEyuYrniOmuA')
botler.polling(none_stop=True, interval=0)