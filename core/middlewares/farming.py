from random import getrandbits, uniform, randint
from aiogram import types
from asyncio import sleep


async def by_game(user_id, callback: types.CallbackQuery, request):
    #  STEP 1 START
    await callback.message.edit_text("Коллим стратегию...", reply_markup=None)
    await sleep(round(uniform(1.1, 2.5), 1))
    await callback.message.edit_text("Заходим на точку...")
    await sleep(round(uniform(1.1, 2.5), 1))
    # TODO Сделать влияние навыков команды на результат
    success = getrandbits(1)  # random value True-False
    if success:
        current_msg_text = "Удачный entry-kill!🔥"
        await callback.message.edit_text(current_msg_text)
        result = (randint(8000, 10000) // 10) * 10
    else:
        current_msg_text = f"Ошибка от <b>{await request.get_random_team_player(user_id)}</b>💢"
        await callback.message.edit_text(current_msg_text)
        result = 4000

    await sleep(1.3)
    #  STEP 1 END

    #  STEP 2 START
    current_msg_text = f"Наша команда осталась {randint(2, 5)} <b>vs</b> {randint(1, 4)}"
    await callback.message.edit_text(current_msg_text)
    result += 6000 if int(current_msg_text[-1]) < 4 else 3000
    await sleep(round(uniform(1.4, 2.8), 1))
    #  STEP 2 END

    #  STEP 3 START
    success = getrandbits(1)
    if success:
        current_msg_text = f"<b>{await request.get_random_team_player(user_id)}</b> остался в клатче...⚠️"
        await callback.message.edit_text(current_msg_text)
        result += randint(4000, 5700) // 10 * 10
        await sleep(round(uniform(1.5, 2.5), 1))
    else:
        current_msg_text = "<b>Раунд проигран💢</b>"
        await callback.message.edit_text(current_msg_text)
        result += randint(2000, 2700) // 10 * 10
        await sleep(1.5)
        return result

    success = getrandbits(1)
    if success:
        current_msg_text = "<b>Клатч выигран!✅</b>"
        result += (randint(4000, 5200) // 10) * 10
    else:
        current_msg_text = "<b>Клатч проигран!💢</b>"
        result += 2200
    await callback.message.edit_text(current_msg_text)

    await sleep(1.5)
    return result


async def by_fake_match(user_id, callback: types.CallbackQuery, request, coefficient):
    #  STEP 1 START
    await callback.message.edit_text("Выходим на нужные контакты... 👥", reply_markup=None)
    await sleep(round(uniform(2, 2.5), 1))
    await callback.message.edit_text("Ждём ответа от игроков... ⏳")
    await sleep(round(uniform(1.1, 3), 1))
    success = getrandbits(4)
    if success != 0:
        current_msg_text = "Игроки согласны!"
        await callback.message.edit_text(current_msg_text)
        result = (randint(8000, 10000) // 10) * 10
        await sleep(round(uniform(1.1, 3), 1))
    else:
        current_msg_text = f"<b>Кто-то нас сдал! 📛</b>"
        await callback.message.edit_text(current_msg_text)
        await sleep(3)
        result = -10000
    # TODO Сделать выбор коэффициента ставки-> выше - больше денег, но больше риск [input == 1/2/3 (1.2/1.5/2)](в конце)
    return result
