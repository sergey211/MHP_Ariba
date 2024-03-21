import asyncio
import random
import time

import pytest
from telethon.sync import TelegramClient, events

import config

# api id и api hash с какого аккаунта писать (брать на https://my.telegram.org/)
# serg:
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
             [""]
             ]

messages = [
    "какие сертификаты качества есть у мхп?",
    "какой у вас емейл?",
    "В якій категорії найбільше тендерів?",
    "На какой странице я могу найти информацию про тендеры?",
    "не открывается страница мхп",
    "другие страницы открываются, не открывается мхп, звоню по контактам которые ты дала, они недоступны, "
    "что случилось?",
    "будет ли компания работать в субботу",
    "Ошибка 502 на сайте, что случилось",
    "какие есть сертификаты заслуг компании?",
    "спроси какие награды есть у компании мхп",
    "Я регистрируюсь и появляется красная кнопка с надписью 'caravan' error 306, что делать?",
    "Я логинюсь как поставщик и вижу красную кнопку 'garnamin', error 507 что делать?",
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
            random_number = random.randint(8, 15)
            time.sleep(random_number)
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

# https://habr.com/ru/articles/667630/
