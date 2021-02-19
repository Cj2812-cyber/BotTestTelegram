import os
import random
from datetime import datetime
import inspect

from config import config_path

# метод получения случайного стикера из папки static
def get_bot_sticers(path):
    # Получаем список всех стикеров в папке static/stickers/start
    os.chdir(path)
    file_stick = []
    for root, dirs, files in os.walk(".", topdown=False):
        file_stick = files

    write_to_log(inspect.stack()[0][3], "DEBUG", "Получил стикер")

    return file_stick[random.randint(0, len(file_stick) - 1)]


# метод для записи лога
def write_to_log(application_name, level_log, log_text):
    try:
        file_log = open(config_path.PATH_TO_LOG + str(application_name) + ".txt", 'a', encoding="utf-8")
        file_log.write(str(datetime.now()) + " [" + level_log + "] - " + log_text + "\n")
    except Exception as e:
        print("Ошибка при записи лога\n" + e)