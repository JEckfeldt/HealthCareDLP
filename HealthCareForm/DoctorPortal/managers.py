from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class PatientManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, username, password, phone, ssn, fname, lname, sex, age, weight, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        user = self.model(username=username, password=password, phone=phone, ssn=ssn,
                           fname=fname, lname=lname, sex=sex, age=age, weight=weight, symptoms="", allergies="", **extra_fields)
        #email = self.normalize_email(email)
        user.set_password(password)
        user.save()
        return user
    
class DoctorManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, username, password, phone, ssn, fname, lname, sex, age, weight, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        user = self.model(username=username, password=password, phone=phone, ssn=ssn,
                           fname=fname, lname=lname, sex=sex, age=age, weight=weight, symptoms="", allergies="", **extra_fields)
        #email = self.normalize_email(email)
        user.set_password(password)
        user.save()
        return user