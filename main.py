import os

from weather_sdk import get_new_event, SMSServer
from dotenv import load_dotenv


load_dotenv(dotenv_path='Secrets/.env')
token = os.getenv('FORECAST_TOKEN')
town_title = 'Курск'

sms_token = os.getenv('SMS_TOKEN')
server = SMSServer(token)

new_event = get_new_event(token, town_title)
event_date = new_event.get_date()
event_time = new_event.get_time()
event_area = new_event.get_area()
phenomenon_description = new_event.get_phenomenon()

sms_template = f'''{town_title}: {event_time} {event_date} {event_area} ожидается {phenomenon_description}. Будьте внимательны и осторожны.'''

sms_message = sms_template.format(
    phenomenon_description,
    town_title,
    event_time,
    event_date,
    event_area,
)

server.send(sms_message)


print(sms_template)
# Гипотеза 1: В переменной нет прогноза погоды для Курска
# Способ проверки: Выведу переменную new_event
# Код для проверки: print(new_event)
# Установленный факт: Принт выводит: 'Регион:  Погода: '
# Вывод: В переменной нет прогноза

# Гипотеза 2.1: town_title на самом деле пуста
# Способ проверки: Вывести переменную town_title
# Код для проверки: print(town_title)
# Установленный факт: Принт выводит 'Курск'
# Вывод: На самом деле town_title не пуст

# Гипотеза 2.2: В town_title не название города
# Способ проверки: Вывести переменную town_title
# Код для проверки: print(town_title)
# Установленный факт: Принт выводит 'Курск'
# Вывод: В town_title есть название города

# Гипотеза 3: Переменная token на самом деле пуста
# Способ проверки: Вывести переменную token
# Код для проверки: print(token)
# Установленный факт: Принт выводит 'None'
# Вывод: Все верно, переменная пуста

# Гипотеза 4.1: Может, `token` всё ещё пуст?
# Способ проверки: Вывести переменную token
# Код для проверки: print(token)
# Установленный факт: Принт выводит 'aGVsbG8gY3J5cHRvIGVudHVzaWFzdCA7KQ=='
# Вывод: Принт не пуст

# Гипотеза 4.2: Может, в токене не то значение, не `85b98d96709fd49a69ba8165676e4592`?
# Способ проверки: Вывести переменную token
# Код для проверки: print(token)
# Установленный факт: Принт выводит 'aGVsbG8gY3J5cHRvIGVudHVzaWFzdCA7KQ==
# Вывод: Токен выводит не `85b98d96709fd49a69ba8165676e4592`

# Гипотеза 4.3: Может, значение `85b98d96709fd49a69ba8165676e4592` успевает измениться до строчки `new_event = ...`?
# Способ проверки: Вывести переменную token
# Код для проверки: print(token)
# Установленный факт: Принт выводит 'aGVsbG8gY3J5cHRvIGVudHVzaWFzdCA7KQ==
# Вывод: Токен изменяется до new_event

# Гипотеза 5.1: Переменная `event_time` пуста/в ней не время
# Способ проверки: Вывести переменную event_time
# Код для проверки: print(event_time)
# Установленный факт: Принт выводит 'утром'
# Вывод: В переменной правильное значение

# Гипотеза 5.2: Переменная `event_date` пуста/в ней не дата
# Способ проверки: Вывести переменную event_date
# Код для проверки: print(event_date)
# Установленный факт: Принт выводит '3 ноября'
# Вывод: В переменной правильное значение

# Гипотеза 5.3: Переменная `event_area` пуста/в ней не место
# Способ проверки: Вывести переменную event_area
# Код для проверки: print(event_area)
# Установленный факт: Принт выводит 'г. Вязьма'
# Вывод: В переменной правильное значение

# Гипотеза 5.4: Переменная `phenomenon_description` пуста/в ней не описание погодного явления
# Способ проверки: Вывести переменную phenomenon_description
# Код для проверки: print(phenomenon_description)
# Установленный факт: Принт выводит 'ветер порывами до 23 м/с'
# Вывод: В переменной правильное значение

# Гипотеза 6: Возможно, в шаблоне используются какие-то переменные, которые не передаются в .format()?
# Способ проверки: Выделю названия переменных town_title, event_time, event_date, event_area, phenomenon_description
# Код для проверки: Выделить слово
# Установленный факт: Ошибок не найдено 
# Вывод: Гипотеза ошибочна

# Гипотеза 7: В переменной sms_template допущена ошибка при использовании .format()
# Способ проверки: добавить f перед кавычками в переменной sms_template
# Код для проверки: print(sms_template)
# Установленный факт: Ошибка исчезла
# Вывод: гипотеза оказалась верна