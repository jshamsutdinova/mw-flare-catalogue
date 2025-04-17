from django.shortcuts import render
from django.utils.dates import MONTHS
from django.db.models import Count

from catalogue.models import Flare
from .forms import YearMonthForm


def month_flare_list(request):
    if request.method == 'POST':
        form = YearMonthForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            month = form.cleaned_data['month']
            delete_artifacts = form.cleaned_data['delete_artifacts']
            request.session['form_data'] = form.cleaned_data
            
            if delete_artifacts:
                flare_counts = Flare.objects.filter(
                    date__year=year, date__month=month, tag=0).values('date').annotate(Count('date')).order_by()
            else:
                flare_counts = Flare.objects.filter(
                    date__year=year, date__month=month).values('date').annotate(Count('date')).order_by()
            
            objects = []
            for rec in flare_counts:
                obj = Flare.objects.filter(date=rec['date'])[0]
                objects.append(obj)

            return render(request, 'catalogue/form.html',  {'form': form,
                                                            'records': flare_counts,
                                                            'objects': objects,
                                                            'year': year,
                                                            'month': MONTHS[int(month)]})
    else:
        userform = YearMonthForm()
        return render(request, 'catalogue/form.html', {'form': userform})


def flare_list(request, year, month, day):
    form_data = request.session.get('form_data')

    if form_data['delete_artifacts']:
        flares = Flare.objects.filter(date__year=year,
                                      date__month=month,
                                      date__day=day, 
                                      tag=0)
    else:
        flares = Flare.objects.filter(date__year=year,
                                      date__month=month,
                                      date__day=day)

    return render(request, "catalogue/flare/day_list.html", {'flares': flares})
