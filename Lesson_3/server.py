import socket
import json
from common.utils import get_message, send_message
from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, ERROR, \
    DEFAULT_PORT, MAX_CONNECTIONS


def process_client_message(message):
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message and message[USER][ACCOUNT_NAME] == 'Aleks':
        return {RESPONSE: 200}
    return {RESPONSE: 400,
            ERROR: 'Bad Request'}


def main():

    port = DEFAULT_PORT
    addr = ''

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((addr, port))
    transport.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        try:
            message_from_client = get_message(client)
            print(message_from_client)
            response = process_client_message(message_from_client)
            send_message(client, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорректное сообщение')
            client.close()


if __name__ == '__main__':
    main()
