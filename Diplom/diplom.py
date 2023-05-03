from fiveth_app.models import *
import telebot
from telebot import types
from datetime import time, timedelta, datetime,timezone

from django.core.exceptions import ValidationError
from decimal import Decimal, DecimalException

autoriz=False
choosewish=""
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboardauto = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton('Trash')
button2 = types.KeyboardButton('Products')
button3 = types.KeyboardButton('Role')
button4 = types.KeyboardButton('Wallet')
button5= types.KeyboardButton('Check wallet')
button6=types.KeyboardButton('Clear order')
button7=types.KeyboardButton('Category for washing')
button8=types.KeyboardButton('Check washing')
button10 = types.KeyboardButton('Register')
button11 = types.KeyboardButton('Auto')
keyboard.add(button1,button2,button3,button4,button5,button6,button7,button8)
keyboardauto.add(button10,button11)
config = {
    'name': 'cleanworld_bot',
    'token': '5831529099:AAFwiCf_7CyMSKnO6I_Ds3UmhIoO2SLomV0'
}
botler = telebot.TeleBot(config['token'])

@botler.message_handler(commands=['start'])
def start(message):
    if not autoriz:
        botler.send_message(message.chat.id, 'First you need to login:', reply_markup=keyboardauto)
    elif autoriz:
        botler.send_message(message.chat.id,'Menu:',reply_markup=keyboard)
    if not Wallet.objects.filter(userid = message.chat.id):
        Wallet.objects.get_or_create(
            userid = message.chat.id,
        )
    if not JustUser.objects.filter(userid = message.chat.id):
        JustUser.objects.get_or_create(
            userid = message.chat.id,
        )
    if not timewashing.objects.filter(userid = message.chat.id):
        JustUser.objects.get_or_create(
            userid = message.chat.id,
        )
@botler.message_handler(content_types=['text'])
def get_text(message):
    if message.text == "Auto":
        if not autoriz:
            c = botler.send_message(message.chat.id, "Enter login and pussword: ")
            botler.register_next_step_handler(c, auto)
        else:
            botler.send_message(message.chat.id, "You already authorized")
    elif message.text == "Register":
        if not autoriz:
            c = botler.send_message(message.chat.id, "Enter login and pussword: ")
            botler.register_next_step_handler(c, register)
        else:
            botler.send_message(message.chat.id, "You already authorized")
    elif autoriz:
        if message.text == "Role":

            keyboard3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            botler.send_message(message.chat.id, "Choose what you want")
            button13 = types.KeyboardButton("Change Role")
            button14 = types.KeyboardButton("Choose Role")
            button15 = types.KeyboardButton("Show Role")
            button16=types.KeyboardButton("About Roles")
            keyboard3.add(button13,button14,button15,button16)
            choice=botler.send_message(message.chat.id, "Please click a button", reply_markup=keyboard3)
            botler.register_next_step_handler(choice,choicee)
        if message.text=="Check washing":
            # filtered_washing = timewashing.objects.filter(userid=message.chat.id)
            # if filtered_washing.count() == 0:
            #     botler.send_message(message.chat.id, "Your washing list is empty")

            for i in timewashing.objects.filter(userid=message.chat.id):
                now = datetime.now()
                #now=now.replace(tzinfo=timezone.utc)
                i.endtime=i.endtime.replace(tzinfo=None)
                if now<i.endtime:
                    botler.send_message(message.chat.id, f'Your washing will end at {i.endtime}')
                else:
                    botler.send_message(message.chat.id, f'your wash is over, you can pick up or we can deliver to you')
                    keyboard2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
                    button = types.KeyboardButton("Deliver: 100")
                    button1 = types.KeyboardButton("Pick up: Free")
                    keyboard2.add(button,button1)
                    choice = botler.send_message(message.chat.id, "Choose an option", reply_markup=keyboard2)
                    botler.register_next_step_handler(choice, clothes)
        if message.text=="Category for washing":
            look = categoryforwashing.objects.filter()
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for i in look:
                button = types.KeyboardButton(f'{i.namecat}: {i.price}')
                keyboard.add(button)
            choice = botler.send_message(message.chat.id, "category", reply_markup=keyboard)
            botler.register_next_step_handler(choice, description1)
        if message.text == "Wallet":
            botler.send_message(message.chat.id, "Enter how much money do you want to add: ")
            botler.register_next_step_handler(message, add_money)
        if message.text=="Check wallet":
            botler.send_message(message.chat.id, Wallet.objects.filter(userid=message.chat.id)[0].balance)

        if message.text == "Products":
            academy = Catagory.objects.filter()
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
            for i in academy:
                button = types.KeyboardButton(f'{i.name}')
                keyboard.add(button)
            choice=botler.send_message(message.chat.id, "category", reply_markup=keyboard)
            botler.register_next_step_handler(choice,products)
        if message.text == "Clear order":
            for i in Order.objects.filter(
                    userid=message.chat.id):
                i.delete()
            botler.send_message(message.chat.id, "Complete!")

        if message.text == "Trash":

            user_cart = [str(i.productid)
            for i in Order.objects.filter(userid=message.chat.id)]

            if user_cart:
                product_cost = dict()
                for i in Products.objects.all():
                    product_cost[i.name] = i.price

                user_cart_result = dict()
                for i in user_cart:
                    if i not in user_cart_result:
                        user_cart_result[i] = user_cart.count(i)

                user_cart_cost = 0

                for res in user_cart_result:
                    user_cart_cost += product_cost[res] * user_cart_result[res]
                today = date.today()
                academy = Order.objects.filter(date__year=today.year,date__month=today.month,date__day=today.day)
                curators = ""
                for i in academy:
                    curators = curators + f'{i.date} - {i.userid} - {i.productid}\n'

                botler.send_message(message.chat.id,curators + f'\nOrder cost - {user_cart_cost}')
                keyboard3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
                botler.send_message(message.chat.id,"Do you want buy?")
                button13 = types.KeyboardButton("Yes")
                button14 = types.KeyboardButton("No")
                keyboard3.add(button13,button14)
                choice=botler.send_message(message.chat.id, "Please click a button", reply_markup=keyboard3)
                botler.register_next_step_handler(choice,buy)
            else:
                botler.send_message(message.chat.id, "Order empty! ")


