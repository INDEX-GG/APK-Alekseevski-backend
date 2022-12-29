from django.core.mail import send_mail
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
                  f'Информация о кандидате: {data["description"]}\n' \
                  f'Прикрепленный документ: {data["docs"]}\n'
        from_email = EMAIL_HOST_USER
        recipient_list = EMAIL_HOST_USER

        attach = data["docs"]

        mail = EmailMessage(subject=subject, body=message, from_email=from_email, to=[recipient_list])
        mail.attach(attach.name, attach.read(), attach.content_type)
        result = mail.send()
        # result = send_mail(subject, message, from_email, recipient_list, )
        return result
