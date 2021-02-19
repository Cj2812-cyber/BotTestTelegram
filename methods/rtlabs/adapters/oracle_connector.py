import cx_Oracle # для подключения и работы с базой Oracle

from config import config_path

from loader import config_oracle


# инициализация бибилиотеки Оракла для работы с базой
def load_library_oracle():
    try:
        cx_Oracle.init_oracle_client(lib_dir=config_path.PATH_TO_CLIENT_FROM_ORACLE)
    except Exception as e:
        print("Не смог загрузить библеотеку cx_Oracle клиента \n" + e)


# Контекст менеджер, создает соединение с БД Oracle, и сам закрывает его, когда все действия в его рамках выполнены
# https://www.youtube.com/watch?v=EYq75XlmNDs
class ConnectToOracle(object):

    def __init__(self):
        self.__class__.count_session = 0 #счетчик открытых соединений


    def __enter__(self):
        try:
            self.connection = cx_Oracle.connect(config_oracle.ORACLE_USER, config_oracle.ORACLE_PASS,
                                           config_oracle.ORACLE_HOST_SN)
            self.cursor = self.connection.cursor()

            self.__class__.count_session += 1

            print("Соедениение c БД Oracle " + str(self.__class__.count_session) + " установленно")

            return self.cursor

        except Exception as e:
            print("Не смог подключиться к БД Oracle\n" + str(e))


    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.connection.close()

            print("Соедениение c БД Oracle " + str(self.__class__.count_session) + " закрыто")

            self.__class__.count_session -= 1
        except Exception as e:
            print("Не смог закрыть соединение c БД Oracle\n" + e)


#устаревший способ подключения
'''
#connection: cx_Oracle
#count_session: int = 0

# подключение к БД оракле и получениек cursor
def connect_to_oracle():
    try:
        global count_session
        global connection

        connection = cx_Oracle.connect(config_oracle.ORACLE_USER, config_oracle.ORACLE_PASS, config_oracle.ORACLE_HOST_SN)
        cursor = connection.cursor()

        count_session += 1

        print("Соедениение " + str(count_session) + " установленно")

        return cursor
    except Exception as e:
        print("Не смог подключиться к БД\n" + str(e))


# закрытие соединение с базой
def close_conn_oracle():

    global connection
    global count_session
    connection.close()

    print("Соедениение " + str(count_session) + " закрыто")

    count_session -= 1
    
'''
