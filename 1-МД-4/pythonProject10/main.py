import telebot
from telebot import types
bot = telebot.TeleBot('5105015774:AAFA4RqB305xwIj6Yqv3r59furm2sPIvQp4')
@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Главное меню")
    btn2 = types.KeyboardButton("❓ Помощь")
    markup.add(btn1, btn2)

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я тестовый бот для курса программирования на языке Питон".format(
                         message.from_user), reply_markup=markup)

