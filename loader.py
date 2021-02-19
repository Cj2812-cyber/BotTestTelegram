import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand

from config import config_parser


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Запуск бота"),
        BotCommand(command="/help", description="Получить справку"),
        BotCommand(command="/drafts", description="Получить черновик заявления из Cassandra"),
        BotCommand(command="/get_file_s3", description="Получить файл с хранилища S3"),
        BotCommand(command="/logs", description="Получить логи с сервера логов"),
        BotCommand(command="/cancel", description="Отмена текущих сценариев"),
        BotCommand(command="/test", description="Тестовая команда")
    ]
    await bot.set_my_commands(commands)

# инициализация данных для подключения к Боту
#load_base_config()
config_bot = config_parser.load_config_bot()

bot = Bot(token=config_bot.TELEGRAM_BOT_TOKEN_API)
ADMIN_ID = config_bot.ADMIN_ID
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# инициализация данных для подключения к серверам по SSH
config_ssh = config_parser.load_config_SSH()

# инициализация данных для подключения к БД Oracle
config_oracle = config_parser.load_config_oracle()

if __name__ == '__main__':
    print("Loader!")