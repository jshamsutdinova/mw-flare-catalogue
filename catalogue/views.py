from django.shortcuts import render
from django.utils.dates import MONTHS
from django.db.models import Count

from catalogue.models import Flare
from .forms import YearMonthForm

import pandas as pd
import numpy as np
import plotly.express as px
from plotly.offline import plot
from plotly.graph_objs import Figure, Scatter


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


def do_plot():
    x_data = [0, 1, 2, 3]
    y_data = [x**2 for x in x_data]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                           mode='lines+markers', name='test',
                           opacity=0.8, marker_color='green')],
                           output_type='div')
    
    df = pd.read_csv('media/csv/event_data20240112_array.csv')
    df.replace(0, np.nan, inplace=True)
    values = df.to_numpy()
    keys = np.array([3000000.0, 3200000.0, 3400000.0,	3600000.0, 3800000.0, 4000000.0,
                    4200000.0, 4400000.0, 4600000.0,	4800000.0, 5000000.0, 5200000.0, 
                    5400000.0, 5600000.0, 5800000.0, 6400000.0, 6800000.0, 7200000.0, 
                    7600000.0, 8000000.0	, 8400000.0, 8800000.0, 9200000.0, 9600000.0, 
                    10000000.0, 10400000.0,	10800000.0,	11200000.0,	11600000.0,	
                    12000000.0,	12960000.0,	13720000.0,	14480000.0,	15240000.0,	
                    16000000.0,	16760000.0,	17520000.0,	18280000.0,	19040000.0,	
                    19400000.0,	20560000.0,	21320000.0,	22080000.0,	23600000.0,	23840000.0])

    traces = []
    
    lower_3_6 = 3000000.0
    upper_3_6 = 5800000.0

    lower_6_12 = 6200000.0
    upper_6_12 = 11800000.0

    lower_12_24 = 12800000.0
    upper_12_24 = 24000000.0
    
    for i, key in enumerate(keys):
        x_data = values[:, i]

        if key >= lower_3_6 and key <= upper_3_6:
            color = 'red'
        elif key >= lower_6_12 and key <= upper_6_12:
            color = 'green'
        else:
            color = 'blue'
    
        trace = Scatter(
            x = x_data,
            y = np.full_like(x_data, key / (10 ** 6)),
            mode='markers',
            name=f'{key / (10**6)} GHz',
            opacity=0.8,
            marker_color=color
        )
        traces.append(trace)

    plot_div = plot(traces, output_type='div')

    return plot_div


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
    plot_div = do_plot()

    return render(request, "catalogue/flare/day_list.html", {'flares': flares,
                                                             'plot': plot_div})


    