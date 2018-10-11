"""
Project "@DobbyMyBot".
"""
import random
import telebot
from telebot.types import Message
from telebot import apihelper

from my_data import MyTelegramData

TOKEN = MyTelegramData.get_token()
CHAT_ID = MyTelegramData.get_chat_id()
USER_ID = MyTelegramData.get_user_id()
JOKE = MyTelegramData.get_joke()
USERS = MyTelegramData.USERS

apihelper.proxy = MyTelegramData.PROXY

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['joke'])
def handle_joke(message: Message):
    bot.send_message(message.chat.id, text=JOKE)


@bot.message_handler(content_types=['text'])
def echo_yep(message: Message):
    if 'best' in message.text:
        bot.reply_to(message, 'Yep! The best!')
    elif message.from_user.id in USERS:
        bot.reply_to(message, f'{message.from_user.first_name}, please stop writing.')
    else:
        bot.reply_to(message, 'Wow! Fresh blood in our ranks')
        USERS.add(message.from_user.id)


bot.polling()
