from config import ADMINS_ID, bot
from aiogram import types, Dispatcher


async def ban(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMINS_ID:
            await message.answer('Вы не являетесь администратором')
        elif not message.reply_to_message:
            await message.answer('Некорректный формат')
        else:
            await bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            await message.answer(f'{message.from_user.first_name} забанил пользователя {message.reply_to_message.from_user.first_name}')

    else:
        await message.answer('Пиши в группе!')


async def unban(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMINS_ID:
            await message.answer('Вы не являетесь администратором')
        elif not message.reply_to_message:
            await message.answer('Некорректный формат')
        else:
            await bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            await message.answer(f'{message.from_user.first_name} разбанил пользователя {message.reply_to_message.from_user.first_name}')


async def pin(message: types.Message):
    if message.from_user.id in ADMINS_ID:
        if message.reply_to_message:
            await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'])
    dp.register_message_handler(unban, commands=['unban'])
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')
