from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

def user_directory_path(instance, filename):
    # Obtain the file extension and construct the filename using the user's username.
    # The filename will be: username.jpg
    ext = filename.split('.')[-1]
    # If you want to handle cases where the username changes, use instance.user.username
    filename = f"{slugify(instance.user.username)}.{ext}"
    # Return the whole path to the file
    return f'profile_pics/{filename}'

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default="default.jpg",upload_to=user_directory_path)
    email_verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username}'

