# -*- coding: utf-8 -*-
from flask import Flask
from flask_sslify import SSLify
from flask import request
from flask import jsonify
import telebot
import requests
from bs4 import BeautifulSoup
from telebot import types
import json
from time import sleep
from time import time
bot = telebot.TeleBot("***")
count_req = int(0)


app = Flask (__name__)
sslify = SSLify(app)


def write_json(data, filename = 'temp.json'):
    with open(filename, 'a') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        try:
            chat_id = r['message']['chat']['id']
            message = r['message']['text']
        #global count_req
        #count_req += 1
        #log_data = [count_req, r['message']['chat']['id'], r['message']['date'], message]
        #write_json(log_data)
        #cw = 'Колличество запросов с момента старта:' + str(count_req)

            if message == '/start' or message == '/help':
                send_welcome(chat_id)
            #elif message == '/count':
            #    bot.send_message(chat_id, cw)
            else:
                snd_msg(message, chat_id)
        except:
            return jsonify(r)
        else:
            return jsonify(r)
    return '<h1> the BOT is lvng hr, mail 2 the Creator if u need smthg: 14hp@ngs.ru </h1>'

@app.route('/bot_log', methods=['POST', 'GET'])
def bot_log():
    with open('temp.json', 'r') as f:
        data_b = f.readlines()
        data_b.append(str(count_req))
    return jsonify(data_b)

def get_url (data) ->str:
    b = (str(data).find('http'))
    e = (str(data).find('"', str(data).find('http')))
    url = str(data)[b:e]
    return url

def send_welcome(chat_id):
    markup = types.ReplyKeyboardMarkup(row_width=3)
    itembtn1 = types.KeyboardButton('Мамоново - Гроново')
    itembtn2 = types.KeyboardButton('Мамоново - Гжехотки')
    itembtn3 = types.KeyboardButton('Багратионовск - Безледы')
    itembtn4 = types.KeyboardButton('Гусев - Голдап')
    itembtn5 = types.KeyboardButton('Морское - Нида')
    itembtn6 = types.KeyboardButton('Чернышевское - Кибартай')
    itembtn7 = types.KeyboardButton('Советск - Панемуне')
    itembtn8 = types.KeyboardButton('Пограничный - Рамонишкяй')
    itembtn9 = types.KeyboardButton('/help')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9)
    bot.send_message(chat_id, "Этот бот находится в разработке. Пока, данные с камер могут поступать с задержкой, но скоро мы наладим их мгновенную отправку прямиком в ваш смартфон! Мы будем признательны, если вы сообщите о любых обнаруженных ошибках на почту 14hp@ngs.ru. А пока вы можете выбрать камеры какого пункта вам нужно показать:", reply_markup=markup)

def snd_msg (message, chat_id):

    if message == 'Мамоново - Гроново':
        bot.send_message(chat_id, "Загружаю данные с камер на границе (может занять какое то время):")
        bot.send_photo(chat_id, photo=('http://artica.ru/granica_bot_img/gronovo-in.jpg'+ '?' + str(time())), caption="Въезд на российскую границу (RU -> PL)")
        bot.send_photo(chat_id, photo=('http://artica.ru/granica_bot_img/gronovo-out.jpg'+ '?' + str(time())), caption= "Нейтральная территория")
        bot.send_photo(chat_id, photo=('http://artica.ru/granica_bot_img/gronovo-pl.jpg' + '?' + str(time())), caption= "Въезд на польскую границу (PL -> RU)")
        bot.send_photo(chat_id, photo=('http://artica.ru/granica_bot_img/gronovo-out2.jpg' + '?' + str(time())), caption= "Выезд с российской границы (RU -> PL)")

    elif message == 'Мамоново - Гжехотки':
        bot.send_message(chat_id, "Загружаю данные с камер на границе (может занять какое то время):")
        bot.send_photo(chat_id, photo=('http://artica.ru/granica_bot_img/grzhechotki-in.jpg' + '?' + str(time())), caption= "Въезд на российскую границу со стороны России (RU -> PL). Если видишь здесь много машин — значит дело дрянь... общее время прохождения границы от 6 до 9 часов")
        bot.send_photo(chat_id, photo=('http://artica.ru/granica_bot_img/grzhechotki-pl.jpg' + '?' + str(time())), caption= "Въезд на польскую границу со стороны Польши (PL -> RU)")
        bot.send_photo(chat_id, photo=('http://artica.ru/granica_bot_img/grzhechotki-out2.jpg' + '?' + str(time())), caption= "Нейтральная территория. Если здесь пробка значит общее время прохождения границы составит от 3 до 5 часов")

    elif message == 'Багратионовск - Безледы':

        bot.send_message(chat_id, "Загружаю данные с камер на границе (может занять какое то время):")
        #bot.send_message(chat_id, '')
        bot.send_photo(chat_id, photo=('http://artica.ru/granica_bot_img/bezledy-pl.jpg' + '?' + str(time())))
        #bot.send_message(chat_id, "")
        bot.send_photo(chat_id, photo=('http://artica.ru/granica_bot_img/bezledy-out2.jpg' + '?' + str(time())))

    elif message == 'Гусев - Голдап':
        bot.send_message(chat_id, "Загружаю данные с камер на границе (может занять какое то время):")
        # bot.send_message(chat_id, '')
        bot.send_photo(chat_id, photo=('http://artica.ru/granica_bot_img/goldap-in.jpg' + '?' + str(time())))
        # bot.send_message(chat_id, "")
        bot.send_photo(chat_id, photo=('http://artica.ru/granica_bot_img/goldap-pl.jpg' + '?' + str(time())))

    elif message == 'Морское - Нида':
        bot.send_message(chat_id, "Загружаю данные с камер на границе (может занять какое то время):")
        # bot.send_message(chat_id, '')
        bot.send_photo(chat_id, photo=('http://artica.ru/granica_bot_img/nida-out.jpg' + '?' + str(time())))

    elif message == 'Чернышевское - Кибартай':
        bot.send_message(chat_id, "Загружаю данные с камер на границе (может занять какое то время):")
        # bot.send_message(chat_id, '')
        bot.send_photo(chat_id, photo=('http://artica.ru/granica_bot_img/kibartai-in.jpg' + '?' + str(time())))

    elif message == 'Советск - Панемуне':
        bot.send_message(chat_id, "Актуальных данных нет. Обновление камер на этом пункте, приостановлено.")

    elif message == 'Пограничный - Рамонишкяй':
        bot.send_message(chat_id, "Актуальных данных нет. Обновление камер на этом пункте, приостановлено.")
    else:
        bot.send_message(chat_id, "Извини, в ответах я ограничен - правильно задавай вопросы /start")


if __name__ == '__main__':

    app.run()
