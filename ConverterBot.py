import telebot
from telebot import types
import requests

bot = telebot.TeleBot(telegram_token)
amount = 0

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.chat.username}! Введите сумму.')
    bot.register_next_step_handler(message, summa)
    
def summa(message):
    global amount
    
    try:
        amount = float(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат. Введите сумму')
        bot.register_next_step_handler(message, summa)
        return
    
    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton('USD/EUR', callback_data='USD/EUR')
        item2 = types.InlineKeyboardButton('EUR/USD', callback_data='EUR/USD')
        item3 = types.InlineKeyboardButton('USD/RUB', callback_data='USD/RUB')
        item4 = types.InlineKeyboardButton('RUB/USD', callback_data='RUB/USD')
        item5 = types.InlineKeyboardButton('EUR/RUB', callback_data='EUR/RUB')
        item6 = types.InlineKeyboardButton('RUB/EUR', callback_data='RUB/EUR')
        item7 = types.InlineKeyboardButton('Другое значение', callback_data='else')    
        markup.add(item1, item2, item3, item4, item5, item6, item7)
        bot.send_message(message.chat.id, 'Выберите пару валют', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Введите сумму больше нуля')
        bot.register_next_step_handler(message, summa)
        
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':
        values = call.data.split('/')
        url = f"https://api.apilayer.com/exchangerates_data/convert?apikey={api_convert_token}&to={values[0]}&from={values[1]}&amount={amount}"
        response = requests.get(url)
        data = response.json()
        res = data['result']
        bot.send_message(call.message.chat.id, f'Получается: {amount} {values[0]} = {round(res, 2)} {values[1]}.\nМожете заново ввести сумму.')
        bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, 'Введите пару валют через слеш.')
        bot.register_next_step_handler(call.message, myconvert)

def myconvert(message):
    try:
        values = message.text.upper().split('/')
        url = f"https://api.apilayer.com/exchangerates_data/convert?apikey={api_convert_token}&to={values[0]}&from={values[1]}&amount={amount}"
        response = requests.get(url)
        data = response.json()
        res = data['result']
        bot.send_message(message.chat.id, f'Получается: {amount} {values[0]} = {round(res, 2)} {values[1]}. Можете заново ввести сумму.')
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, 'Впишите валюты корректно через слеш.')
        bot.register_next_step_handler(message, myconvert) 
        
bot.polling(none_stop=True)
