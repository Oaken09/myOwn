import telebot
from telebot import types
from tkn import my_token

token = my_token
bot = telebot.TeleBot(my_token)
keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
button1 = types.KeyboardButton('Как проходит курс?')
button2 = types.KeyboardButton('Мой курс')
button3 = types.KeyboardButton('Меню')
keyboard.add(button1, button2, button3)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Кнопка")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)