import random
from config import ADMINS_ID
from aiogram import types, Dispatcher
from config import bot
import time


# @dp.message_handler()
async def echo(message: types.Message):
    username = f'@{message.from_user.username}' if message.from_user.username is not None else message.from_user.first_name

    bad_words = ['fuck', 'shit', 'holy shit', 'damn', 'hell', 'bitch']
    for i in bad_words:
        if i in message.text.lower():
                await message.reply(f'Не матерись {username}')
                time.sleep(5)
                await bot.delete_message(message.chat.id, message.message_id)
                break

    if message.text.startswith('.'):
        await bot.pin_chat_message(message.chat.id, message.message_id)

    if message.from_user.id in ADMINS_ID:
        if message.text.startswith('game'):
            dices = ['⚽','🏀','🎳','🎯','🎰', '🎲']
            dice = random.choice(dices)
            await bot.send_dice(message.chat.id, emoji=dice)

        # try:
        #     await bot.send_message(message.from_user.id, int(message.text)**2)
        # except:
        #     await bot.send_message(message.from_user.id, message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)