'''
lerning cdek api 

'''


import requests
#авторизация
url = 'https://api.cdek.ru/v2/oauth/token?parameters'
acc = '***'
pas = '***'
n = '1230119741' #номер заказа
session = requests.session()
ans = requests.post(url, {'grant_type' : 'client_credentials', 'client_id' : acc, 'client_secret' : pas})
https://api.cdek.ru/v2/orders
session.headers["access_token"] = "***" #from ans
session.headers["token_type"] = "bearer"


#запросыЖ
zurl = 'https://api.cdek.ru/v2/orders?cdek_number={cdek_number}'

headers = {	"Authorization": "Bearer " + session.headers["access_token"]}
zak = requests.get('https://api.cdek.ru/v2/orders?cdek_number=' + n, headers=headers, timeout=10)

session = requests.session()
ans = requests.post(url, {'grant_type' : 'client_credentials', 'client_id' : acc, 'client_secret' : pas})
https://api.cdek.ru/v2/orders