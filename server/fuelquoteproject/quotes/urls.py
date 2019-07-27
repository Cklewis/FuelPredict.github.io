from django.urls import path, re_path

from . import views

urlpatterns = [
    # '' specifies the root
    path('', views.quotes, name='quotes'),
    path('<int:id>/', views.quote_detail_page, name='quote'),
    path('get_quote/', views.get_quote, name='get_quote'),
    path('confirm/<int:quote_id>' ,views.quote_confirmation_page, name="confirm")

]