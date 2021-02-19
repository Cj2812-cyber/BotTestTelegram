from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from methods import methods_bot
from config import config_path

@dp.message_handler(commands="cancel", state="*")
async def cmd_cancel(message: types.Message, state: FSMContext):

    await state.finish()
    await message.answer("Действие отменено!", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(commands=['start'])
async def cdm_start(message: types.Message, state: FSMContext):

    await dp.current_state(user=message.from_user.id).finish()
    # получаем случайный стикер для приветственного сообщения
    with open(methods_bot.get_bot_sticers(config_path.PATH_TO_STICS_START), 'rb') as stickers:
        await message.answer_sticker(stickers)

    await message.answer("Привет, {0.first_name}!\nЯ бот созданный что бы помогать по работе сотрудникам РТЛабс\n"
                         "Если хочешь узнать что я могу, введи команду /help".format(message.from_user), reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(commands=['help'], state="*")
async def cmd_help(message: types.Message, state: FSMContext):

    await state.finish()
    # получаем случайный стикер для сообщения по команде /help
    with open(methods_bot.get_bot_sticers(config_path.PATH_TO_STICS_HELP), 'rb') as stickers:
        await message.answer_sticker(stickers)

    # открываем и выводим содержимое файла help.txt
    with open(config_path.PATH_TO_HELP) as file_help:
        text_help = file_help.read()
    await message.answer(str(text_help))



@dp.message_handler(regexp='отмена')
async def cmd_cancel(message: types.Message, state: FSMContext):

        await dp.current_state(user=message.from_user.id).finish()
        await message.answer("Действие отменено!", reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(content_types=['text'])
async def response_on_text_message(message: types.Message):
    await message.answer("Знал бы, что ты пишешь, ответил бы, а так...")
