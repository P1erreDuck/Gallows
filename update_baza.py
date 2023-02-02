import json
from utils import get_data, update_data

old_baza = get_data()
new_baza = {}
for k, v in old_baza.items():
    print(k,v)
    user = old_baza[k]
    if "nickname" not in user:
        user["nickname"] = None
    if "points" not in user:
        user["points"] = 0
    if "name" not in user:
        user["name"] = None
    new_baza[k] = user
update_data(new_baza)


        