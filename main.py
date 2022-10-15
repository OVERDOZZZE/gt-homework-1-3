import random
from aiogram import types
from aiogram.utils import executor
from config import bot, dp
import logging
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f'Hello {message.from_user.first_name}, вот что может этот бот:\n'
                                                 f'1. /mem - забавные cats\n'
                                                 f'2. /quiz - небольшая викторина')


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('Следующий вопрос', callback_data='button_call_1')
    markup.add(button_call_1)

    question = 'Сколько изотопов водорода существует в природе на Земле?'
    answer = [
        '1',
        '2',
        '3',
        '4'
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation='На Земле есть три изотопа водорода: Наиболее распространенным является Протий (1Н),'
                    'Дейтерий (2Н) и Тритий (3Н)',
        reply_markup=markup

    )


@dp.callback_query_handler(lambda call: call.data == 'button_call_1')
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


@dp.message_handler(commands=['mem'])
async def memes(message: types.Message):
    await bot.send_message(message.from_user.id, f'Waggish cats')

    i1 = open('media/img.png', 'rb')
    i2 = open('media/img_1.png', 'rb')
    i3 = open('media/img_2.png', 'rb')
    i4 = open('media/img_3.png', 'rb')
    i5 = open('media/img_4.png', 'rb')
    i6 = open('media/img_5.png', 'rb')
    i7 = open('media/anonymous.jpg', 'rb')
    lst = [i1, i2, i3, i4, i5, i6, i7]

    photo1 = random.choice(lst)
    await bot.send_photo(message.from_user.id, photo=photo1)


@dp.message_handler()
async def echo(message: types.Message):
        try:
            await bot.send_message(message.from_user.id, int(message.text)**2)
        except:
            await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

