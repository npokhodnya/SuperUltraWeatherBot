import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from keyboard_tools import get_keyboard
from weather_forecast_tools import *

# Working with .env file and env variables
load_dotenv("env/config.env")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)


@dp.message_handler(content_types=['location'])
async def handle_location(message: types.Message):
    lat = message.location.latitude
    lon = message.location.longitude
    text = get_weather(lat, lon)
    await message.answer(text)


@dp.message_handler(commands=['start'])
async def cmd_help(message: types.Message):
    text = f"Hello, <b>{message.from_user.full_name}</b>! \nClick on the button below to share your location!"
    await message.answer(text, reply_markup=get_keyboard())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
