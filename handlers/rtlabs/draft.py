#handlers
from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from states.rtlabs import draft as stats_draft
from methods.rtlabs import draft



@dp.message_handler(commands=['drafts'])
async def start_get_draft(message: types.Message):

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.add("Отмена")
    #state = dp.current_state(user=message.from_user.id)

    await message.answer("Укажите номер(а) заявлений для которых необходимы черновики", reply_markup=keyboard)
    await dp.current_state(user=message.from_user.id).set_state(stats_draft.DraftCassandra.waiting_for_order_id)


@dp.message_handler(commands="cancel", state="*")
async def cmd_cancel(message: types.Message, state: FSMContext):

    await state.finish()
    await message.answer("Действие отменено!", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler(state=stats_draft.DraftCassandra.waiting_for_order_id)
async def send_to_draft_in_bot(message: types.Message, state: FSMContext):

    orders_id = message.text
    drafts = draft.get_draft_of_cassandra(orders_id)
    for file in drafts:
        await message.answer_document(file)

    await message.answer("Черновики сохранены!", reply_markup=types.ReplyKeyboardRemove())

    # сброс состояний и хранимых в них переменных
    await state.finish()
