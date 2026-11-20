import os
from dotenv import load_dotenv
from gigachat import GigaChat
from prompts import SYSTEM_PROMPT
from gigachat.models import (
    ChatCompletionRequest, ChatMessage, ChatModelOptions,
) 

load_dotenv()
key = os.getenv("GIGACHAT_CREDENTIALS")
scope = os.getenv("GIGACHAT_SCOPE")

character_data = input("Опиши персонажа или идею для нового персонажа: ").strip()
restriction = input("Какие ограничения нужно учитывать? ").strip()
desired_result = input("Что ты хочешь получить от ИИ-помощника? ").strip()
genre = input("В каком жанре создать персонажа? ").strip()

print("\nВыбери формат ответа:")
print("1 — краткий ответ")
print("2 — пошаговый ответ")

answer_format = input("Введи 1 или 2: ").strip()

if answer_format == "1":
    format_instruction = "Дай краткий ответ, выдели только основные мысли."
elif answer_format == "2":
    format_instruction = "Дай подробный пошаговый ответ с объяснениями и примерами."
else:
    print("Ошибка: нужно выбрать 1 или 2.")
    exit()


if not character_data:
    print("Ошибка: необходимо указать данные персонажа.")
    exit()

if not desired_result:
    print("Ошибка: необходимо указать желаемый результат.")
    exit()

if not restriction:
    restriction = "не указано"


user_prompt = f"""
Задача: создание или анализ художественного персонажа.

Исходные данные:
{character_data}

Жанр:
{genre}

Ограничения:
{restriction}

Желаемый результат:
{desired_result}

Формат ответа:
{format_instruction}

Выполни задачу, учитывая все предоставленные данные.
"""


print("Сформированный запрос:")
print(user_prompt)


request = ChatCompletionRequest(
        model="GigaChat-2",
        messages=[
            ChatMessage(
                role="system",
                content=SYSTEM_PROMPT,
            ),
            ChatMessage(
                role="user",
                content=user_prompt,
            )
        ],
        model_options=ChatModelOptions(
            temperature=0.2,
            max_tokens=400,
        )
)

print("Отправляем запрос...")


with GigaChat(
    credentials=key,
    scope=scope,
    model="GigaChat-2",
    ca_bundle_file="certs/russian_trusted_root_ca_pem.crt",
    timeout=60,
) as client:
    responce = client.chat.create(request)

answer = responce.messages[0].content[0].text

with open("last_prompt.txt", "w", encoding="utf-8") as file:
    file.write(user_prompt)

with open("last_answer.txt", "w", encoding="utf-8") as file:
    file.write(answer)

print("Ответ:")
print(answer)

print("\nЗапрос и ответ сохранены в файлы.")