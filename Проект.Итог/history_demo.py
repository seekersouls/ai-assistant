from gigachat.models import ChatMessage
from prompts import SYSTEM_PROMPT

messages = [
    ChatMessage(
        role="system",
        content=SYSTEM_PROMPT
    )
]

messages.append(
    ChatMessage(
        role="user",
        content="Придумай персонажа для фантастического мультфильма."
    )
)

messages.append(
    ChatMessage(
        role="assistant",
        content="Персонаж — гиперэмоциональный, пафосный и крайне самоуверенный инопланетянин, который хочет захватить планету Земля и стать великим захватчиком."
    )
)

print("Количество сообщений:", len(messages))
print("Роли сообщений:")

for message in messages:
    print(message.role)

messages.append(
    ChatMessage(
        role="user",
        content="Расскажи подробнее о прошлом этого персонажа."
    )
)

messages.append(
    ChatMessage(
        role="assistant",
        content="В прошлом персонаж был учненным, а после получения титула захватчика стал изгнанником после проваленной миссии и работал постовым / работником кухни на пищевой планете Foodcourtia, после сбежал от туда, утверждая что уволил себя."
    )
)

print("Количество сообщений:", len(messages))

for message in messages:
    print(message.role)


messages = [
    ChatMessage(
        role="system",
        content=SYSTEM_PROMPT
    )
]

while True:
    user_text = input("Введите сообщение: ").strip()

    if user_text.lower() == "выход":
        print("Программа завершена.")
        break

    if not user_text:
        print("Введите текст.")
        continue

    messages.append(
        ChatMessage(
            role="user",
            content=user_text
        )
    )

    messages.append(
        ChatMessage(
            role="assistant",
            content="Тестовый ответ без API"
        )
    )

    print("Количество сообщений:", len(messages))

    for message in messages:
        print(message.role)