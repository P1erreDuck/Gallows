from telebot import types

from bot import bot
from utils import get_data, is_pizdaty_vvod, show, update_data, klava, sbros


@bot.message_handler(content_types=["text"])
def gameplay(message: types.Message):
    baza = get_data()
    user = baza[str(message.from_user.id)]
    vvod = message.text.lower()
    if not user["slovo"]:
        bot.send_message(message.chat.id, 'Вы не начали игру. Чтобы начать нажмите Загадать слово.')
    else:
        pizdaty_vvod = is_pizdaty_vvod(vvod)
        if not pizdaty_vvod:
            bot.send_message(message.chat.id, 'Нужно ввести ОДНУ РУССКУЮ букву!')
        else:
            if vvod in user["neotgad"]:
                user["otgad"].append(vvod)
                user["neotgad"].remove(vvod)
                bot.send_message(
                    message.chat.id, f'Буква "{vvod}" открыта!\n {show(user["slovo"], user["otgad"])}')
                update_data(baza)
                if len(user["neotgad"]) == 0:
                    bot.send_message(
                        message.chat.id,
                        f'Поздравляю! Ты угадал слово <b>{user["slovo"]}</b>!'
                        f'\n Чтобы начать новую игру нажми Загадать слово',
                        reply_markup=klava()
                    )
                    sbros(user, baza)
                    update_data(baza)

            elif vvod in user['otgad']:
                bot.send_message(message.chat.id, f'Ты уже проверял букву "{vvod}"!\n {show(user["slovo"], user["otgad"])}')
            else:
                user["hp"] = user["hp"] - 1
                user["otgad"].append(vvod)
                update_data(baza)
                bot.send_message(
                    message.chat.id, f'Буквы "{vvod}" нет в этом слове! Осталось попыток:{user["hp"]}')
                if user["hp"] == 0:
                    bot.send_message(
                        message.chat.id,
                        f'Поражение! Это было слово <b>{user["slovo"]}</b>. '
                        f'\n Чтобы начать новую игру нажми Загадать слово',
                        reply_markup=klava()
                    )
                    sbros(user, baza)