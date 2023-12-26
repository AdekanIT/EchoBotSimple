import telebot
from telebot.types import ReplyKeyboardRemove
from buttons import kb

bot = telebot.TeleBot('6829892916:AAG2suH6RDFW2VO5xisuVWRQG9oaR6PE_l0')


# Обработка команды старт
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    # print(message.from_user)  # Чтоб узнать инфу про пользователя
    bot.send_message(user_id, 'Hello! Welcome to telegram bot!', reply_markup=kb)


# Обработка текстовых сообщений
@bot.message_handler(content_types=['text'])
def text_message(message):
    user_id = message.from_user.id
    if message.text.title() == 'Wikipedia':
        bot.send_message(user_id, 'Enter word:', reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(message, wiki)
    elif message.text.title() == 'Translate':
        bot.send_message(user_id, 'Enter the word for translate: ', reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(message, translate)
    else:
        bot.send_message(user_id, 'WTF?!')


def wiki(message):
    user_id = message.from_user.id
    if message.text.title() == 'Cat':
        bot.send_message(user_id, 'Cat (Felis catus), also called house cat or domestic cat, is a member of the family Felidae in the order Carnivora. It is also the smallest member of that family, which includes lions, tigers, and pumas.', reply_markup=ReplyKeyboardRemove())


def translate(message):
    user_id = message.from_user.id
    if message.text.title() == 'Cat':
        bot.send_message(user_id, 'Кот', reply_markup=ReplyKeyboardRemove())


# Запуск бота
bot.polling(none_stop=True)