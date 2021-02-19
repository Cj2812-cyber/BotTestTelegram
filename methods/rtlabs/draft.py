# methods
from config import config_path

import requests  # библиотека для работы с запросами через https GET, POST, PUT, DELETE
import re  # регулярные выражения

#from oracle import connect_to_oracle, close_conn_oracle
from methods.rtlabs.adapters import oracle_connector


# метод получения черновика по заявлению из Cassandra (1047501078/1014798542)
def get_draft_of_cassandra(text):

    try:

        orders :list = formating_order_message(text) # список заявлений по которым, необходимо достать черновики
        users :list = get_oid_user(orders)
        files = [] # список файлов черновиков, которые нужно отправить сообщением в боте

        for index, (order, user_id) in enumerate(zip(orders, users)):
            # создаем/перезаписываем файл с черновиком
            with open(config_path.PATH_TO_SAVE_DRAFT + 'draft_' + str(order) + '.txt', 'w', encoding="utf-8") as f:

                headers = {'content-type': "application/json", 'token': str(user_id) + '@@@@1'}
                resp = requests.get(config_path.URL_GET_DRAFT + str(order), headers=headers)
                f.write(resp.text)

            files.append(open(config_path.PATH_TO_SAVE_DRAFT + 'draft_' + str(order) + '.txt', 'rb'))

        # возвращаем файл в двоичном виде, что бы можно было отправить в бота
        return files

    except Exception as e:
        print(repr(e))

# форматирование текста из сообщения бота, на выходе возвращается список заявлений
def formating_order_message(message_text):
    orders_set = set()
    orders = []

    if (message_text.find('\n')):

        #message_text = re.sub('\n', ',', message_text)
        message_text = re.sub('\D+', ',', message_text)
        text = message_text.split(',')
        for order in text:
            if order != "":
                orders_set.add(order)

    for order in orders_set:
        orders.append(order)

    return orders


# получение списка user_id для списка заявлений по которым необходим черновик
def get_oid_user(orders):

    with oracle_connector.ConnectToOracle() as cursor:
        #cursor = oracle.connect_to_oracle()
        users_id = []

        for order_id in orders:
            cursor.execute(r"select user_id from lk.order_hist where order_id = :order_id", {"order_id": order_id})
            users_id.append(re.sub(r'\D+', '', str(cursor.fetchone())))  # забираем результат выполнения запроса, в курсоре остается пустота

        #oracle.close_conn_oracle()

    return users_id