from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
)

start_button = KeyboardButton(f'/start')
mem_button = KeyboardButton(f'/mem')
share_location = KeyboardButton('Share locaton', request_location=True)
share_info = KeyboardButton('Share Info', request_contact=True)

start_markup.add(start_button, mem_button).add(share_location).add(share_info)