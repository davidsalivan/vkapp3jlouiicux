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
 
 
# API-����
token = "b38a2e1d74f3b0a0007740ac5205ee9d0738b9380695f916e38da6216ffd5aaefbbe1fc206cda8f6d91f0"
 
# ������������ ��� ����������
vk = vk_api.VkApi(token=token)
 
longpoll = VkLongPoll(vk)
print("��� �������")

# �������� ����
while True:
    time.sleep(5)
    for event in longpoll.listen():
 
        # ���� ������ ����� ���������
        if event.type == VkEventType.MESSAGE_NEW:
 
            if event.to_me:
 
                request = event.text
                randint = random.randint(100000000,900000000)
                request = request.lower()
                chat_id = vk.method('messages.getConversations')
                chat_id = chat_id['items']
                print(chat_id)

                # �������� ������ ������
                for check in request:
                   #id = vk.method('messages.getConversations')
                   #id = id['items'][0]['last_message']['from_id']
                   #print(id)'
                    if request == "������":
                        write_msg(randint, event.user_id, "������")
                    elif request == "����":
                        write_msg(randint, event.user_id, "���� :(")
                    if request == "��� ������":
                        write_msg(randint, event.user_id, "��� �����: https://vk.com/doc-111025026_498834322")
                    elif request == "�������":
                        write_msg(randint, event.user_id, "��� ��� � ����: ������ ���� ��� ������")                   
                    else:
                        write_msg(randint, event.user_id, "�� �����...")
