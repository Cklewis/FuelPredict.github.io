from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.

'''
class HomePageTests(SimpleTestCase):

  def test_home_page_status_code(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)

  def test_view_url_by_name(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)

  def test_view_uses_correct_template(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code,200)
    self.assertTemplateUsed(response, 'pages/home.html')

class RegisterPageTests(TestCase):
  username = 'newuser'
  email = 'newuser@email.com'

  def test_register_page_status_code(self):
    response = self.client.get('/users/register/')
    self.assertEqual(response.status_code, 200)

  def test_view_url_by_name(self):
    response = self.client.get(reverse('register'))
    self.assertEqual(response.status_code, 200)

  def test_view_uses_correct_template(self):
    response = self.client.get(reverse('register'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'pages/register.html')


  def test_registration_form(self):
    new_user = get_user_model().objects.create_user(self.username, self.email)
    self.assertEqual(get_user_model().objects.all().count(), 1)
    self.assertEqual(get_user_model().objects.all()[0].username, self.username)
    self.assertEqual(get_user_model().objects.all()[0].email, self.email)

class QuotesPageTests(TestCase):
  def test_quotes_page_status_code(self):
    response = self.client.get('/users/quotes')
    self.assertEqual(response.status_code, 301) 
'''