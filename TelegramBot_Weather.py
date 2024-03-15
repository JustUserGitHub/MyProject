import telebot
from telebot import types
import random
import requests
from datetime import datetime

bot = telebot.TeleBot(telegram_token) #токен бота

@bot.message_handler(commands=['start'])
def start(message):
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Weather')
    item2 = types.KeyboardButton('RandomNumber')        
    markup.add(item1, item2)
    bot.send_message(message.chat.id, f'Привет, {message.chat.username}!\nВыбери что-нибудь.', reply_markup=markup)
    
def weather_info(message):
    inf = 'https://api.openweathermap.org/data/2.5/weather?q='+message.text+'&units=metric&lang=ru&appid='+api_token # токен сайта OpenWeather
    url = requests.get(inf) 
    pogoda = url.json()
    
    if url.status_code == 200:    
        town = f"Погода в городе: {message.text.capitalize()}"
        temp = f"Температура состовляет: {round(pogoda['main']['temp'])}°C"
        feels_likes = f"Ощущается как: {round(pogoda['main']['feels_like'])}°C"
        pressure = f"Давление: {pogoda['main']['pressure']} мм.рт.ст."
        humidity = f"Влажность: {pogoda['main']['humidity']}%"
        wind = f"Ветер: {pogoda['wind']['speed']} м/с"
        sunrise = f"Восход: {datetime.fromtimestamp(int(pogoda['sys']['sunrise'])).strftime('%d.%m.%Y %H:%M')}"
        sunset = f"Закат: {datetime.fromtimestamp(int(pogoda['sys']['sunset'])).strftime('%d.%m.%Y %H:%M')}"
        bot.send_message(message.chat.id, f'{town}\n{temp}\n{feels_likes}\n{wind}\n{pressure}\n{humidity}\n{sunrise}\n{sunset}')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Weather')
        markup.add(item1)
    
    elif url.status_code == 404:
        bot.send_message(message.chat.id, f'Введи корректное название города.')
        bot.register_next_step_handler(message, weather_info)

@bot.message_handler(content_types=['text'])
def info(message):
    
    if message.text == "Weather":
        bot.send_message(message.chat.id, 'В каком городе хочешь узнать погоду?')   
        bot.register_next_step_handler(message, weather_info)
    
    elif message.text == "RandomNumber":
        bot.send_message(message.chat.id, f'Твоё случайное число: {random.randint(0, 1000)}')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('RandomNumber')
        markup.add(item1)
    
bot.infinity_polling()
