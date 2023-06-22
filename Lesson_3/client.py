
import json
import socket
import time
from common.utils import get_message, send_message
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT


def create_presence(account_name='Aleks'):

    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return out


def process_ans(message):
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


def main():

    addr = DEFAULT_IP_ADDRESS
    port = DEFAULT_PORT

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((addr, port))
    message_to_server = create_presence()
    send_message(transport, message_to_server)

    try:
        answer = process_ans(get_message(transport))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение')


if __name__ == '__main__':
    main()
