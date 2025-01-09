from django.urls import path
from . import views

urlpatterns = [
    path("teams/", views.teams_view, name="teams"),  # Exemplo de rota
]
