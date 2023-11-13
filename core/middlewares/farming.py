from random import getrandbits, uniform, randint
from aiogram import types
from asyncio import sleep


async def default_farm(user_id, callback: types.CallbackQuery, request):
    await callback.message.edit_text("Коллим стратегию...", reply_markup=None)
    await sleep(round(uniform(1.1, 2.5), 1))
    await callback.message.edit_text("Заходим на точку...")
    await sleep(round(uniform(1.1, 2.5), 1))
    success = getrandbits(1)  # random value True-False
    current_msg_text = "Удачный entry-kill!🔥" if success else \
        f"Ошибка от <b>{await request.get_random_team_player(user_id)}</b>💢"
    await callback.message.edit_text(current_msg_text)
    result = (randint(8000, 10000) // 10) * 10 if success else 4000
    await sleep(1.3)
    #  STEP 1 END
    players_alive = randint(2, 5)
    current_msg_text = f"Наша команда осталась {players_alive} <b>vs</b> "
    players_alive = randint(1, 4)
    current_msg_text += str(players_alive)
    await callback.message.edit_text(current_msg_text)
    result += 6000 if players_alive < 4 else 3000
    await sleep(round(uniform(1.4, 2.8), 1))
    # STEP 2 END
    success = getrandbits(1)
    current_msg_text = f"<b>{await request.get_random_team_player(user_id)}</b> остался в клатче...⚠️" \
        if success else "<b>Раунд проигран💢</b>"
    await callback.message.edit_text(current_msg_text)
    if not success:
        result += randint(2000, 2700) // 10 * 10
        await sleep(1.5)
        return result
    await sleep(round(uniform(1.5, 2.5), 1))
    success = getrandbits(1)
    current_msg_text = "<b>Клатч выигран!✅</b>" if success else "<b>Клатч проигран!💢</b>"
    await callback.message.edit_text(current_msg_text)
    result += (randint(4000, 5000) // 10) * 10 if success else 2700
    await sleep(1.5)
    return result
