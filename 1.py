#!/usr/local/bin/python
# -*- coding: utf-8 -*-

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
token = "1cdc7f16a8929ad4026a075b37577a3e6816397ee7706a6639f2708468938765bb74f53a0d8065d6d8f4f"
 
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
                   #id = vk.method('messages.getConversations')
                   #id = id['items'][0]['last_message']['from_id']
                   #print(id)
                    if request == "привет":
                        write_msg(randint, event.peer_id, "Привет")
                    elif request == "пока":
                        write_msg(randint, event.peer_id, "Пока :(")
                    if request == "дай замены":
                        write_msg(randint, event.peer_id, "Введите корпус ")
                    elif request == "начать":
                        write_msg(randint, event.peer_id, "Вот что я умею: Привет,Пока,Дай замены,1 корпус,2 корпус") 
                    if request == "1 корпус":
                        write_msg(randint, event.peer_id, "Вот держи замены 1 корпуса: https://vk.com/doc-111025026_499974580")
                    elif request == "2 корпус":
                        write_msg(randint, event.peer_id, "Вот держи замены 2 корпуса: https://vk.com/doc-111025026_499974594")						
                    else:
                        write_msg(randint, event.peer_id, "Не понял...")
