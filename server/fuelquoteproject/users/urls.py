from django.urls import path

from . import views


urlpatterns = [
    path('edit/', views.edit_userProfile,name='edit'),
    path('profile/', views.userProfile, name="profile"),
    path('register/', views.Register.as_view(), name="register"),
]
