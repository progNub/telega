import requests
import json

webpage = requests.get('https://www.nbrb.by/api/exrates/rates/431')
DOLLAR = webpage.json()
print(DOLLAR.get('Cur_OfficialRate'))



# with open("valuta.json", "w+") as f:
#     json.dump(webpage.json(), f)
#
# js_file = {}
# with open("valuta.json", "r") as f:
#     js_file = json.loads(f.read())
# data = {}
# with open('valuta.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)
#
# print(data.get('Cur_OfficialRate'))
# print(js_file)
