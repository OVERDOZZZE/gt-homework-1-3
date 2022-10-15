from config import bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types, Dispatcher


# @dp.callback_query_handler(lambda call: call.data == 'button_call_1')
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('Следующий вопрос', callback_data='button_call_2')
    markup.add(button_call_1)

    question = 'В какой части велосипеда использован винт с обратной резьбой?'
    answer = [
        'В сидении',
        'В руле',
        'В педалях',
        'В заднем переключателе'

    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation=f'Это был легкий вопрос для разминки',
        reply_markup=markup

    )


async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('Следующий вопрос', callback_data='button_call_3')
    markup.add(button_call_2)

    question = 'Сколько океанов на Земле?'
    answer = [
        '3',
        '4',
        '5',
        '6'
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='На земле всего 5 океанов: Атлантический, Индийский, Тихий, Южный и Северный Ледовитый.',
        reply_markup=markup
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == 'button_call_1')
    dp.register_callback_query_handler(quiz_3, lambda call: call.data == 'button_call_2')