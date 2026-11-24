# Установка инструментов

## Git

Проверка: `git --version`
Результат: `git version 2.43.0`
Git уже был доступен в системе, поэтому отдельная установка не потребовалась. Список пакетов обновлялся командой `sudo apt update`

## Python и виртуальное окружение

Версия Python: `Python 3.12.3`
Версия pip в системе: `pip 24.0`
Проверка/установка инструментов выполнялась командами `sudo apt update` и `sudo apt install -y python3 python3-pip python3-venv`
Создано виртуальное окружение: `python3 -m venv .venv`
Окружение активировано: `source .venv/bin/activate`. Python расположен внутри `.venv`

## Зависимости проекта

Команда: `python -m pip install -r requirements.txt`
В `requirements.txt` указаны `gigachat==0.2.4` и `python-dotenv==1.0.1`
Зависимости отображаются в выводе `python -m pip list`
**Результат `python -m pip check`:** `No broken requirements found.`

## Ошибки и их причины

- Ошибки при установке зависимостей не зафиксировано.

## Что удалось исправить

- Подготовлено отдельное виртуальное окружение `.venv`.
- Зависимости проекта проверены; конфликтов зависимостей не обнаружено.