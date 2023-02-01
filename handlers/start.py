from telebot import types

from bot import bot
from utils import add_user, klava


@bot.message_handler(commands=['start'])
def start_command(message: types.Message):
    add_user(message.from_user.id)
    bot.send_message(message.chat.id, 'Загадать слово?', reply_markup=klava())
