from django.core.mail import EmailMessage

from config.settings import EMAIL_HOST_USER


class Util:
    @staticmethod
    def send_mail(data):
        for i in data:
            if data[i] == '':
                data[i] = 'Не указано'
            else:
                continue

        subject = 'Вакансии'
        message = f'ФИО: {data["fullname"]}\n' \
                  f'Название вакансии: {data["vacancy"]}\n' \
                  f'Email: {data["email"]}\n' \
                  f'Телефон: {data["phone"]}\n' \
                  f'Информация о кандидате: {data["description"]}\n'
        from_email = EMAIL_HOST_USER
        recipient_list = EMAIL_HOST_USER

        if "docs" in data:
            attach = data["docs"]
            mail = EmailMessage(subject=subject, body=message, from_email=from_email, to=[recipient_list])
            mail.attach(attach.name, attach.read(), attach.content_type)
            result = mail.send()
            return result
        else:
            mail = EmailMessage(subject=subject, body=message, from_email=from_email, to=[recipient_list])
            result = mail.send()
            return result
