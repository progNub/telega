import requests
import json

file_name = "databases/valuta.json"


def get_rate(id="431"):
    temp = '0000'
    id = str(id)
    try:
        webpage = requests.get(f'https://www.nbrb.by/api/exrates/rates/{id}')
        DOLLAR = webpage.json()
        temp = DOLLAR.get('Cur_OfficialRate')
    except:
        print(f'not answer from https://www.nbrb.by/api/exrates/rates/{id}')
    return temp


def get_all_rates():
    temp = "0000"
    try:
        webpage = requests.get("https://www.nbrb.by/api/exrates/currencies")
        temp = webpage.json()
    except:
        print('not answer from https://www.nbrb.by/api/exrates/currencies')
    return temp


def write_to_json():
    try:
        with open(file_name, 'w+') as f:
            json.dump(get_all_rates(), f, indent=2)
            print("write complite")
    except IOError:
        print("write is not complete: " + file_name)

