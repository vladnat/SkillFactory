import requests, json

def get_values(url):
    dict_ = {}

    for el in json.loads(requests.get(url).text):
        if el['Cur_ID'] == 298:
            dict_['RUB'] = el['Cur_OfficialRate'] / 100
        if el['Cur_ID'] == 145:
            dict_['USD'] = el['Cur_OfficialRate']
        if el['Cur_ID'] == 292:
            dict_['EUR'] = el['Cur_OfficialRate']  
    return dict_

values = get_values('https://www.nbrb.by/api/exrates/rates?periodicity=0')

class ConvertExeptions(Exception):
    pass
