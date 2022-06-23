import telebot

import re
import requests
import json

URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"


def load_exchange():
    return json.loads(requests.get(URL).text)


def get_exchange(ccy_key):
    for exc in load_exchange():
        if(ccy_key == exc('ccy')):
            return exc
    return False


bot = telebot.TeleBot('token')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row("Привет", "Пока")

keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row("USD", "EUR", "RUR", "BTC")


@bot.message_handler(commands=['start'])
def start_message(message):
    print(str(message.from_user.first_name) + " " + str(message.from_user.last_name))
    print(message)
    # bot.send_message(message.chat.id, 'Салем! Сыз маган start деп жаздыныз.', reply_markup=keyboard1)

#723596194

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет, друг')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, 'Пока, друг')
    elif message.text == 'Стикер жыберыныз':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMdX7vCseWjrbTk5d2YnJBOw7Ft-GAAAgEAA8A2TxMYLnMwqz8tUR4E')
    elif message.text == 'курс':
        bot.send_message(message.chat.id, 'Осылардын быреуын танданыз', reply_markup=keyboard2)
    # elif message.text == 'USD':
    #     bot.send_message(message.chat.id, str(get_exchange("USD")))


@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    print(message)

bot.polling()

