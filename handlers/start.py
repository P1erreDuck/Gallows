from telebot import types

from bot import bot
from utils import add_user, klava, get_data, update_user


@bot.message_handler(commands=['start'])
def start_command(message: types.Message):
    baZa = get_data()
    if str(message.from_user.id) not in baZa:
        add_user(message, baZa)
    else:
        update_user(message, baZa)

    bot.send_message(message.chat.id, 'Загадать слово?', reply_markup=klava())
