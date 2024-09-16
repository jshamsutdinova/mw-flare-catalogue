from django.shortcuts import render
from main.models import *


# Create your views here.
def home(request):
    return render(request, "main/home.html", {})


def tab_users(request):
    team = Team.objects.all()
    context = {
        "team": team,
        "active-nav-item": 'users',
    }
    return render(request, "tabs/users.html", context)


def tab_publications(request):
    return render(request, "tabs/publications.html", {})


def tab_conference(request):
    conferences = Conference.objects.all()
    presentation = Presentation.objects.filter(conf_id=1)
    context = {
        "conferences": conferences,
        "presentation": presentation
    }
    return render(request, "tabs/conference.html", context)


def tab_results(request):
    return render(request, "tabs/results.html", {})


def tab_publication_abstract(request):
    conferences = Conference.objects.all()
    presentation = Presentation.objects.filter(conf_id=1)
    context = {
        "conferences": conferences,
        "presentation": presentation
    }
    return render(request, "publications/abstract.html", context)


def tab_publication_proceedings(request):
    return render(request, "publications/proceedings.html", {})


def tab_publication_papers(request):
    return render(request, "publications/papers.html", {})