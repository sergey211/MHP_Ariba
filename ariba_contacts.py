import asyncio
import time
import requests
import pytest
from requests.structures import CaseInsensitiveDict
from telethon.sync import TelegramClient, events
import config

api_id = config.api_id
api_hash = config.api_hash


def make_reset():
    url = "https://ariba.gart.technology/tenders/reset_user_history/?username=Serzhioo&user_type=TELEGRAM"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    data = '{"user_type": "TELEGRAM", "username": "Serzhioo"}'
    resp = requests.post(url, headers=headers, data=data)
    print()
    print(resp.text)
    print(resp.status_code)


result = False

responses = [
    ["0669934604", "s.lesko@mhp.com.ua"],
    ["0503354807", "d.kolov@mhp.com.ua"],
    [" "],
]

messages = ["дай пожалуйста контакты кого-нибудь из мхп, не работает сайт, хочу позвонить",
            " этот контакт недоступен, дай чей-нибудь еще ",
            " этот тоже недоступен, есть еще кто-нибудь из службы поддержки? "
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
    for i in range(1, 4):
        print(i)
        client = await connect()
        user = config.ariba_bot
        await client.send_message(user, '/reset')
        # make_reset()
        time.sleep(7)

        for index, message in enumerate(messages):
            try:
                await asyncio.wait_for(send_message(user, client, index), timeout=300)
                client = await connect()
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
    assert result == True


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

# make_reset()
asyncio.run(main())
