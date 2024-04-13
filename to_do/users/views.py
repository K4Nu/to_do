from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm,UpdateUserForm,UpdateProfileForm,ResendVerificationEmailForm,CustomAuthenticationForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.signing import Signer,BadSignature
from django.contrib.auth.models import User
from .utils import send_verification_email
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.contrib.auth import authenticate, login
import os

def index(request):
    return render(request,"users/index.html")

def register(request):
    if request.method=="POST":
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            profile=Profile(user=user)
            profile_image=request.FILES.get("profile_picture")
            max_size=1*1024*1024
            if profile_image.size>max_size:
                messages.error(request,"File is too big")
                return
            if not profile_image:
                profile_image="default.jpg"
            profile.image=profile_image
            profile.save()
            send_verification_email(user)
            return render(request,'users/verification.html')
    else:
        form=CustomUserCreationForm()
    return render(request,"users/register.html",{"form":form})

@login_required
def profile(request):
    return render(request,"users/profile.html")

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import UpdateUserForm, UpdateProfileForm

@login_required
def profile_update(request):
    user = request.user
    profile = user.profile

    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            saved_profile=profile_form.save(commit=False)
            existing_image = request.user.profile.image
            if saved_profile.image:
                print(os.stat(saved_profile.image))
            if not saved_profile.image:
                saved_profile.image=existing_image
            saved_profile.save()
            return redirect('profile')
    else:
        user_form = UpdateUserForm(instance=user)
        profile_form = UpdateProfileForm(instance=profile)

    return render(request, "users/update_profile.html", {"user_form": user_form, "profile_form": profile_form})


def verify_email(request,token):
    signer=Signer()
    try:
        user_id=signer.unsign(token)
        user=User.objects.get(pk=user_id)
        profile=Profile.objects.get(user=user)
        profile.email_verified=True
        profile.save()
        return redirect('login')
    except (BadSignature, User.DoesNotExists,Profile.DoesNotExists):
        return render(request,"invalid_token.html")

def resend_verification_email(request):
    if request.method == "POST":
        form = ResendVerificationEmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                if not user.profile.email_verified:
                    send_verification_email(user)
                    messages.success(request, "A new verification email has been sent to your email address.")
                else:
                    messages.info(request, "Your email is already verified.")
                return render(request,"users/verification.html")
            except User.DoesNotExist:
                messages.error(request, "No user found with this email address.")
    else:
        form = ResendVerificationEmailForm()

    # This return will handle both GET requests and POST requests where the form is not valid or an exception occurs
    return render(request, 'users/resend_verification_email.html', {'form': form})

def custom_login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.profile.email_verified:
                    login(request, user)
                    return redirect('index')  # Redirect to a success page.
                else:
                    messages.error(request, "Your email address is not verified.")
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})