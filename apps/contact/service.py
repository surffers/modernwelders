from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Вы подписались на рассыылку',
        'Пароль и логин от вашего кабинета',
        'aleksandrkarpukofficial@gmail.com',
        [user_email],
        fail_silently=False,
    )