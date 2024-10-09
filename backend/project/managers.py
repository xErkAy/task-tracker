from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, username=None, password=None, full_name=None):
        if username is None:
            raise TypeError('User must have a username')
        if password is None:
            raise TypeError('User must have a password')

        user = self.model(username=username, full_name=full_name)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, password):
        if password is None:
            raise TypeError('Superuser must have a password')

        user = self.create_user(username, password)
        user.is_admin = True
        user.is_staff = True
        user.save()

        return user