def register(message):
    list = message.text.split(" ")
    a = AutoRegister.objects.get_or_create(
        userid=message.chat.id,
        login=list[0],
        password=list[1]
    )
    botler.send_message(message.chat.id, "Good")
def auto(message):
    list = message.text.split(" ")
    try:
        user = AutoRegister.objects.get(login=list[0], password=list[1])
        if user.authorized:
            botler.send_message(message.chat.id, "Login success", reply_markup=keyboard)
        else:
            user.authorized = True
            user.save()
            botler.send_message(message.chat.id, "Login success\n", reply_markup=keyboard)
    except AutoRegister.DoesNotExist:
        botler.send_message(message.chat.id, "Fault\nTry again", reply_markup=keyboardauto)
    except Exception as e:
        print(f"Error during authorization: {e}")
        botler.send_message(message.chat.id, "Login or password is failed. Please try again.")
def description1(message):
    list=message.text.split(":")
    a=list[1]
    a=str(a)
    global choosewish
    choosewish=list[0]
    look = description.objects.filter()
    for i in look:
        if str(i.nameid) == str(list[0]):
            botler.send_message(message.chat.id, i.description)

    keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    botler.send_message(message.chat.id, "Do you want continue?")

    button13 = types.KeyboardButton("Yes")
    button14 = types.KeyboardButton("No")
    keyboard1.add(button13, button14)
    choice = botler.send_message(message.chat.id, "Please click a button", reply_markup=keyboard1)
    botler.register_next_step_handler(choice, priceforwish)

def priceforwish(message):
    if message.text=="No":
        botler.send_message(message.chat.id,'Fine',reply_markup = keyboard)

    if message.text=="Yes":
        if JustUser.objects.filter(userid=message.chat.id, companyORuser__isnull=True).exists():
            keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
            botler.send_message(message.chat.id, "Choose your role")
            button13 = types.KeyboardButton("Company")
            button14 = types.KeyboardButton("User")
            keyboard1.add(button13, button14)
            choice = botler.send_message(message.chat.id, "Please click a button", reply_markup=keyboard1)
            botler.register_next_step_handler(choice, choicee2)
        else:
            user = JustUser.objects.get(userid=message.chat.id)
            if user.companyORuser == 'User':
                limit = 7
            elif user.companyORuser == 'Company':
                limit = 15
            num_records = timewashing.objects.count()
            if num_records >= limit:
                botler.send_message(message.chat.id, 'All slots are taken. Please try again later.',reply_markup = keyboard)
            else:
                botler.send_message(message.chat.id, "OK")
                keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
                botler.send_message(message.chat.id, "Please choose the right weight for your clothes")
                button13 = types.KeyboardButton("0-1 kg")
                button14 = types.KeyboardButton("1-3 kg")
                button15 = types.KeyboardButton("3-6 kg")
                button16 = types.KeyboardButton("6+ kg")
                keyboard1.add(button13, button14,button15,button16)
                choice = botler.send_message(message.chat.id, "Please click a button", reply_markup=keyboard1)
                botler.register_next_step_handler(choice, ty)
