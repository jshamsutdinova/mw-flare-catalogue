from django.urls import path, include
from main import views


app_name = "home"

publications_patterns = [
    path("abstract/", views.tab_publication_abstract, name="abstract"),
    path("proceedings/", views.tab_publication_proceedings, name="proceedings"),
    path("papers/", views.tab_publication_papers, name="papers")
]

tab_patterns = [
    path("users/", views.tab_users, name="users"),
    path("publications/", views.tab_publication_abstract, name="publication"),
    path("publications/", include(publications_patterns)),
    path("conference/", views.tab_conference, name="conference"),
    path("results/", views.tab_results, name='results'),
]

urlpatterns = [
    path("", views.home, name="home"),
    path("", include(tab_patterns)),
]
