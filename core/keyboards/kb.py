from aiogram.utils.keyboard import ReplyKeyboardBuilder


# Main menu
def menu():
    builder = ReplyKeyboardBuilder()
    builder.button(text="💸 Баланс"), builder.button(text="🎮 Моя команда")
    builder.button(text="👤 Список игроков"), builder.button(text="💰 Купить/Продать игрока")
    builder.button(text="🤑 Фармить")
    builder.adjust(2, 2, 1)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder="Выберите действие")


def admin_panel():
    builder = ReplyKeyboardBuilder()
    builder.button(text="💸 Баланс"), builder.button(text="🎮 Моя команда")
    builder.button(text="👤 Список игроков"), builder.button(text="💰 Купить/Продать игрока")
    builder.button(text="🤑 Фармить")
    builder.button(text="set user balance"), builder.button(text="ban user")
    builder.adjust(3, 2, 2)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder="Выбериет действие")
