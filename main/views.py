from typing import Any
from django.shortcuts import render
from main.models import *
from django.views.generic.detail import DetailView


class ConferenceDetailView(DetailView):
    model = Presentation
    context_object_name = 'presentation_list'
    template_name = 'tabs/conference.html'

    def get_context_data(self, request, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['presentation_list'] = Presentation.objects.filter(conf_id=self.kwargs['pk'])

        return render(request, "tabs/conference.html", context)


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
    presentation = Presentation.objects.all()
    context = {
        "conferences": conferences,
        "presentation": presentation
    }
    return render(request, "tabs/conference.html", context)


def tab_results(request):
    return render(request, "tabs/results.html", {})


def tab_publication_abstract(request):
    conferences = Conference.objects.all()
    presentation = Presentation.objects.order_by('first_author', 'name')
    context = {
        "conferences": conferences,
        "presentation": presentation
    }
    return render(request, "publications/abstract.html", context)


def tab_publication_proceedings(request):
    proceeding = Proceedings.objects.all()
    context = {'proceedings': proceeding}
    return render(request, "publications/proceedings.html", context)


def tab_publication_papers(request):
    return render(request, "publications/papers.html", {})