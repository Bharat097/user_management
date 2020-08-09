from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    gender_choices = {
        ("male", "Male"),
        ("female", "Female"),
    }
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10, blank=True)
    gender = models.CharField(max_length=6, choices=gender_choices, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    img = models.ImageField(null=True, blank=True)
    location = models.CharField(max_length=150, blank=True)

    @property
    def imageURL(self):
        try:
            url = self.img.url
        except Exception:
            url = ""
        return url
