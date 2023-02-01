from telebot import types

from bot import bot
from utils import get_data, zagad_slov, update_data


@bot.message_handler(func=lambda m: m.text == "Загадать слово")
def word_generation(message: types.Message):
    baza = get_data()
    user = baza[str(message.from_user.id)]
    slovo, neotgad, podskazka = zagad_slov()
    user["slovo"] = slovo
    user["neotgad"] = neotgad
    user["otgad"] = []
    user["podskazka"] = podskazka
    update_data(baza)
    bot.send_message(
        message.chat.id,
        f'Я загадал слово из {len(slovo)} букв. Можешь начинать отгадывать по одной букве. У тебя 8 жизней. Удачи!')