from aiogram.dispatcher.filters.state import State, StatesGroup

class DraftCassandra(StatesGroup):
    waiting_for_order_id = State()