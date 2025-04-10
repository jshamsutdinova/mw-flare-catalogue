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
    flares = Flare.objects.filter(date__year=year,
                                  date__month=month,
                                  date__day=day)
    return render(request, "catalogue/flare/day_list.html", {'flares': flares})


def delete_artifacts(request):
    if request.method == 'POST':
        del_toggle = request.POST.get('del_toggle', False)

        if del_toggle:
            flare_list = Flare.objects.filter(tag=0)
        else:
            flare_list = Flare.objects.all()
        
    return render(request, 'catalogue/form.html', {'flare_list': flare_list})
