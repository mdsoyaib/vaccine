from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.


class Staff(models.Model):
    staff_name=models.CharField(max_length=20, null=True, blank=True)
    email_id=models.TextField(null=True, blank=True)
    age=models.IntegerField(null=True, blank=True)
    address=models.TextField(null=True, blank=True)


class Patient(models.Model):
    patient_name=models.CharField(max_length=30, null=True, blank=True)
    appointment_number=models.IntegerField(null=True, blank=True)


class AppointmentSchedule(models.Model):
    # patient_id= fk
    appointment_number=models.IntegerField(null=True, blank=True)
    time=models.TimeField()
    date=models.DateField()


class Doctor(models.Model):
    doctor_name=models.CharField(max_length=30, null=True, blank=True)
    appointment_number=models.IntegerField(null=True, blank=True)
    time=models.TimeField()
    date=models.DateField()
    bill=models.PositiveIntegerField(null=True, blank=True)


class Payment(models.Model):
    #patient_id = fk
    amount=models.IntegerField(null=True, blank=True)
    paid_amount=models.IntegerField(null=True, blank=True)
    due_amount=models.IntegerField(null=True, blank=True)


class Vaccine(models.Model):
    vaccine_name=models.CharField(max_length=30, null=True, blank=True)
    price=models.IntegerField(null=True, blank=True)
    stock_quantity=models.IntegerField(null=True, blank=True)


class Vaccination(models.Model):
   # patient_id= fk
   appointment_number=models.IntegerField(null=True, blank=True)
   vaccine_name=models.CharField(max_length=30, null=True, blank=True)


class Report(models.Model):
   # patient_id= fk
   patient_name = models.CharField(max_length=30, null=True, blank=True)
   appointment_number=models.IntegerField(null=True, blank=True)
   vaccine_name=models.CharField(max_length=30, null=True, blank=True)


class VaccineStock(models.Model):
    #vaccine_id= fk
     stock_in= models.PositiveIntegerField(null=True, blank=True)
     stock_out= models.PositiveIntegerField(null=True, blank=True)
     current_stock= models.PositiveIntegerField(null=True, blank=True)


class Signup(models.Model):
     first_name= models.CharField(max_length=30, null=True, blank=True)
     last_name= models.CharField(max_length=30, null=True, blank=True)
     email_id = models.TextField(null=True, blank=True)
     password= models.IntegerField(null=True, blank=True)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email),)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):

        user = self.create_user(
            email,
            password=password,
        )
        user.is_active=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255, default=None, null=True)
    last_name = models.CharField(max_length=255, default=None, null=True)

    email = models.EmailField(max_length=100, unique=True)

    username = None
    user_permissions = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    session_token = models.CharField(max_length=10, default=0)

    is_active = models.BooleanField(default=False)
    # a admin user; non super-user
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)  # a superuser

    phone = models.CharField(max_length=255, default=None, null=True, blank=True)
    address = models.TextField(default=None, null=True, blank=True)
    city = models.CharField(max_length=255, default=None, null=True, blank=True)
    state = models.CharField(max_length=255, default=None, null=True, blank=True)
    zip_code = models.CharField(max_length=255, default=None, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    profile_image = models.FileField(upload_to='static/vams/user')

    objects = UserManager()
