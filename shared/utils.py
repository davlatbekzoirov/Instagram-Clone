import re
import threading
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from rest_framework.exceptions import ValidationError

email_regex = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b")
phone_regex = re.compile(r"(\+[0-9]+\s*)?(\([0-9]+\))?[\s0-9\-]+[0-9]+")

def check_email_or_phone(email_or_phone):
    if re.fullmatch(email_regex, email_or_phone):
        return "email"
    elif re.fullmatch(phone_regex, email_or_phone):
        return "phone"
    else:
        raise ValidationError({
            "success": False,
            "message": "Email yoki telefon raqamingiz noto'g'ri"
        })

class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()

class Email:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['subject'],
            body=data['body'],
            to=[data['to_email']],
        )
        if data.get('content_type') == 'html':
            email.content_subtype = 'html'
        EmailThread(email).start()

def send_email(email, code):
    html_content = render_to_string(
        'email/authetication/activate_account.html',
        {'code': code}
    )
