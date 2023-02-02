from aiogram.dispatcher.filters.state import StatesGroup, State


# Only for tests
class Test(StatesGroup):
    q1 = State()
    q2 = State()


class QuestSelection(StatesGroup):
    age = State()
    party_type = State()
