import logging

from aiogram import Dispatcher
from aiogram.types import Message

from parties.party_dict import PARTIES


async def show_quests(message: Message):
    await message.answer(
        text="Взгляните на доступные квесты:")
    for party in PARTIES:
        await message.answer(
            text=f"Посмотрите на этот квест:\n"
                 f"{party['name']}\n"
                 "URL: example.com")
        await message.answer_photo(photo=open(party.get('photo'), "rb"))


def register_show_quests(dp: Dispatcher):
    dp.register_message_handler(show_quests, commands=["quests"])
