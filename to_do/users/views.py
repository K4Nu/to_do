from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm,UpdateUserForm,UpdateProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

def index(request):
    return render(request,"users/index.html")

def register(request):
    if request.method=="POST":
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            profile=Profile(user=user)
            profile.image=request.FILES.get("profile_picture")
            profile.save()
            return redirect("login")
    else:
        form=CustomUserCreationForm()
    return render(request,"users/register.html",{"form":form})

@login_required
def profile(request):
    return render(request,"users/profile.html")

@login_required
def profile_update(request):
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('index')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, "users/update_profile.html", {"user_form": user_form, "profile_form": profile_form})


