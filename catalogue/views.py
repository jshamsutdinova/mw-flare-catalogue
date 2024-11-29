from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils.dates import MONTHS

from catalogue.models import FlareList, Flare
from .forms import YearMonthForm


def month_flare_list(request):
    if request.method == 'POST':
        form = YearMonthForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            month = form.cleaned_data['month']
            records = FlareList.objects.filter(date__year=year, date__month=month)
            return render(request, 'catalogue/form.html',  {'form': form,
                                                            'records': records,
                                                            'year': year,
                                                            'month': MONTHS[int(month)]})
    else:
        userform = YearMonthForm()
        return render(request, 'catalogue/form.html', {'form': userform})

def flare_list(request, dt):
    list = get_object_or_404(FlareList, date=str(dt))
    flares = Flare.objects.filter(date__date=str(dt))
    return render(request, "catalogue/flare/day_list.html", {'list': list,
                                                             'flares': flares})
