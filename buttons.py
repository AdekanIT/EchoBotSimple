from telebot import types


kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

button1 = types.KeyboardButton('Wikipedia')
button2 = types.KeyboardButton('Translate')


kb.add(button1, button2)