def clothes(message):
    if message.text=="Deliver: 100":
        user = Wallet.objects.filter(
            userid=message.chat.id)[0]
        if user.balance < 100:
            botler.send_message(message.chat.id, "Not Enough money!", reply_markup=keyboard)
        else:
            now = datetime.now()
            user.balance -= 100
            user.save()
            for i in timewashing.objects.filter(
                    userid=message.chat.id, endtime__lt=now):
                i.delete()
            botler.send_message(message.chat.id, "Complete!, expect delivery", reply_markup=keyboard)
    if message.text=="Pick up: Free":
        now = datetime.now()
        for i in timewashing.objects.filter(
                userid=message.chat.id,endtime__lt=now):
            i.delete()
        botler.send_message(message.chat.id, "Complete! OK, we are waiting for you", reply_markup=keyboard)
def ty(message):
     from datetime import  timedelta, datetime
     if message.text=="0-1 kg":

         user = Wallet.objects.filter(
             userid=message.chat.id)[0]
         a=categoryforwashing.objects.filter(namecat=choosewish)
         for i in a:
             if user.balance< i.price*1:
                 botler.send_message(message.chat.id, "Not Enough money!", reply_markup=keyboard)
             else:
                 from datetime import datetime, timedelta

                 now = datetime.now()
                 timer = now + timedelta(minutes=45)
                 timewashing.objects.get_or_create(
                     userid=message.chat.id,
                     endtime=timer

                 )
                 user.balance -= i.price*1
                 user.save()
                 botler.send_message(message.chat.id, f'Ok,washing will end after 30 minutes and 15 minutes of drying, at {timer.strftime("%Y-%m-%d %H:%M:%S")}', reply_markup=keyboard)

     if message.text == "1-3 kg":
        user = Wallet.objects.filter(
            userid=message.chat.id)[0]
        a = categoryforwashing.objects.filter(namecat=choosewish)
        for i in a:
            if user.balance < i.price * 2:
                botler.send_message(message.chat.id, "Not Enough money!", reply_markup=keyboard)
            else:
                now = datetime.now()
                future = now + timedelta(hours=2)
                timewashing.objects.get_or_create(
                    userid=message.chat.id,
                    endtime=future
                )
                user.balance -= i.price * 2
                user.save()
                botler.send_message(message.chat.id, f'Ok,washing will end after 1 hour 30 minutes and 30 minutes of drying, at {future.strftime("%Y-%m-%d %H:%M:%S")}',
                                    reply_markup=keyboard)
     if message.text == "3-6 kg":
        user = Wallet.objects.filter(
            userid=message.chat.id)[0]
        a = categoryforwashing.objects.filter(namecat=choosewish)
        for i in a:
            if user.balance < i.price * 3:
                botler.send_message(message.chat.id, "Not Enough money!", reply_markup=keyboard)
            else:
                now = datetime.now()
                future = now + timedelta(hours=3,minutes=45)
                timewashing.objects.get_or_create(
                    userid=message.chat.id,
                    endtime=future
                )
                user.balance -= i.price * 3
                user.save()
                botler.send_message(message.chat.id,
                                    f'Ok,washing will end after 3 hours  and 45 minutes of drying, at {future.strftime("%Y-%m-%d %H:%M:%S")}',
                                    reply_markup=keyboard)
     if message.text == "6+ kg":
        user = Wallet.objects.filter(
            userid=message.chat.id)[0]
        a = categoryforwashing.objects.filter(namecat=choosewish)
        for i in a:
            if user.balance < i.price * 4:
                botler.send_message(message.chat.id, "Not Enough money!", reply_markup=keyboard)
            else:
                now = datetime.now()
                future = now + timedelta(hours=6)
                timewashing.objects.get_or_create(
                    userid=message.chat.id,
                    endtime=future
                )
                user.balance -= i.price * 4
                user.save()
                botler.send_message(message.chat.id,
                                    f'Ok,washing will end after 5 hours and 1 hour of drying, at {future.strftime("%Y-%m-%d %H:%M:%S")} ',
                                    reply_markup=keyboard)

