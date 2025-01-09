from rest_framework import serializers
from teams.models import Team

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'titles', 'top_scorer', 'fifa_code', 'first_cup']
