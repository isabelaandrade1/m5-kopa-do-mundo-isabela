from django.urls import path
from .views import TeamsView, TeamDetailView

urlpatterns = [
    path("teams/", TeamsView.as_view(), name="teams"),
    path("teams/<int:team_id>/", TeamDetailView.as_view(), name="team_detail"),
]
