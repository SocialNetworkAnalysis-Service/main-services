# -*- coding: utf-8 -*-

import json
from colorama import init
from vk_api import VkApi
from vk_api.exceptions import AuthError, VkApiError
import re

TZ = 3600 * 3
USER_AGENT = 'KateMobileAndroid/52.4 (Android 8.1; SDK 27; armeabi-v7a; Xiaomi Redmi 5A; ru)'


config = {}


class Colors:
    INFO = '\033[34;1m'
    OK = '\033[32;1m'
    WARNING = '\033[33;1m'
    ERROR = '\033[31;1m'
    RESET = '\033[0m'


def con(text):
    print(text + Colors.RESET)


def captcha_handler(captcha):
    r = input('Введите капчу ' + captcha.get_url() + ': ').strip()
    return captcha.try_again(r)


def parsing_vk_user(user_id):
    init()

    global config
    try:
        with open('src/utils/config.json') as f:
            config = json.load(f)

    except FileNotFoundError:
        config = {'limit': 1000, 'types': {
            'chats': True, 'groups': True, 'users': True}}

        with open('config.json', 'w') as f:
            json.dump(config, f, indent=2)

    if config['limit'] <= 0:
        config['limit'] = 1e10
    s = 'vk1.a.gCAbNChe6Vfr5nQub_SQkSFsrSWzLJQs2j5kLh0tYP4XTdi6RzVdlZ1ri5R3NGbxDD6vgifSuYGeogdaBQzOHJP0SQ9fe-ixrC8YupvSfX2JTSVXcrfkHMIAI7zRJWrseYJ2qEtvI-gLnBb8zZflAe3VSjgsjjhthjoXDSy4brQv90cJc9m1y0vkJJSgPsMD64Wq-iBBjSe1om4DlreX4Q'
    if len(s) == 220:
        vk = VkApi(token=s, captcha_handler=captcha_handler)

        vk.http.headers.update({
            'User-agent': USER_AGENT,
            'Timeout': '10'
        })

    elif ':' in s:
        sp = s.split(':')
        vk = VkApi(sp[0], sp[1], app_id=2685278,
                   captcha_handler=captcha_handler)
        vk.http.headers.update({
            'User-agent': USER_AGENT,
            'Timeout': '10'
        })

        try:
            vk.auth(token_only=True)
        except AuthError:
            con(Colors.ERROR + 'Неверный логин или пароль')
            return
    else:
        con(Colors.WARNING + 'Введите данные для входа в виде "логин:пароль" или "токен"')
        return

    try:
        user = vk.method('users.get')[0]
    except VkApiError as ex:
        if ex.__dict__['error']['error_code'] == 5:
            error_text = 'неверный токен'
        else:
            error_text = str(ex)

        con(Colors.ERROR + 'Ошибка входа: ' + error_text)
        return
    con(Colors.OK + 'Вход выполнен')

    pr = vk.method('users.get', {
                   'user_id': user_id, 'fields': 'activities,about,bdate,books,career,education,schools,interests,universities'})
    formatted_string = str(pr)
    user_data = formatted_string.replace('[', '').replace(']', '').replace(
        '{', '').replace('}', ''). replace("'", '')
    groups = vk.method('users.getSubscriptions', {'user_id': user_id})
    del groups['users']
    groups = str(groups)
    groups = groups.replace('{', '').replace('}', '').replace('groups', '').replace(':', '').replace(
        'items', '').replace("'", '').replace("''", '').replace('[', '').replace(']', '').replace(' ', '')
    data_str = re.sub(r"count\d+,", "", groups)
    items = data_str.split(',')
    items = items[:10]
    users_groups = ''
    for item in items:
        try:
            subs = vk.method('groups.getById', {
                             'group_id': item, 'fields': 'activity,description'})
            filtered_subs = [{'name': item['name'], 'activity': item['activity'],
                              'description': item['description']} for item in subs]
            filtered_subs = str(filtered_subs)
            filtered_subs = filtered_subs.replace('[', '').replace(']', '').replace(
                '{', '').replace('}', '').replace("'", '').replace("'", '')
            users_groups += filtered_subs + '\n'
        except:
            print('error')
    print(user_data)
    print(users_groups)



