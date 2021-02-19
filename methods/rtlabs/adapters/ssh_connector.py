import paramiko  # библиотека для работы по SSH

from loader import config_ssh

from config import config_path

# Контекст менеджер для установки соединения по SSH
class SSHConnectFromSSH:

    def __init__(self, sftp:bool):
        self.__class__.connect_count = 0
        self.sftp = sftp

    def __enter__(self):
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            # Подключение
            self.client.connect(hostname=config_ssh['host'], username=config_ssh['login'],
                       password=config_ssh['password'], port=config_ssh['port'])

            self.__class__.connect_count += 1
            print("Соединение по SSH " + str(self.__class__.connect_count) + " установлено")

            if self.sftp is True:
                # устанавливаем режим работы с сервером как SFTP
                self.ftp = self.client.open_sftp()
                return self.ftp
            else:
                return self.client

        except Exception as e:
            print("Не удалось установить соединение по SSH\n" + e)

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.client.close()

            print("Соединение по SSH " + str(self.__class__.connect_count) + " закрыто")

            self.__class__.connect_count -= 1

        except Exception as e:
            print("Не удалось закрыть соединение по SSH\n" + e)

#Test
'''
with SSHConnectFromSSH() as ftp:
    app_list = ftp.listdir(config_path.PATH_TO_LOGS_HORUS + '2021-02-08/sfapi')
    for app in app_list:
        print(app)
'''