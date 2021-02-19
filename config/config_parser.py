from dataclasses import dataclass

from dotenv import load_dotenv
import os

load_dotenv()


# получение данных для доступа к Боту
@dataclass
class TgBot:

    TELEGRAM_BOT_TOKEN_API: str
    ADMIN_ID: int


def load_config_bot():

    TgBot.TELEGRAM_BOT_TOKEN_API = os.getenv("TELEGRAM_BOT_TOKEN_API") # получаем токен из переменной окружения
    TgBot.ADMIN_ID = os.getenv("ADMIN_ID")

    return TgBot


# получение данных для подключения к БД Oracle
@dataclass
class OracleConn:

    ORACLE_USER: str
    ORACLE_PASS: str
    ORACLE_HOST_SN: str


def load_config_oracle():

    OracleConn.ORACLE_USER = os.getenv("ORACLE_USER")
    OracleConn.ORACLE_PASS = os.getenv("ORACLE_PASS")
    OracleConn.ORACLE_HOST_SN = os.getenv("ORACLE_HOST_SN")

    return OracleConn


# получение данных для подключения к серверам по SSH
@dataclass
class SSHConn:
    CONNECT_TO_SSH = {}


def load_config_SSH():

    SSHConn.CONNECT_TO_SSH['host'] = os.getenv("SSH_HOST")
    SSHConn.CONNECT_TO_SSH['login'] = os.getenv("SSH_LOGIN")
    SSHConn.CONNECT_TO_SSH['password'] = os.getenv("SSH_PASS")
    SSHConn.CONNECT_TO_SSH['port'] = os.getenv("SSH_PORT")

    return SSHConn.CONNECT_TO_SSH



def decor_load_config(load_config_bot, load_config_oracle, load_config_SSH):

    def load_all_config():

        print("Начало загрузки конфигурационных файлов ...")
        load_config_bot()
        load_config_oracle()
        load_config_SSH()
        print("Конфигурационный файлы успешно загружены!")

    return load_all_config

load_base_config = decor_load_config(load_config_bot, load_config_oracle, load_config_SSH)
