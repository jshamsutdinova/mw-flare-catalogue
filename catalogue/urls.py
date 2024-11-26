# catalogue/urls.py

from django.urls import path
from catalogue import views

app_name = "catalogue"

urlpatterns = [
    path("", views.month_flare_list, name='month_flare_list'),
    path('<int:dt>/', views.flare_list, name='flare_list'),
]
