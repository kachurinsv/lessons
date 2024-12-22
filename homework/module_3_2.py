def send_email(message='Это сообщение для проверки связи', recipient='university.help@gmail.com',
               sender="university.help@gmail.com"):
    if ('@' not in recipient or not recipient.endswith(('.com', '.ru', '.net', '.by'))
        or '@' not in sender or not sender.endswith(('.com', '.ru', '.net', '.by'))):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    elif sender != "university.help@gmail.com":
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

    send_email('message', 'vasyok1337@gmail.com')
    send_email('message', 'urban.fan@mail.ru', 'urban.info@gmail.com')
    send_email('message', 'urban.student@mail.ru', 'urban.teacher@mail.uk')
    send_email('message', 'university.help@gmail.com', 'university.help@gmail.com')
