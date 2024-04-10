from django.db.models.signals import post_save,pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile
from django.core.files.storage import default_storage

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Welcome to To-Do App',
            f'Welcome {instance.username} to our app, we hope you will enjoy it',
            'k4nu420@gmail.com',
            [instance.email],
        )

@receiver(pre_save,sender=Profile)
def delete_old_image(sender,instance,**kwargs):
    if instance._state.adding and not instance.pk:
        return
    try:
        old_instance=Profile.objects.get(pk=instance.pk)
    except Profile.DoesNotExists:
        return

    if old_instance.image:
        if default_storage.exists(old_instance.image.name):
            old_instance.image.delete(save=False)