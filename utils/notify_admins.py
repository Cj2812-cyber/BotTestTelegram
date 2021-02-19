import logging

from aiogram import Dispatcher, types

from loader import config_bot


async def on_startup_notify(dp: Dispatcher):
    #for admin in ADMINS:
    try:
        await dp.bot.send_message(config_bot.ADMIN_ID, "Бот Запущен", reply_markup=types.ReplyKeyboardRemove())

    except Exception as err:
        logging.exception(err)