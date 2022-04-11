from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import re


def es_correo_valido(correo):
            expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
            return re.match(expresion_regular, correo) is not None



def send_mail(email, name, subject, message):
    
    context = {'email': email, 'name': name,'subject': subject, 'message': message}

    template = get_template('web/mail.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Confirmation Email',
        'Automatically sent message',
        settings.EMAIL_HOST_USER,
        [email],
        cc=["smdlr47@hotmail.com"]
    )

    email.attach_alternative(content, "text/html")
    email.send()
