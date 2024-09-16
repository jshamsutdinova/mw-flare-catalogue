# catalogue/urls.py

from django.urls import path
from catalogue import views


urlpatterns = [
    # path("", views.month_index, name="month_index"),
    path("", views.form_year_month),
    path("<int:pk>/", views.month_detail, name="month_detail"),
]
