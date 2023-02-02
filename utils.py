import json
import random
from telebot import types


def update_data(new_data):
    with open("base.json", "w") as f:
        json.dump(new_data, f, indent=2)


def get_data():
    with open("base.json", "r") as f:
        data = json.load(f)
        return data


def add_user(message, baZa):
    struktura = {
        message.from_user.id:
            {
                "slovo": None,
                "otgad": [],
                "neotgad": None,
                "hp": 8,
                "podskazka": None,
                "points": 0,
                "nickname": message.from_user.username,
                "name": message.from_user.full_name
            }
    }
    baZa.update(struktura)
    update_data(baZa)


def update_user(message, baZa):
    user = baZa[str(message.from_user.id)]
    user['name'] = message.from_user.full_name
    user['nickname'] = message.from_user.username
    update_data(baZa)

def show(slovo1, otgad1):
    pustishka = ''
    for i in slovo1:
        if i in otgad1:
            pustishka += i
        else:
            pustishka += "_"
    return pustishka


def is_pizdaty_vvod(vvod):
    # проверить длинну
    # проверить букву на русскость
    vrb = "а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я".split(", ")
    if len(vvod) != 1:
        return False
    if vvod not in vrb:
        return False
    return True


def zagad_slov():
    with open("all_words.json", encoding="utf-8") as f:
        data = json.load(f)
        while True:
            slovo = random.choice(list(data.keys())).lower()
            if "-" in slovo:
                continue
            break
        neotgad = list(set(list(slovo)))
        podskazka = data[slovo]["definition"]
        return slovo, neotgad, podskazka


def klava():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Загадать слово")
    item2 = types.KeyboardButton("Выход")
    item3 = types.KeyboardButton("Определение из словаря Ефремовой")
    item4 = types.KeyboardButton("Счет / Таблица лидеров")
    markup.add(item1, item2)
    markup.add(item3)
    markup.add(item4)
    return markup


def sbros(user, baza):
    user["hp"] = 8
    user["otgad"] = []
    user["slovo"] = None
    user["neotgad"] = []
    user["podskazka"] = None
    update_data(baza)

def slov_leader(baza):
    slov_l = dict(sorted(baza.items(), key=lambda item: item[1]["points"], reverse=True))
    return slov_l

