from django.shortcuts import render
from catalogue.models import Catalogue

from .forms import FormDate, UserForm

import plotly.express as px
from plotly.offline import plot
import numpy as np

# Create your views here.

def form_year_month(request):
    form = UserForm(request.POST)
    context = {'form': form}
    return render(request, "catalogue/form.html", context)


def month_index(request):
    months = Catalogue.objects.all()
    context = {
        "months": months
    }
    return render(request, "catalogue/month_index.html", context)


def month_detail(request, pk):
    list_flare = Catalogue.objects.get(pk=pk)
    context = {
        "list_flare": list_flare 
    }
    return render(request, "catalogue/month_detail.html", context)

def plot(request):
    x = np.arange(0, 4*np.pi, 0.1)
    y = np.sin(x)

    fig = px.timeline(
        x, y
    )
    fig.update_xaxes(autorange="reversed")
    test_plot = plot(fig, output_type="div")
    context = {'plot_div': test_plot}

    return render(request, 'catalogue/month_detail.html', context)

