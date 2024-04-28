import os.path
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from .utils import nfsw_filter

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    image=forms.FileField(required=False)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email=self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already used")
        return email

    def clean_username(self):
        username = self.cleaned_data.get("username")
        # Check if the username is not None or an empty string
        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        return username

    def clean(self):
        cleaned_data=super().clean()
        password1=cleaned_data.get("password1")
        username=cleaned_data.get("username")

        if password1 and username and username.lower() in password1.lower():
            self.add_error("password1", "Password cannot contain the username!")

        return cleaned_data

    def clean_image(self):
        image=self.cleaned_data.get("image")
        if image:
            extension=os.path.splitext(image.name)[1].lower()
            valid_extensions = ['.png', '.jpg', '.jpeg']
            if image.size>settings.MAX_UPLOAD_SIZE:
                raise forms.ValidationError(f"File size is too big, maximum allowed size is {round(settings.MAX_UPLOAD_SIZE / (1024 * 1024))} MB")
            if extension not in valid_extensions:
                raise forms.ValidationError("Unsupported file extension. Allowed extensions are: PNG, JPG, JPEG.")
        return image

class UpdateUserForm(forms.ModelForm):
    username=forms.CharField(max_length=100,required=True)
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=["username","email"]

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=["image"]
        widgets={"image":forms.FileInput()}

    def clean_image(self):
        image=self.cleaned_data.get("image")
        if image:
            extension=os.path.splitext(image.name)[1].lower()
            valid_extensions = ['.png', '.jpg', '.jpeg']
            if image.size>settings.MAX_UPLOAD_SIZE:
                raise forms.ValidationError(f"File size is too big, maximum allowed size is {round(settings.MAX_UPLOAD_SIZE / (1024 * 1024))} MB")
            if extension not in valid_extensions:
                raise forms.ValidationError("Unsupported file extension. Allowed extensions are: PNG, JPG, JPEG.")
        return image

class ResendVerificationEmailForm(forms.Form):
    email=forms.EmailField(label="Your email address")

class CustomAuthenticationForm(AuthenticationForm):
    pass

class ImageGenerationForm(forms.Form):
    input=forms.CharField(label="input",max_length=1500)

    def clean_input(self):
        input = self.cleaned_data.get("input")
        output = nfsw_filter({'inputs': input})
        # Extract scores for the label 'safe'
        safe_scores = [item['score'] for item in output[0] if item['label'] == 'safe']
        if not safe_scores or safe_scores[0] < 0.7:
            raise forms.ValidationError("This content is not allowed")
        return input
