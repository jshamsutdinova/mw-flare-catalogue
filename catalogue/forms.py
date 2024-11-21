from django import forms
from .models import YearMonth
from django.utils.dates import MONTHS


YEAR_CHOICES =( 
    (2023, 2023), 
    (2024, 2024)
) 


class YearMonthForm(forms.Form):
    year = forms.ChoiceField(choices=YEAR_CHOICES)
    month = forms.ChoiceField(choices=MONTHS)
 
