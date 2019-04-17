#!/usr/bin/python
# -*- coding: cp1251 -*-
import os, sys
import time
import vk_api
import random
import requests
from vk_api.longpoll import VkLongPoll, VkEventType
#import u_photo
 
 
def write_msg(rand_int, user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': rand_int})
 
 
# API-êëþ÷
token = "b38a2e1d74f3b0a0007740ac5205ee9d0738b9380695f916e38da6216ffd5aaefbbe1fc206cda8f6d91f0"
 
# Àâòîðèçóåìñÿ êàê ñîîáùåñòâî
vk = vk_api.VkApi(token=token)
 
longpoll = VkLongPoll(vk)
print("Áîò çàïóùåí")

# Îñíîâíîé öèêë
while True:
    time.sleep(5)
    for event in longpoll.listen():
 
        # Åñëè ïðèøëî íîâîå ñîîáùåíèå
        if event.type == VkEventType.MESSAGE_NEW:
 
            if event.to_me:
 
                request = event.text
                randint = random.randint(100000000,900000000)
                request = request.lower()
                chat_id = vk.method('messages.getConversations')
                chat_id = chat_id['items']
                print(chat_id)

                # Êàìåííàÿ ëîãèêà îòâåòà
                for check in request:
                   #id = vk.method('messages.getConversations')
                   #id = id['items'][0]['last_message']['from_id']
                   #print(id)'
                    if request == "привет":
                        write_msg(randint, event.user_id, "Привет")
                    elif request == "пока":
                        write_msg(randint, event.user_id, "Пока :(")
                    if request == "дай замены":
                        write_msg(randint, event.user_id, "вот держи: https://vk.com/doc-111025026_498834322")
                    elif request == "команды":
                        write_msg(randint, event.user_id, "Вот что я умею: Привет Пока Дай замены")                   
                    else:
                        write_msg(randint, event.user_id, "Не понял...")
