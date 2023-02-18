import logging

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery

from parties.party_dict import PARTY_DICT
from tgbot.keyboards.inline import question_age_keyboard, question_party_keyboard
from tgbot.misc.states import QuestSelection


async def user_info(message: Message):
    return message.chat.username


async def write_answer(callback: CallbackQuery, state: FSMContext, state_step: str):
    """
    Writes down answer from CallbackQuery into a particular state_step in state
    """
    answer = callback.data
    async with state.proxy() as data:
        data[state_step] = answer


async def select_party_ask_age(message: Message):
    logging.info(f'User {await user_info(message)} started quest selection.')
    await message.answer(
        text="Я помогу вам подобрать квест для вашего праздника. Для этого мне нужно задать вам несколько вопросов.\n"
             "Какой возраст участников?",
        reply_markup=question_age_keyboard)
    await QuestSelection.age.set()


async def ask_party_type(call: CallbackQuery, state: FSMContext):
    await write_answer(callback=call, state=state, state_step='age')
    await call.message.edit_reply_markup()  # Deletes keyboard
    logging.info(f'User {await user_info(call.message)} has chosen {call.data}.')
    await call.answer(f"Вы выбрали {call.data}!")
    await call.message.answer(
        text="По какому поводу планируется праздник?",
        reply_markup=question_party_keyboard)
    await QuestSelection.party_type.set()


async def show_parties(call: CallbackQuery, state: FSMContext):
    await write_answer(callback=call, state=state, state_step='party_type')
    await call.message.edit_reply_markup()  # Deletes keyboard
    logging.info(f'User {await user_info(call.message)} has chosen {call.data}.')
    await call.answer(f"Вы выбрали {call.data}!")
    state_data = await state.get_data()
    age = state_data.get('age')
    party_type = state_data.get('party_type')
    party = PARTY_DICT.get((age, party_type))
    await call.message.answer(
        text=f"Посмотрите на этот квест:\n"
             f"{party['name']}\n"
             "URL: example.com")
    await call.message.answer_photo(photo=open(party.get('photo'), "rb"))
    await state.finish()
    await call.message.answer('Чтобы забронировать квест и узнать более подробную информацию о деталях организации '
                              'праздника, напишите нам в личные сообщения @kvestpskov и мы ответим вам в ближайшее '
                              'время.')


async def cancel(call: CallbackQuery, state: FSMContext):
    logging.info(f'User {await user_info(call.message)} cancelled quest selection.')
    await call.answer('Вы отменили подбор квеста.', show_alert=True)
    await state.finish()
    await call.message.edit_reply_markup()


async def another(call: CallbackQuery, state: FSMContext):
    # Ввод пользователя с клавиатуры
    pass


def register_quest_selection(dp: Dispatcher):
    dp.register_message_handler(select_party_ask_age, commands=["select"])
    dp.register_callback_query_handler(cancel, text='cancel', state="*")
    dp.register_callback_query_handler(another, text='another', state="*")
    dp.register_callback_query_handler(ask_party_type, state=QuestSelection.age)
    dp.register_callback_query_handler(show_parties, state=QuestSelection.party_type)
