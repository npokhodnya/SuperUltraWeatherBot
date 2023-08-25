from aiogram import types


def get_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Share Position", request_location=True)
    keyboard.add(button)
    return keyboard
