from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup)

# Main menu
main_menu = [
    [KeyboardButton(text="💸 Баланс"), KeyboardButton(text="🎮 Моя команда")],
    [KeyboardButton(text="👤 Список игроков"), KeyboardButton(text="💰 Купить/Продать игрока")],
    [KeyboardButton(text="🤑 Фармить")]
]
menu = ReplyKeyboardMarkup(keyboard=main_menu, resize_keyboard=True, input_field_placeholder="Выберите действие")


