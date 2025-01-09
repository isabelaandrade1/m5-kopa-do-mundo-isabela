from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Team
from .serializers import TeamSerializer
import datetime

class TeamsView(APIView):
    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        errors = self.validate_data(data)

        if errors:
            return Response({"error": errors}, status=status.HTTP_400_BAD_REQUEST)

        serializer = TeamSerializer(data=data)
        if serializer.is_valid():
            team = serializer.save()
            return Response(TeamSerializer(team).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def validate_data(self, data):
        if data.get("titles", 0) < 0:
            return "titles cannot be negative"

        first_cup = data.get("first_cup")
        if first_cup:
            try:
                first_cup_date = datetime.datetime.strptime(first_cup, "%Y-%m-%d").date()
                if first_cup_date.year < 1930 or first_cup_date.year not in [
                    1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974,
                    1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022
                ]:
                    return "there was no world cup this year"
            except ValueError:
                return "invalid date format, should be YYYY-MM-DD"

        disputed_cups = len([
            1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974,
            1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022
        ])
        if data.get("titles", 0) > disputed_cups:
            return "impossible to have more titles than disputed cups"

        return None


class TeamDetailView(APIView):
    def get(self, request, team_id):
        try:
            team = Team.objects.get(id=team_id)
            serializer = TeamSerializer(team)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, team_id):
        try:
            team = Team.objects.get(id=team_id)
            for key, value in request.data.items():
                setattr(team, key, value)
            team.save()
            serializer = TeamSerializer(team)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, team_id):
        try:
            team = Team.objects.get(id=team_id)
            team.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status=status.HTTP_404_NOT_FOUND)
