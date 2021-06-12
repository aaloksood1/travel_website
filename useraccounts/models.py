from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.

class UserOperations:

    @staticmethod
    def validate_data_and_return_errors(username, email, password,confirm_password, \
                                        is_superuser = False, is_active = True, \
                                        is_staff = False):
        """ Perform various checks on the user data
            These are application level checks
            Database checks must be enforced at Data base level
            For example: Data base query with username to validate whether usename is unique
            may lead to race condition if performed at application level
        """
        errors = []

        if not username:
            errors.append("Please enter a Username")

        if not password:
            errors.append("Please enter a Password")

        if password != confirm_password:
            errors.append("Passwords do not match")

        if User.objects.filter(username = username).exists():
            errors.append("User with username {} already exists".format(username))

        if User.objects.filter(email = email).exists():
            errors.append("User with email id {} already exists".format(email))

        return errors

    @classmethod
    def create_a_user(cls, username, email, first_name, last_name, password, confirm_password):

        user = None
        #validate user data
        errors = cls.validate_data_and_return_errors(username = username,
                                                     email =email,
                                                     password = password,
                                                     confirm_password= confirm_password)

        if not errors:
            try:
                user = User.objects.create_user(username=username,
                                                email=email,
                                                first_name=first_name,
                                                last_name=last_name,
                                                password=password)
                user.save()
            except Exception as e:
                print("Exception while adding user {}: {}".format(username,  e.__dict__))
                errors.append("Unexpected error: Please contact Administrator")
                #print(errors)


        return (user,errors)

    @staticmethod
    def authenticate_user(username, password):
        user = auth.authenticate(username = username,
                                 password = password)
        return user