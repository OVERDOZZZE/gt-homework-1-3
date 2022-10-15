from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import types, Dispatcher
from config import bot, dp
import random
from client_keyboards.client_kb import start_markup

# @dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f'Hello {message.from_user.first_name}, вот что может этот бот:\n'
                                                 f'1. /mem - забавные cats\n'
                                                 f'2. /quiz - небольшая викторина', reply_markup=start_markup)


# @dp.message_handler(commands=['quiz'])
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


# @dp.message_handler(commands=['mem'])
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



async def info(message: types.Message):
    await bot.send_message(message.from_user.id, f' Вот что может этот бот:\n'
                                                 f'1. /start для того, чтобы запустить бота\n'
                                                 f'2. /quiz для того, чтобы начать викторину\n'
                                                 f'3. /mem - бот отправляет картинки котов\n'
                                                 f'4. /ban - бот банит участника чье сообщение было переслано админом(только в группах)\n'
                                                 f'5. /unban - бот разбанит участника чье сообщение было переслано админом(только в группах)\n'
                                                 f'6. Если сообщение начинается с точки- бот его закрепляет\n'
                                                 f'7. Команда "dice" отправляет анимированную кость\n'
                                                 f'8. Кнопка "Share location" в клавиатуре отправляет геолокацию\n'
                                                 f'9. Кнопка "Share Info" в клавиатуре отправляет контактные данные\n'
                           )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(memes, commands=['mem'])
    dp.register_message_handler(info, commands=['info'])
