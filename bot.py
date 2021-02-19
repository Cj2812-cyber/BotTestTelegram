import logging
from aiogram import executor

import handlers # необходимо что бы начли обрабатывать handlers в пакете handlers
import states

from loader import dp, set_commands
from utils.notify_admins import on_startup_notify
from methods.rtlabs.adapters import oracle_connector

logger = logging.getLogger(__name__)

async def on_startup(dispatcher):

    oracle_connector.load_library_oracle() # инициализхируем библиотеку клиента Oracle
    await set_commands(dispatcher.bot)
    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


async def close_bot(dispatcher):
    #await dispatcher.bot.message.answer("Бот ушел!")
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

# если мы запускаем именно данный файл, выполнится код в этом условии, если будет вызван этот файл путем import в других
# файлах, то данный код не выполнится
if __name__ == '__main__':
    print("Run!")
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=close_bot)
    # инициализация бибилиотеки Оракла для работы с базой


