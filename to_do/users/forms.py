from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

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

class UpdateUserForm(forms.ModelForm):
    username=forms.CharField(max_length=100,required=True)
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=["username","email"]

class UpdateProfileForm(forms.ModelForm):
    image=forms.ImageField()

    class Meta:
        model=Profile
        fields=["image"]