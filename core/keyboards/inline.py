from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)

# Buy / Sell player
buy_sell = [
    [InlineKeyboardButton(text="Купить", callback_data="buy_player")],
    [InlineKeyboardButton(text="Продать", callback_data="sell_player")]
]
buy_sell_kb = InlineKeyboardMarkup(inline_keyboard=buy_sell, resize_keyboard=True)

# List of farm methods
farm_list = [
    [InlineKeyboardButton(text="MAC-10", callback_data="mac-10")],
    [InlineKeyboardButton(text="UMP-45", callback_data="ump-45")],
    [InlineKeyboardButton(text="MP-7", callback_data="mp-7")]
]
farm_kb = InlineKeyboardMarkup(inline_keyboard=farm_list, resize_keyboard=True)

# List of Sides [A/B]
choose_side_list = [
    [InlineKeyboardButton(text="Медленно \"A!\"\U0001F977", callback_data="side-a")],  # Ninja emoji here
    [InlineKeyboardButton(text="Rush \"B\"!🤬", callback_data="side-b")]
]
choose_side_kb = InlineKeyboardMarkup(inline_keyboard=choose_side_list, resize_keyboard=True)
