from aiogram.utils.keyboard import ReplyKeyboardBuilder


# Main menu
def menu(is_admin=False):
    builder = ReplyKeyboardBuilder()
    builder.button(text="💸 Баланс"), builder.button(text="🎮 Моя команда")
    builder.button(text="👤 Список игроков"), builder.button(text="💰 Купить/Продать игрока")
    builder.button(text="🤑 Фармить")
    if is_admin:
        builder.button(text="set user balance"), builder.button(text="get user balance")
        builder.button(text="ban user"), builder.button(text="unban user")
        builder.adjust(3, 2, 2, 2)
    else:
        builder.adjust(2, 2, 1)
    return builder.as_markup(resize_keyboard=True, input_field_placeholder="Выберите действие")


def back_button():
    builder = ReplyKeyboardBuilder()
    builder.button(text="↩️ Отмена")
    return builder.as_markup(resize_keyboard=True)
