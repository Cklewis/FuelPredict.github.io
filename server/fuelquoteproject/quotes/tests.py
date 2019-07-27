from django.test import TestCase
from django.test import Client
from .forms import *   # imports all forms
from users.forms import *
import datetime

# Create your tests here.
class Setup_Class(TestCase):
  def setUp(self):
    self.user = CustomUser.objects.create(
      username='test_user',
      full_name='John Smith',
      address1='123 Test Terrace',
      address2='Suite 203',
      city='Dallas',
    )

class TestQuoteForm(TestCase):
  def setUp(self):
    self.user = CustomUser.objects.create(
      username='test_user',
      full_name='John Smith',
      address1='123 Test Terrace',
      address2='Suite 203',
      city='Dallas',
    )

  def test_QuoteForm_valid(self):
    user_pk = CustomUser.objects.get(pk=1).pk
    form = FuelQuoteModelForm(data={
      'user': user_pk,
      'delivery_date': "2019-10-10",
      'gallons_requested': 150,
      'delivery_state': "Texas",
      'delivery_street': "1234 Test Terrace",
      'delivery_zipcode':"75001"})
    self.assertTrue(form.is_valid())

  def test_UserForm_invalid(self):
    form = CustomUserCreationForm(data={'username':"",
      'full_name':"",
      'address1':"",
      'address2':"",
      'city':""})
    self.assertFalse(form.is_valid())
