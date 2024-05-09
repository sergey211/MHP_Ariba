import asyncio
import random
import time

import pytest
from telethon.sync import TelegramClient, events

import config

api_id = config.api_id
api_hash = config.api_hash

result = False

responses = [[""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""],
             [""]
             ]

messages = [
    " подпиши меня на Добавки і спеції харчові ",
    " подпиши меня на ІТ обладнання та сервіс",
    " подпиши меня на Компоненти для виробництва комбікорму, корма для тварин",
    " подпиши меня на  Таропакувальні матеріали",
    " подпиши меня на  Адміністративно-господарчі товари та послуги",
    " подпиши меня на  Будівництво та ремонт",
    " подпиши меня на  Ветпрепарати",
    " подпиши меня на  Дезінфікуючі та миючі засоби промислові",
    " подпиши меня на  Енергоносії",
    " подпиши меня на  Засоби індивідуального захисту, спецодяг, взуття",
    " подпиши меня на  Інженерне та електротехнічне обладнання",
    " подпиши меня на  Інструменти та комплектуючі",
    " подпиши меня на  Лабораторні та медичні матеріали",
    " подпиши меня на  Насіння, добрива, засоби захисту рослин",
    " подпиши меня на  Невиробничі послуги",
    " подпиши меня на  Продукти харчування та напої",
    " подпиши меня на  Промислове обладнання, запчастини та сервіс",
    " подпиши меня на  Сільськогосподарські тварини",
    " подпиши меня на  Транспорт, сільгосп. техніка, запчастини та сервіс",
    " подпиши меня на  Хімічні речовини",
    " подпиши меня на  Сільськогосподарські послуги"

]


@pytest.mark.asyncio
async def connect():
    global api_id, api_hash, result
    result = False
    client = TelegramClient('ariba.session', api_id, api_hash)  # подключение к тг аккаунту
    await client.start()
    return client


@pytest.mark.asyncio
async def main():
    client = await connect()
    user = config.ariba_bot

    for index, message in enumerate(messages):
        try:
            await asyncio.wait_for(send_message(user, client, index), timeout=300)
            client = await connect()
            random_number = random.randint(10, 85)
            time.sleep(5)
        except asyncio.TimeoutError:
            print("No message received after 5 minutes.")
        except Exception as e:
            print(f"An error occurred: {e}")

    await client.disconnect()


@pytest.mark.asyncio
async def send_message(user, client, index):
    global result
    await client.send_message(user, messages[index])

    @client.on(events.NewMessage(chats=user))
    async def handler(event):
        await handle_response(event, responses[index], client)

    await client.run_until_disconnected()
    assert result is True


@pytest.mark.asyncio
async def handle_response(event, valid_responses, client):
    global result
    message_text = event.message.text
    if any(response in message_text for response in valid_responses):
        result = True
    else:
        print(f"Expected: {valid_responses}, got: {message_text}")
        result = False
    await client.disconnect()
    return result


asyncio.run(main())
