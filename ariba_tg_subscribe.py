import asyncio
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from telethon import TelegramClient

import config
import ariba_reset_Serzhioo

api_id = config.api_id
api_hash = config.api_hash

client = TelegramClient('ariba.session', api_id, api_hash)
client.start()


async def send_message_and_wait_for_reply_new(message):
    async with client:
        target_username = config.ariba_bot
        async with client:
            try:

                print("Аутентификация пользователя...")
                await client.start()

                # Получение информации о пользователе по его нику
                print("Получение информации о пользователе...")
                entity = await client.get_entity(target_username)

                # Отправка сообщения и получение его идентификатора
                print("Отправка сообщения...")
                sent_message = await client.send_message(entity, message)

                # Получаем последние сообщения в диалоге
                print("Получение последних сообщений...")
                last_messages = await client.get_messages(entity)
                last_message_id = last_messages[-1].id if last_messages else 0

                print("Ожидание  ответа...")
                for i in range(180):  # ожидание до 3 минут (180 секунд)
                    async for message in client.iter_messages(entity):
                        if message.id > last_message_id:
                            print('Получен  ответ:', message.text, i)
                            return
                            # break  # Прерываем цикл после получения первого ответа
                            # raise Exception('Stop this thing')
                    else:
                        print("Ожидание  ответа...", i)
                        await asyncio.sleep(1)  # ждем 1 секунду перед следующей попыткой

                print("Истекло время ожидания. Не получен ответ.")
                print("Отправка сообщения... ")
                sent_message = await client.send_message(entity, 'Истекло время ожидания. Не получен ответ.')

            except Exception as e:
                print(f"Произошла ошибка: {e}")


async def connect():
    global api_id, api_hash, result
    result = False
    client = TelegramClient('ariba.session', api_id, api_hash)  # подключение к тг аккаунту
    await client.start()
    return client


class JavascriptExecutor:
    pass


def find_tenders():
    chrome_options = Options()
    # chrome_options.add_experimental_option('detach', True)
    chrome_options.add_argument('headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(config.base_url+"/tendery")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn1-bord ')]").click()
    btns = driver.find_elements(By.XPATH, "//button[text()='75']")
    driver.execute_script("arguments[0].click();", btns[0])
    els = driver.find_elements(By.XPATH, "//div[contains(@class,'Tenders_tenderFlexWrapper')]")
    print("total = ", len(els))
    rand = random.randint(0, len(els) - 1)
    print(rand)
    last_tend = els[rand].text
    tems = last_tend.split("\n")
    categ = tems[4]
    print(categ)
    time.sleep(5)
    client.loop.run_until_complete(send_message_and_wait_for_reply_new("подпиши на " + categ))


ariba_reset_Serzhioo.clear_categories()
find_tenders()
