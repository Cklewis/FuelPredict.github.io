from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from users.models import CustomUser
from localflavor.us.models import USZipCodeField, USStateField

# Create your models here.
User = settings.AUTH_USER_MODEL

class FuelQuote(models.Model):
    gallons_requested = models.PositiveIntegerField(blank=False)
    delivery_street = models.CharField(max_length=200)
    delivery_street2 = models.CharField(max_length=200, blank=True)
    delivery_state = USStateField()
    delivery_zipcode = USZipCodeField()
    delivery_date = models.DateField(blank=False)
    total_amount_due = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    price_per_gallon = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    discounts = models.DecimalField(max_digits=15, decimal_places=2, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
class FuelQuoteModifier(models.Model):
    price_per_gallon = models.DecimalField(max_digits=10, decimal_places=2)
    summer_modifier = models.DecimalField(max_digits=10, decimal_places=2)
    profit_margin = models.DecimalField(max_digits=5, decimal_places=3)