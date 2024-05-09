import asyncio
import random
import time
import pytest
import config
from telethon.sync import TelegramClient, events

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
    "Привет",
    "С чем ты можешь помочь?",
    "Расскажи пожалуйста как зарегистрироваться в системе",
    "Могу ли я зарегистрироваться как поставщик?",
    "Я регистрируюсь и появляется красная кнопка с надписью 'caravan', что делать?",
    "Расскажи как проходит процедура закупок",
    "Какие требования для пользователя для участия в закупках?",
    "Я логинюсь как поставщик и вижу красную кнопку 'garnamin', что делать?",
    "Подпиши меня на продукты питания и напитки",
    "На что я подписан?",
    "Посоветуй на что мне подписаться, я занимаюсь техникой для сельского хозяйства и запчастями",
    "Да, спасибо",
    "Расскажи, какой телефонный код у Австрии",
    "Напомни, какая столица Франции?",
    "Кто тебя создал?",
    "Ты кто?",
    "Пидкажи буд ласка як зареструватися в Ариба нетварк",
    "Do you speak english?",
    "Could you answer in english please?",
    "Не работает сайт , дай пожалуйста контакт службы поддержки",
    "Этот контакт недоступен, есть еще какой-нибудь контакт? ",
    "Этот контакт тоже недоступен, есть еще? ",
    "Ну пока",
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
