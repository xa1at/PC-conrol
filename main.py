import time

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

from utils.config import settings
from utils.imports_all import *


session = vk_api.VkApi(token=settings['api_group_vk'])
get_apis = session.get_api()
check_longpoll = VkBotLongPoll(session, group_id=settings['group_id'])
prefix = settings['prefix']


def send_messages(ids, some_text):
    session.method("messages.send", {"user_id": ids, "message": some_text, "random_id": 0})


def send_messages_plus_keyboard(ids, some_text, keyboard):
    session.method('messages.send', {'user_id': ids, 'message': some_text, 'keyboard': keyboard,
                                     'random_id': get_random_id()})


send_messages(settings['owner_id'], f'Скрипт успешно запущен! {time.ctime()}')
for event in check_longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        msg = event.message['text']
        users_id = event.message['peer_id']

        if msg == prefix + 'check':
            send_messages(users_id, f'Скрипт работает.\n {time.ctime()}')
        elif msg in ['menu', 'меню', '/menu', 'ьутг']:
            send_messages_plus_keyboard(users_id, 'Меню: \n'
                                                  'Лист 1', main_keyboard())
        elif msg == '➡':
            send_messages_plus_keyboard(users_id, 'Меню: \n'
                                                  'Лист 2', second_main_keyboard())
        elif msg == '⬅':
            send_messages_plus_keyboard(users_id, 'Меню: \n'
                                                  'Лист 1', main_keyboard())
        elif msg == prefix + 'help':
            send_messages(users_id, help_commands_function())
        elif msg == prefix + 'micro':
            main_record_audio(users_id=users_id)
        elif msg == prefix + 'off':
            send_messages(users_id, 'Выключил ПК!!')
            function_off_pc()
        elif msg == prefix + 'restart':
            send_messages(users_id, 'ПК ушел на перезагрузку.')
            function_restart_pc()
        elif msg == prefix + 'block':
            send_messages(users_id, 'Экран заблокирован!')
            function_block_screen()
        elif msg == prefix + 'blue':
            from funcrions.blue_screen import function_blue_screen
            send_messages(users_id, 'Опасная штучка, такое лучше не делать в следующий раз.\n'
                                    'Но все равно, функция выполнена успешно!')
            function_blue_screen()
        elif msg == prefix + 'process':
            send_messages(users_id, get_process())
        elif msg == prefix + 'screen':
            main_function_screenshot(users_id=users_id)
        elif msg == prefix + 'info_pc':
            send_messages(users_id, pc_information())
        elif msg == prefix + 'minimize':
            send_messages(users_id, 'Окна свернуты!')
            function_for_minimize_all_windows()
        elif msg == prefix + 'photo':
            main_web_photo(users_id=users_id)
        elif msg == prefix + 'sleep':
            send_messages(users_id, 'ПК ушел в спящий режим.')
            function_sleep_mode()
        elif (prefix + 'heather') in msg:
            city = msg[::]
            heather_check(city=city)
        elif (prefix + 'open') in msg:
            function_open_url(text=msg[5::])
        elif (prefix + 'start') in msg:
            function_start_program(program_name=msg[5::])
        elif (prefix + 'set') in msg:
            main_wallpaper_function(event=event)
