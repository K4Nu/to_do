from django.core.mail import send_mail
from django.conf import settings
from django.core.signing import Signer
from django.urls import reverse

def send_verification_email(user, domain):
    signer = Signer()
    token = signer.sign(user.pk)
    relative_verification_url = reverse('verify_email', kwargs={'token': token})
    verification_url = f"http://{domain}{relative_verification_url}"
    subject = 'Please verify your email'
    message = f'Hi {user.username}, please click on the link to verify your email: {verification_url}'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)
