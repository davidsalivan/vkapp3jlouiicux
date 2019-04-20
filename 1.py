#!/usr/bin/python
# -*- coding: cp1251 -*-
import os, sys
import time
import vk_api
import random
import requests
import json
from vk_api.longpoll import VkLongPoll, VkEventType
#import u_photo
 
 
def write_msg(rand_int, user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': rand_int})

# API-ключ
token = "8f1fe8bac0b998eb67226f3751e6fe94bfefa5602e4179fb459c1571b69b27f0f4023e97a07d0fbaf9a81"
 
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk)
print("Бот запущен")

# Основной цикл
while True:
    time.sleep(5)
    for event in longpoll.listen():
 
        # Если пришло новое сообщение
        if event.type == VkEventType.MESSAGE_NEW:
 
            if event.to_me:
 
                request = event.text
                randint = random.randint(100000000,900000000)
                request = request.lower()
                chat_id = vk.method('messages.getConversations')
                chat_id = chat_id['items']
                print(chat_id)

                # Каменная логика ответа
                for check in request:
                   #id = vk.method('messages.getConversations') # заготовка на будущее!
                   #id = id['items'][0]['last_message']['from_id']
                   #print(id)'
                    if request == "привет":
                        write_msg(randint, event.user_id, "Привет")
                    elif request == "пока":
                        write_msg(randint, event.user_id, "Пока :(")
                    if request == "дай замены":
                        write_msg(randint, event.user_id, "вот держи: https://vk.com/doc-111025026_499228899") #тут надо менять ссылку потому что парсер не особо умею писать!
                    elif request == "начать":
                        write_msg(randint, event.user_id, "Вот что я умею: Привет Пока Дай замены")                   
                    else:
                        write_msg(randint, event.user_id, "Не понял...")
