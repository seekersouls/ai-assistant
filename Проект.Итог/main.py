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

messages = [
    ChatMessage(
        role="system",
        content=SYSTEM_PROMPT
    )
]

max_pairs = 2
k = 2 * max_pairs
system_message = messages[0]

with open("chat_history.txt", "a", encoding="utf-8") as file:
    file.write("Новый запуск\n\n")

print("Доступные команды:")
print("выход — завершить программу")
print("очистить — очистить историю")
print("история — показать историю")

with GigaChat(
    credentials=key,
    scope=scope,
    model="GigaChat-2",
    ca_bundle_file="certs/russian_trusted_root_ca_pem.crt",
    timeout=60,
) as client:

    while True:
        user_text = input("Введите сообщение: ").strip()

        command = user_text.lower()

        if command == "выход":
            print("Программа завершена.")
            break

        if command == "очистить":
            system_message = messages[0]
            messages = [system_message]

            with open("chat_history.txt", "a", encoding="utf-8") as file:
                file.write("История текущего диалога очищена\n\n")

            print("История диалога очищена.")
            continue

        if command == "история":
            print("Количество сообщений:", len(messages))

            for message in messages:
                print(message.role)

            continue

        if not user_text:
            print("Введите текст.")
            continue

        messages.append(
            ChatMessage(
                role="user",
                content=user_text
            )
        )

        request = ChatCompletionRequest(
            model="GigaChat-2",
            messages=messages,
            model_options=ChatModelOptions(
                temperature=0.2,
                max_tokens=400,
            )
        )

        response = client.chat.create(request)

        answer = response.messages[0].content[0].text

        print("Ответ помощника:")
        print(answer)

        messages.append(
            ChatMessage(
                role="assistant",
                content=answer
            )
        )

        with open("chat_history.txt", "a", encoding="utf-8") as file:
            file.write("Пользователь: " + user_text + "\n")
            file.write("ИИ: " + answer + "\n")
            file.write("\n")

        if len(messages) > 1 + 2 * max_pairs:
            messages = [system_message] + messages[-k:]

        print("Количество сообщений:", len(messages))