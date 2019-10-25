# https://github.com/eternnoir/pyTelegramBotAPI#more-examples

import telebot
from telebot import apihelper
from telebot import types

apihelper.proxy = {'http': 'https://149.28.154.147:3128', 'https': 'https://149.28.154.147:3128'}
token = '985278030:AAEnWCdRE9Bibz6n5wHEkuqtVkYJj33WNeU'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Получить задание')
    itembtn2 = types.KeyboardButton('Проверить задание')
    itembtn3 = types.KeyboardButton('Узнать свои баллы')
    itembtn4 = types.KeyboardButton('Справка')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.reply_to(message, "Выберите нужный пункт меню", reply_markup=markup)


@bot.message_handler(regexp="Получить задание")
def handle_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Выполнено! отправить отчет')
    itembtn2 = types.KeyboardButton('На главную')
    markup.add(itembtn1, itembtn2)
    bot.reply_to(message, "Вашe задание выложить пост!!!!")


@bot.message_handler(regexp="Проверить задание")
def handle_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Первое задание')
    itembtn2 = types.KeyboardButton('Второе задание ')
    itembtn3 = types.KeyboardButton('На главную')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.reply_to(message, "Выберите один из пунктов")

@bot.message_handler(regexp="Узнать свои балы")
def handle_message(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    itembtn1 = types.KeyboardButton('На главную')
    markup.add(itembtn1)
    bot.reply_to(message, "У вас 35 баллов вы занимаете 22 место из 50")

bot.polling(timeout=1000)
