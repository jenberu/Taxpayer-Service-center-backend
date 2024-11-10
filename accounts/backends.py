from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Check if the username is an email or a username
        User = get_user_model()
        try:
            # Try to get the user by email if the username looks like an email
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            try:
                # Fallback to getting the user by username if not found by email
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None

        # Check if the password is correct for the found user
        if user.check_password(password):
            return user
        return None
