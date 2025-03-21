import telebot
from telebot import types
from db_req import *
from config import TG_TOKEN, driver_menu_button_ru,driver_menu_button_uz,passager_menu_button_ru,passager_menu_button_uz, rol_ru, rol_uz, button

bot = telebot.TeleBot(TG_TOKEN)
global lan1

@bot.message_handler(commands=['start'])
def start (message):
    
    print('Начало бота')
    # Start 
    
    # find lan
    lan = find_lan(message.chat.id)
    
    # find user
    user = find_user(message.chat.id)
    print(user)
    
    #find role    
    role = find_role(message.chat.id)
    if lan == 'ru':
        if user is None:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Отправить номер телефога", request_contact=True)
            markup.add(item1)
            bot.send_message(message.chat.id, "Добро пожаловать!\nДля продолжение вам необходима поделиться контактом!", reply_markup=markup)   
        else:    
            if role is None:          
                markup = button(rol_ru)
                bot.send_message(message.chat.id, text='Выбирите вашу роль!', reply_markup=markup)    
            elif role == 'passager':    
                markup = button(passager_menu_button_ru)
                bot.send_message(message.chat.id, text='Ваша роль пассажир \nГлавное меню', reply_markup = markup)
            elif role == 'driver':     
                markup = button(driver_menu_button_ru)
                bot.send_message(message.chat.id, text='Главное меню', reply_markup = markup)
    elif lan == 'uz':
        if user is None:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Telefon raqamini yuborish", request_contact=True)
            markup.add(item1)
            bot.send_message(message.chat.id, "Xush kelibsiz!\nDavom etish ucun telefon raqamingizni jonating!", reply_markup=markup)
        else:
            if role is None:
                markup = button(rol_uz)
                bot.send_message(message.chat.id, text='Rolingizni tanlang!', reply_markup = markup)
            elif role == 'passager':
                markup = button(passager_menu_button_uz)
                bot.send_message(message.chat.id, text='Bosh menu', reply_markup = markup)
            elif role == 'driver':
                markup = button(driver_menu_button_uz)
                bot.send_message(message.chat.id, text='Bosh menu', reply_markup = markup)
    else:
        markup = types.InlineKeyboardMarkup()
        item1 = types.InlineKeyboardButton("Русский 🇷🇺", callback_data='ru')
        item2 = types.InlineKeyboardButton("O'zbek 🇺🇿", callback_data='uz')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, "Assalomu aleykum!\nВыберете язык!  🇷🇺\nTil tanlang!  🇺🇿", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'ru':
        bot.send_message(call.message.chat.id, "Вы выбрали русский язык")
        add_lan(call.message.chat.id, 'ru')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Отправить номер телефога", request_contact=True)
        markup.add(item1)
        bot.send_message(call.message.chat.id, "Добро пожаловать!\nДля продолжение вам необходима поделиться контактом!", reply_markup=markup)
    
    elif call.data == 'uz':
        bot.send_message(call.message.chat.id, "O'zbek tili tanlandi")
        add_lan(call.message.chat.id, 'uz')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Telefon raqamini yuborish", request_contact=True)
        markup.add(item1)
        bot.send_message(call.message.chat.id, "Xush kelibsiz!\nDavom etish ucun telefon raqamingizni jonating!", reply_markup=markup)
    else:
        bot.send_message(call.message.chat.id, "Error")

@bot.message_handler(content_types=['contact'])
def contact(message):
    lan = find_lan(message.chat.id)
    num = message.contact.phone_number
    number = '+998'+num[-9:]
    add_user(message.chat.id, number, message.from_user.first_name)
    
    if lan == 'ru':
        markup = button(rol_ru)
        bot.send_message(message.chat.id, "Вы водитель или пассажир?", reply_markup=markup)
        
    elif lan == 'uz':
        markup = button(rol_uz)
        bot.send_message(message.chat.id, "Haydovchi yoki yo'lovchimi?", reply_markup=markup)
    else:
        pass


@bot.message_handler(content_types=['text'])
def text(message):
    # find lan 
    lan = find_lan(message.chat.id)
    
    # driver
    if message.text == '🚖 Водитель' or message.text == '🚖 Haydovchi':
        
        if lan == 'ru':
            markup = button(driver_menu_button_ru)
            bot.send_message(message.chat.id, "Главное меню", reply_markup=markup)
            add_role(message.chat.id, 'driver')
        elif lan == 'uz':
            markup = button(driver_menu_button_uz)
            bot.send_message(message.chat.id, "Bosh munyu", reply_markup=markup)
            add_role(message.chat.id, 'driver')
       
    # passsager
    elif message.text == '🙋‍♂️ Пассажир' or message.text == '🙋‍♂️ Yo\'lovchi':
        
        if lan == 'ru':
            markup = button(passager_menu_button_ru)
            bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup)
            add_role(message.chat.id, 'passager')
        elif lan == 'uz':
            markup = button(passager_menu_button_uz)
            bot.send_message(message.chat.id, "Amalni tanlang", reply_markup=markup)
            add_role(message.chat.id, 'passager')
    else:
        if lan == 'ru':
            bot.send_message(message.chat.id, "Выберите один из вариантов")
        elif lan == 'uz':
            bot.send_message(message.chat.id, "Birorini tanlang")
       



if __name__ == '__main__':
    bot.polling(none_stop=True)