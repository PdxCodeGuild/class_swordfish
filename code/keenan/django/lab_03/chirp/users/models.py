# commented out the below line to see if I can run without it
# from django.db import models
# adding this for custom user models/Abstract Users
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username
