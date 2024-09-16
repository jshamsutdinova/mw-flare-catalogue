from django import forms


YEARS = [x for x in range(2023, 2025)]

class FormDate(forms.Form):
    dt = forms.DateField(
        label="Choose a year",
        required=True,
        widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        input_formats=["%Y-%m"]
    )


class UserForm(forms.Form):
    dt = forms.DateField(label='Choose year',
                         widget=forms.SelectDateWidget(years=YEARS))
