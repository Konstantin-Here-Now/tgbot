from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tgbot.misc.states import Test


async def enter_test(message: Message):
    await message.answer(
        text="Вы начали тестирование.\n"
             "Вопрос 1: вы человек?")
    await Test.q1.set()


async def test1(message: Message, state: FSMContext):
    answer = message.text
    async with state.proxy() as data:
        data['answer_age'] = answer
    await message.answer(
        text='Вы неправильно ответили на вопрос.\n'
             'Вы точно человек?'
    )
    await Test.q2.set()


async def test2(message: Message, state: FSMContext):
    data = await state.get_data()
    answer_age = data.get('answer_age')
    answer_party_type = message.text
    await message.answer(
        text='Спасибо за ваши ответы.'
    )
    await message.answer(f'Ответ 1: {answer_age}')
    await message.answer(f'Ответ 2: {answer_party_type}')
    await state.finish()


def register_testing(dp: Dispatcher):
    dp.register_message_handler(enter_test, commands=["test"])
    dp.register_message_handler(test1, state=Test.q1)
    dp.register_message_handler(test2, state=Test.q2)
