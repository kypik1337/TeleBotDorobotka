from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

a1 = KeyboardButton('/start')
button_client = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
button_client.add(a1)
a2 = KeyboardButton('/game')
button_client2 = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
button_client2.add(a2)