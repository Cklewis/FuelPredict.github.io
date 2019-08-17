from django.urls import path

from . import views


urlpatterns = [
    # '' specifies the root
    path('', views.index, name='index'),
]