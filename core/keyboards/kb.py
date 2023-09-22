from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup)

# Main menu
main_menu = [
    [KeyboardButton(text="💸 Баланс"), KeyboardButton(text="🎮 Моя команда")],
    [KeyboardButton(text="👤 Список игроков"), KeyboardButton(text="💰 Купить/Продать игрока")],
    [KeyboardButton(text="🤑 Фармить")]
]
menu = ReplyKeyboardMarkup(keyboard=main_menu, resize_keyboard=True, input_field_placeholder="Выберите действие")

# Buy / Sell player
buy_sell = [
    [InlineKeyboardButton(text="Купить", callback_data="buy_player")],
    [InlineKeyboardButton(text="Продать", callback_data="sell_player")]
]
buy_sell_player = InlineKeyboardMarkup(inline_keyboard=buy_sell, resize_keyboard=True)

# List of farm methods
farm_list = [
    [InlineKeyboardButton(text="MAC-10", callback_data="mac-10")],
    [InlineKeyboardButton(text="UMP-45", callback_data="ump-45")],
    [InlineKeyboardButton(text="MP-7", callback_data="mp-7")]
]
choose_farm = InlineKeyboardMarkup(inline_keyboard=farm_list, resize_keyboard=True)
