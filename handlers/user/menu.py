from aiogram.dispatcher.filters import Command, Text
from aiogram.types import  Message, ReplyKeyboardRemove
from loader import dp
from keyboards.default import menu

@dp.message_handler(Command("start"))
async def show_menu(message: Message):
    await message.answer("Qosh keldiniz", reply_markup=menu)
    await message.answer("Tandanyz", reply_markup=menu)

@dp.message_handler(Text(equals=["11 class", "9 class", "KTl,Bil","NIS"]))
async def get_food(message: Message):
    await message.answer(f"Tandaldy {message.text}.Rahmet", reply_markup=ReplyKeyboardRemove())