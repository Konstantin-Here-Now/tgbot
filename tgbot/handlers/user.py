from aiogram import Dispatcher
from aiogram.types import Message


async def user_start(message: Message):
    await message.reply(
        text="Я помогу вам подобрать квест для вашего праздника. Для этого мне нужно задать вам несколько вопросов."
             "Введите команду /select")


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
