# MHP_Ariba
ariba_contacts - скрипт на основе ariba_repeat, для проверки конкретного таска

ariba_quests_to_admin - скрипт, задающий вопросы боту, которые он часто переадресует админу

ariba_regression_cases - скрипт, задающий определенный список вопросов в телеграмме, получив ответ - задает следующий

ariba_repeat - скрипт, задающий один вопрос определенное кол-во раз, чтобы проверять определенные кейсы на повторяемость

ariba_send_mail_subscribe - скрипт, открывающий страницу тендеров МХП , считает кол-во имеющихся тендеров, выбирает случайный из
них, запоминает категорию, логинится в почту и отсылает почтовому боту запрос на подписку на данную категорию

ariba_tg_subscribe - скрипт открывает страницу тендеров, выбирает случайный тендер, берет из него категорию и просит подписать
бота в телеграмме

ariba_send_some_mails - скрипт логинится в почту и отсылает почтовому боту несколько писем с определенным интервалом

ariba_send_mail - скрипт логинится в почту и отправялет письмо почтовому боту (для быстрой проверки, что почтовый бот отвечает)

ariba_subscride_all_API - подписать юзера на все категории через АПИ (для проверки адекватности рассылки)

ariba_subscride_all_TG - подписать юзера на все категории через телеграм (просит подписать на категории одну за одной)

ariba_excel_report - скрипт открывает эксель файл, берет из него вопросы по одному, задает их боту и ответы заносит в соседний столбец,
делает 3 таких прогона, затем сохраняет файл. Остается проверить ответы и получаем удобный отчет.

ariba_sheets_report - скрипт открывает таблицу гугл шитс в интернете, берет лист template с заготовленными вопросами, копирует его на новый лист, который называет текущей датой, задает данные вопросы боту в телеграм, и заполняет ответами, таблицу, делает три таких прогона, после каждого прогона делает АПИ-шный сброс переписки.
