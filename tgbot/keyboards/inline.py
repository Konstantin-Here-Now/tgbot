from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot.keyboards.callback_datas import ask_age_callback

question_age_keyboard = InlineKeyboardMarkup(row_width=2,
                                             inline_keyboard=[
                                                 [InlineKeyboardButton(text='5-7 лет',
                                                                       callback_data='5-7 лет'),
                                                  InlineKeyboardButton(text='7-9 лет',
                                                                       callback_data='7-9 лет')
                                                  ],
                                                 [
                                                     InlineKeyboardButton(text='10-14 лет',
                                                                          callback_data='10-14 лет'),
                                                     InlineKeyboardButton(text='14-17 лет',
                                                                          callback_data='14-17 лет')
                                                 ],
                                                 [
                                                     InlineKeyboardButton(text='18-25 лет',
                                                                          callback_data='18-25 лет'),
                                                     InlineKeyboardButton(text='25 и страше',
                                                                          callback_data='25 и страше')
                                                 ],
                                                 [
                                                     InlineKeyboardButton(text='Отмена',
                                                                          callback_data='cancel'),
                                                 ]
                                             ]
                                             )

question_party_keyboard = InlineKeyboardMarkup(row_width=2,
                                               inline_keyboard=[
                                                   [InlineKeyboardButton(text='День рождения',
                                                                         callback_data='День рождения'),
                                                    InlineKeyboardButton(text='Праздник для класса',
                                                                         callback_data='Праздник для класса')
                                                    ],
                                                   [
                                                       InlineKeyboardButton(text='Выпускной в детском саду',
                                                                            callback_data='Выпускной в детском саду'),
                                                       InlineKeyboardButton(text='Корпоратив',
                                                                            callback_data='Корпоратив')
                                                   ],
                                                   [
                                                       InlineKeyboardButton(text='Другое',
                                                                            callback_data='another'),
                                                   ],
                                                   [
                                                       InlineKeyboardButton(text='Отмена',
                                                                            callback_data='cancel'),
                                                   ]
                                               ]
                                               )