def choicee(message):
    if message.text=="About Roles":
        botler.send_message(message.chat.id,"User is a role for regular  users who want to wash their clothes,and 7 washing machines are ready for users. \n\nCompany is a role for an enterprise where laundry is needed for a considerable number of people,and 15 washing machines are ready for company.",reply_markup=keyboard)
    if message.text=="Choose Role":
        for i in JustUser.objects.filter(userid=message.chat.id):
            if i.companyORuser == None:
                keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
                botler.send_message(message.chat.id, "Choose your role")
                button13 = types.KeyboardButton("Company")
                button14 = types.KeyboardButton("User")
                keyboard1.add(button13, button14)
                choice = botler.send_message(message.chat.id, "Please click a button", reply_markup=keyboard1)
                botler.register_next_step_handler(choice, choicee2)
            elif i.companyORuser=="User" or "Company":
                 botler.send_message(message.chat.id, "Sry but you're already have a role", reply_markup=keyboard)

    if message.text == "Change Role":

        keyboard1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        botler.send_message(message.chat.id, "choose the role you want")
        button13 = types.KeyboardButton("Company")
        button14 = types.KeyboardButton("User")
        keyboard1.add(button13, button14)
        choice = botler.send_message(message.chat.id, "Please click a button", reply_markup=keyboard1)
        botler.register_next_step_handler(choice, change)
    if message.text == "Show Role":
        for i in JustUser.objects.filter(userid=message.chat.id):
            botler.send_message(message.chat.id, f"Your role: {i.companyORuser}", reply_markup=keyboard)
def change(message):
    for i in JustUser.objects.filter(
            userid = message.chat.id):
        i.delete()
    JustUser.objects.get_or_create(
        userid=message.chat.id,
        companyORuser=message.text
    )
    botler.send_message(message.chat.id, f"Great now you: {message.text}", reply_markup=keyboard)
def choicee2(message):
    for i in JustUser.objects.filter(
            userid = message.chat.id):
        i.delete()
    JustUser.objects.get_or_create(
        userid=message.chat.id,
        companyORuser=message.text
    )
    botler.send_message(message.chat.id, f"Great now you: {message.text}", reply_markup=keyboard)

def buy(message):
    if message.text=="Yes":
        user_cart = [str(i.productid)
                     for i in Order.objects.filter(userid=message.chat.id)]

        if user_cart:
            product_cost = dict()
            for i in Products.objects.all():
                product_cost[i.name] = i.price

            user_cart_result = dict()
            for i in user_cart:
                if i not in user_cart_result:
                    user_cart_result[i] = user_cart.count(i)

            user_cart_cost = 0

            for res in user_cart_result:
                user_cart_cost += product_cost[res] * user_cart_result[res]
            user = Wallet.objects.filter(
                userid=message.chat.id)[0]
            if user.balance < user_cart_cost:
                botler.send_message(message.chat.id, "Not Enough money!",reply_markup=keyboard)
            else:
                user.balance -= user_cart_cost
                user.save()
                clearusercart(message)
    if message.text == "No":
                botler.send_message(message.chat.id, "OK", reply_markup=keyboard)


def clearusercart(message):
    for i in Order.objects.filter(
            userid = message.chat.id):
        i.delete()
    botler.send_message(message.chat.id, "Complete!",reply_markup=keyboard)

def add_money(message):
    try:
        user = Wallet.objects.filter(
            userid=message.chat.id)[0]
        user.balance += Decimal(message.text)
        user.save()
    except DecimalException:
        botler.send_message(message.chat.id, 'Non Digit!')
    else:
        botler.send_message(message.chat.id, "Summ added to wallet!")

def products(message):
    academy = Products.objects.filter(catagoryid__name=message.text)
    curators = ""
    a=Wallet.objects.filter(userid=message.chat.id)
    for i in a:
        user=i.balance
    keyboard= types.InlineKeyboardMarkup()
    for i in academy:
        button=types.InlineKeyboardButton(f'{i.name}: {i.price}$',callback_data=i.name)
        keyboard.add(button)
    botler.send_message(message.chat.id, f"your wallet: {str(user)}$",reply_markup=keyboard)

@botler.callback_query_handler(func=lambda call: True)
def callback_data(call):
    if call.data:
        a=Order.objects.get_or_create(
            userid=call.message.chat.id,
            productid=Products.objects.get(name=call.data),
            date=datetime.now()
        )
        botler.send_message(call.message.chat.id,f'Product: {call.data} add to trash',reply_markup=keyboard)
botler.polling(none_stop=True,interval=0)