# catalogue/urls.py

from django.urls import path
from catalogue import views

app_name = "catalogue"

urlpatterns = [
    path("", views.index, name='select_year_month'),
]
