from aiogram import Dispatcher, Bot, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from markups import help_markup
from admin import register_hendlers_admin
storage = MemoryStorage
from main import *  

@dp.message_handler(commands=["start"])
async def welcome_message(message: types.Message):
    username = message.from_user.username
    text = f"Hello, {username}. Send /help to see what I can do."
    await message.reply(text=text)


@dp.message_handler(commands=["help"])
async def help_message(message: types.Message):
    markup = help_markup()
    await message.reply(text="Выберите вариант", reply_markup=markup)






if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)