from telebot import types

TG_TOKEN = '8051183669:AAEcFb0dUc6oxs4HBTe7tuqfzWlqJr2VkYA'

driver_button_ru = [
    'Поменять язык',
    'Аккаунт',
]
driver_button_uz = [
    'Til almashtrish',
    'Akkaunt',
]

passager_button_ru = [
    'Поменять язык',
    'Аккаунт',
    '🚖 Заказать такси',
    '📞 Поддержка'
]
passager_button_uz = [
    'Til almashtrish',
    'Akkaunt',
    '🚖 Taksi buyurtirish',
    '📞 Qo\'llab-quvvat'
]

rol_ru = [
    '🚖 Водитель',
    '🙋‍♂️ Пассажир'
]

rol_uz = [
    '🚖 Haydovchi',
    '🙋‍♂️ Yo\'lovchi'
]

def button(button_list):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    buttons = [types.KeyboardButton(text=text) for text in button_list]
    markup.add(*buttons)
    return markup
