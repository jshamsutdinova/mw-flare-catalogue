from django.shortcuts import render
from django.http import HttpResponse
from django.utils.dates import MONTHS

from catalogue.models import SummaryDay, YearMonth
from .forms import YearMonthForm


def index(request):
    if request.method == 'POST':
        form = YearMonthForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            month = form.cleaned_data['month']
            records = SummaryDay.objects.filter(year_month__year=year, year_month__month=month)
            return render(request, 'catalogue/form.html',  {'form': form,
                                                                        'records': records,
                                                                        'year': year,
                                                                        'month': MONTHS[int(month)]})
    else:
        userform = YearMonthForm()
        return render(request, 'catalogue/form.html', {'form': userform})

