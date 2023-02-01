from telebot import types

from bot import bot
from utils import get_data


@bot.message_handler(func=lambda m: m.text == "Определение из словаря Ефремовой")
def start_game(message: types.Message):
    baza = get_data()
    user = baza[str(message.from_user.id)]
    if not user["podskazka"]:
        bot.send_message(
            message.chat.id, 'Вам еще не загадали слово.'
        )
    else:
        bot.send_message(
            message.chat.id,
            f'<i>{user["podskazka"]}</i>'
        )