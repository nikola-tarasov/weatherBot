from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import TOKEN_API, OPEN_WEATHER_TOKEN
import asyncio
import requests
import schedule
import time



bot = Bot(TOKEN_API)
dp = Dispatcher(bot)



kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='/help')
b2 = KeyboardButton(text='/vote')

kb.add(b1,b2)

@dp.message_handler(commands=['start'])
async def start_commands(message: types.Message):
        await message.answer(text='Привет! Я бот погоды! Напишите в сообщении город на латинице, чтобы получить прогноз на сегодя ')
        await message.delete()




@dp.message_handler()
async def get_WEATHER(message: types.Message):
                name = 'kursk'

                response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={name}&appid={OPEN_WEATHER_TOKEN}&units=metric")

                data = response.json()

                city = data['name']
                temp = data['main']['temp']
                humidity = data['main']['humidity']
                pressure = data['main']['pressure']
                wind = data['wind']['speed']
        
                await message.answer( text=f"Город: {city}\n Тумператур: {temp}\n Давление: {pressure}\n Влажность:{humidity}\n Скорость ветра: {wind} метров в секунду")


if __name__=='__main__':
        executor.start_polling(dp, skip_updates=True)
        



