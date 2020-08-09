from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


# Create your models here.
class User(AbstractUser):
    gender_choices = {
        ("male", "Male"),
        ("female", "Female"),
    }
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be entered in the format: '9999999999'.")

    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10, validators=[phone_regex], blank=True, null=True)
    gender = models.CharField(max_length=6, choices=gender_choices)
    dob = models.DateField(blank=True, null=True)
    img = models.ImageField(null=True, blank=True)
    location = models.CharField(max_length=150)

    @property
    def imageURL(self):
        try:
            url = self.img.url
        except Exception:
            url = ""
        return url
