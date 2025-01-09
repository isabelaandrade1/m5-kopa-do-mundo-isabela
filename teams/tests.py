# teams/tests.py

from django.test import TestCase
from teams.models import Team

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(
            name="Brasil",
            titles=5,
            top_scorer="Pelé",
            fifa_code="BRA",
            first_cup="1930-07-13"
        )
        self.assertEqual(str(team), "<[1] Brasil - BRA>")
