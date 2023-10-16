from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.utils.dbconnect import Request



# Buy / Sell player
def buy_sell_kb():
    builder = InlineKeyboardBuilder()
    builder.button(text="Купить", callback_data="buy_player")
    builder.button(text="Продать", callback_data="sell_player")
    return builder.as_markup(resize_keyboard=True)


# List of farm methods
def farm_methods_kb():
    builder = InlineKeyboardBuilder()
    builder.button(text="MAC-10", callback_data="mac-10")
    builder.button(text="UMP-45", callback_data="ump-45")
    builder.button(text="MP-7", callback_data="mp-7")
    return builder.as_markup(resize_keyboard=True)


# List of Sides [A/B]
def choose_side_kb():
    builder = InlineKeyboardBuilder()
    builder.button(text="Медленно \"A!\"\U0001F977", callback_data="side-a")  # Ninja emoji here
    builder.button(text="Rush \"B\"!🤬", callback_data="side-b")
    return builder.as_markup(resize_keyboard=True)


# Keyboard that shows user's players
def get_nicknames_keyboard(nicknames):
    builder = InlineKeyboardBuilder()
    for i in range(0, 5):
        builder.button(text=nicknames[i], callback_data="sell_" + nicknames[i])
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)
