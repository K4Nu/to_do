from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.signing import Signer
from django.core.mail import send_mail
from django.conf import settings

def send_verification_email(user):
    signer = Signer()
    token = signer.sign(user.pk)
    verification_url = f" http://127.0.0.1:8000/verify_email/{token}/"
    # Send email using Django's send_mail with the verification_url
    subject = 'Please verify your email'
    message = f'Hi {user.username}, please click on the link to verify your email: {verification_url}'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    send_mail(subject,message,from_email,recipient_list)