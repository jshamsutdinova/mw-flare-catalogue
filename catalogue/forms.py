from django import forms
from django.utils.dates import MONTHS


YEAR_CHOICES =( 
    (2023, 2023), 
    (2024, 2024),
    (2025, 2025),
) 


class YearMonthForm(forms.Form):
    year  = forms.ChoiceField(choices=YEAR_CHOICES)
    month = forms.ChoiceField(choices=MONTHS)
    delete_artifacts = forms.BooleanField(
        label="Delete artifacts",
        required=False,
        initial=False)
