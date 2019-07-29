from django.contrib.auth.models import AbstractUser
from django.db import models
from localflavor.us.models import USStateField, USZipCodeField
#Create your models here.

class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=50, blank=False)
    address1 = models.CharField(max_length=100, blank=False)
    address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=False)
    state = USStateField()
    zipcode = USZipCodeField()
