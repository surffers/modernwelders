from django.core.mail import send_mail
from django.template.loader import render_to_string


msg_html = render_to_string('contact/email.html')
def send(user_email):
    send_mail(
        'Вы подписались на рассыылку',
        'Пароль и логин от вашего кабинета',
        'Surffers',
        [user_email],
        fail_silently=False,
        html_message=msg_html,
    ),

