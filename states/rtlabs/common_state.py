from aiogram.utils.helper import Helper, HelperMode, ListItem


class CommonStates(Helper):
    mode = HelperMode.snake_case

    STATE_DRAFT = ListItem()
    STATE_LOGS = ListItem()
