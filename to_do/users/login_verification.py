from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from .models import Profile

class EmailVerifiedBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(User.USERNAME_FIELD)
        try:
            user = User._default_manager.get_by_natural_key(username)
            if user.check_password(password):
                # Allow superusers to log in regardless of email verification
                if user.is_superuser:
                    return user

                # Check if the user has a profile and if it's verified
                try:
                    profile = Profile.objects.get(user=user)
                    # Only return the user if the email is verified
                    if profile.email_verified:
                        return user
                    else:
                        # Optionally, you can add a message to inform the user
                        if request:
                            from django.contrib import messages
                            messages.error(request, "Your email address is not verified.")
                        return None
                except Profile.DoesNotExist:
                    # If there is no profile, return None or handle it based on your requirements
                    return None
        except User.DoesNotExist:
            # Run the default password hasher once to reduce timing difference between existing and non-existing users
            User().set_password(password)
        return None
