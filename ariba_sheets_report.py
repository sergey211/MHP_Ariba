import asyncio
import datetime
import pygsheets
from telethon import TelegramClient

import config
from ariba_reset_Serzhioo import reset_history

api_id = config.api_id
api_hash = config.api_hash

client = TelegramClient('ariba.session', api_id, api_hash)
client.start()
target_username = config.ariba_bot

# Получаем текущее время
current_time = datetime.datetime.now()

# Добавляем один час
new_time = current_time + datetime.timedelta(hours=1)

# Форматируем новое время
formatted_time = new_time.strftime("%Y-%m-%d %H:%M:%S")

# Форматируем новое время
formatted_date = new_time.strftime("%Y-%m-%d")

print("Текущее время:", current_time)
print("Время по Киеву:", formatted_time)


async def send_message_and_wait_for_reply_new(message):
    async with client:
        async with client:
            try:

                # print("Аутентификация пользователя...")
                await client.start()

                # Получение информации о пользователе по его нику
                # print("Получение информации о пользователе...")
                entity = await client.get_entity(target_username)

                # Отправка сообщения и получение его идентификатора
                # print("Отправка сообщения...")
                sent_message = await client.send_message(entity, message)

                # Получаем последние сообщения в диалоге
                # print("Получение последних сообщений...")
                last_messages = await client.get_messages(entity)
                last_message_id = last_messages[-1].id if last_messages else 0

                # print("Ожидание  ответа...")
                for i in range(20):  # ожидание около 7 минут (значение = 20) значение 40=14 минут
                    async for message in client.iter_messages(entity):
                        if message.id > last_message_id:
                            print('Получен ответ:', message.text, i)
                            return message.text
                            # break  # Прерываем цикл после получения первого ответа
                            # raise Exception('Stop this thing')
                    else:
                        print("Ожидание ответа...", i)
                        await asyncio.sleep(1)  # ждем 1 секунду перед следующей попыткой

                print("Истекло время ожидания. Не получен ответ.")
                print("Отправка сообщения... ")
                return "timeout"
                # sent_message = await client.send_message(entity, 'Истекло время ожидания. Не получен ответ.')

            except Exception as e:
                print(f"Произошла ошибка: {e}")


CREDENTIALS_FILE = 'D:\\Projects\\MHP-Ariba\\credentials.json'  # Имя файла с закрытым ключом
gc = pygsheets.authorize(service_account_file='D:\\Projects\\MHP-Ariba\\credentials.json')

# Идентификатор существующей таблицы
spreadsheet_id = config.spreadsheet_id
sh = gc.open_by_key(spreadsheet_id)
worksheet1 = gc.open_by_key(spreadsheet_id).worksheet_by_title("template")
try:
    worksheet = sh.add_worksheet(formatted_date, src_worksheet=worksheet1)
except Exception as e:
    worksheet = gc.open_by_key(spreadsheet_id).worksheet_by_title(formatted_date)

# Заполнение таблицы данными
print('https://docs.google.com/spreadsheets/d/' + spreadsheet_id)


column_index = 3  # Индекс столбца (начиная с 1)
column_values = worksheet.get_col(column_index)
limited_values = column_values[1:27]

# Вывод данных в консоль

for j in range(4, 7):  # 4 - first, 6 - last
    reset_history()
    i = 2
    for value in limited_values:
        print(value)
        start_time = datetime.datetime.now()
        answer = client.loop.run_until_complete(send_message_and_wait_for_reply_new(value))
        operation1_time = datetime.datetime.now()
        new_time = operation1_time + datetime.timedelta(hours=1)
        formatted_time = new_time.strftime("%H:%M:%S")
        elapsed_time = int((operation1_time - start_time).total_seconds())
        answer2 = answer + " время ответа по Киеву: " + str(formatted_time) + " , ответ занял " + str(
            elapsed_time) + " сек"
        worksheet.update_value((i, j), answer2)
        i += 1


print('Таблица успешно обновлена.')
