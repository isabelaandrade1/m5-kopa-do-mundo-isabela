from django.urls import path
from teams.views import TeamsView  # Importe a view corretamente

urlpatterns = [
    path("teams/", TeamsView.as_view(), name="teams"),  # Use o método `as_view` para views baseadas em classe
]
