from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, FuelQuote
from crispy_forms.helper import FormHelper
from localflavor.us.models import USStateField
from bootstrap_datepicker_plus import DatePickerInput

class FuelQuoteModelForm(forms.ModelForm):
  class Meta:
    model = FuelQuote
    fields= [
      'gallons_requested',
      'delivery_street',
      'delivery_state',
      'delivery_zipcode',
      'delivery_date',
    ]
    widgets = {
    'delivery_date': DatePickerInput(format='%m/%d/%Y'),
    }
