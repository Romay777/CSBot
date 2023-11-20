from aiogram.utils.keyboard import InlineKeyboardBuilder

pos_s = ['playerone', 'playertwo', 'playerthree', 'playerfour', 'playerfive']


# Buy / Sell player
async def get_buy_sell_kb():
    builder = InlineKeyboardBuilder()
    builder.button(text="Купить", callback_data="buy_player")
    builder.button(text="Продать", callback_data="sell_player")
    return builder.as_markup(resize_keyboard=True)


# Keyboard that shows user's players
async def get_nicknames_keyboard(nicknames):
    builder = InlineKeyboardBuilder()
    for i in range(5):
        builder.button(text=nicknames[i], callback_data="sell_" + nicknames[i])
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


# List of available positions
async def get_position_list(positions):
    builder = InlineKeyboardBuilder()
    has_free_pos = False
    for pos in pos_s:
        if positions[pos] == 0:
            builder.button(text=f"{pos_s.index(pos)+1}", callback_data=f"buy_on_{pos}")
            has_free_pos = True
    if not has_free_pos:
        builder.button(text="Нет доступных позиций\n[закрыть]", callback_data="close_message")
    return builder.as_markup(resize_keyboard=True)


# List of guns [doesn't matter]
async def get_guns_choice():
    builder = InlineKeyboardBuilder()
    builder.button(text="MAC-10", callback_data="gun_choosed")
    builder.button(text="UMP-45", callback_data="gun_choosed")
    builder.button(text="MP-7", callback_data="gun_choosed")
    return builder.as_markup(resize_keyboard=True)


# List of farm methods
async def get_farm_methods():
    builder = InlineKeyboardBuilder()
    builder.button(text="⚠️Подставной матч⚠️", callback_data="farm_by_fake_match")
    builder.button(text="♻️Обычный матч♻️", callback_data="farm_by_game")
    return builder.as_markup(resize_keyboard=True)


# List of Sides [A/B]
async def get_side_choice():
    builder = InlineKeyboardBuilder()
    builder.button(text="Медленно \"A!\"\U0001F977", callback_data="side_choosed")  # Ninja emoji here
    builder.button(text="Rush \"B!\"🤬", callback_data="side_choosed")
    return builder.as_markup(resize_keyboard=True)


async def get_bet_coefficient():
    builder = InlineKeyboardBuilder()
    builder.button(text="x1.2", callback_data="coefficient_1")
    builder.button(text="x1.5", callback_data="coefficient_2")
    builder.button(text="x2", callback_data="coefficient_3")
    return builder.as_markup(resize_keyboard=True)
