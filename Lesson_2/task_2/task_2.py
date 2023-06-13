"""
### 2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл orders.json.
При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""

import json
import os

def write_order_to_json(item, quantity, price, buyer, date):

    f_name="orders.json"
    orders = {'orders':[]}
    if os.path.exists(f_name):  # если файл не существует, создадим его ниже, open(f_name, 'w')
        with open(f_name, "r", encoding="utf-8") as file:
            orders = json.load(file)
        orders['orders'].append({
                                    "item": item,
                                    "quantity": quantity,
                                    "price": price,
                                    "buyer": buyer,
                                    "date": date
                                })
    with open(f_name,"w",encoding="utf-8",) as file:
        json.dump(orders, file, indent=4, ensure_ascii=False)


#write_order_to_json('PS', 8, 4000, 'Sony', '02.02.2023')
write_order_to_json('Laptop', 3, 200, 'Micron', '02.01.2023')