"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""


import subprocess
import chardet


ls_urls = ['yandex.ru', 'youtube.com']

for i in ls_urls:
    ping_res = subprocess.run(['ping', i], capture_output=True)
    encoding = chardet.detect(ping_res.stdout)['encoding']
    print(ping_res.stdout.decode(encoding).encode('utf-8').decode('utf-8'))