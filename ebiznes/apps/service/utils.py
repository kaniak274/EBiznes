from django.conf import settings
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_email(subject, html_template, to, msg_ctx = None):
    message = render_to_string(html_template, msg_ctx)

    mail.send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        to,
        html_message=strip_tags(message)
    )
