from aiogram import Bot, Dispatcher
from decouple import config


TOKEN = config('TOKEN', default='None')

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)
ADMINS_ID = [2043671245]