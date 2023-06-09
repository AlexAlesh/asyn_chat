"""
Задание 3.

Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""


ls_str = ['attribute','класс','функция', 'type']

for i in ls_str:
    try:
        st_b = bytes(i, 'ascii')
    except UnicodeEncodeError:
        st_b = f'"{i}" невозможно записать в байтовом виде'
    print(f'Тип:{type(st_b)}. Содержимое:{st_b}. ')