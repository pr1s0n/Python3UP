# -*-coding:utf-8 -*-
# @Author   ：pr1s0n
# @Time     : 2020/5/10 20:55
# @FileNAme : db_handler.py.py
# @Blog     : http://www.pr1s0n.com

import json
import os
from conf import settings


def select(username):
    user_path = os.path.join(
        settings.USER_DATA_PATH,f'{username}.json'
    )
    if os.path.exists(user_path):
        with open(user_path,'r',encoding='utf-8') as f:
            user_dic = json.load(f)
            return user_dic


def save(user_dic):
    username = user_dic.get('username')
    user_path = os.path.join(
        settings.USER_DATA_PATH,f'{username}.json'
    )
    with open(user_path,'w',encoding='utf-8') as f:
        json.dump(user_dic,f,ensure_ascii=False)