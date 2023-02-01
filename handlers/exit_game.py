from telebot import types

from bot import bot
from utils import get_data, update_data, sbros


@bot.message_handler(func=lambda m: m.text == "Выход")
def exit_game(message: types.Message):
    baza = get_data()
    user = baza[str(message.from_user.id)]
    sbros(user, baza)
    update_data(baza)
    bot.send_message(
        message.chat.id,
        'До встречи!'
    )