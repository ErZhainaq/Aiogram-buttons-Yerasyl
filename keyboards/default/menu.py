from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="11 class"),
            KeyboardButton(text="9 class"),
        ],
        [
            KeyboardButton(text="KTL,BIL"),
            KeyboardButton(text="NIS")
        ],
    ],
    resize_keyboard=True
)