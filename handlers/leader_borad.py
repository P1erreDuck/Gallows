from telebot import types

from bot import bot
from utils import get_data, update_data, slov_leader


@bot.message_handler(func=lambda m: m.text == "Счет / Таблица лидеров")
def leaderboard(message: types.Message):
    baza = get_data()
    main_user = baza[str(message.from_user.id)]
    slov_l = slov_leader(baza)
    pustishka = f'Ваши очки:{main_user["points"]}' \
                f'\nЛучшие игроки:\n'
    counter = 1
    for user_id, user_data in slov_l.items():
        points = user_data['points']
        full_name = user_data['name']
        pustishka += f"{counter}. <a href='tg://user?id={user_id}'>{full_name}</a> - {points}\n"
        counter += 1
    bot.send_message(message.chat.id, pustishka)






