from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from crispy_forms.helper import FormHelper
from localflavor.us.models import USStateField

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = [
            'username',
            'full_name',
            'email',
            'password1',
            'password2'
        ]

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs['placeholder'] = field.label
            field.label = ''
            field.help_text = ''

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = [
            'full_name',
            'email',
            'address1',
            'address2',
            'city',
            'state',
            'password',
            'zipcode',
        ]

    def clean_zipcode(self):
        zipcode = self.cleaned_data['zipcode']
        if len(zipcode) < 5:
            raise ValidationError("Zipcode must contain 5 digits")
        return zipcode


    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field= self.fields.get(field_name)
            field.widget.attrs['placeholder'] = field.label
            field.label= ''
        
class UserLoginForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'password'
        ]
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)
            field.widget.attrs['placeholder'] = field.label
            field.label = ''
            field.help_text = ''