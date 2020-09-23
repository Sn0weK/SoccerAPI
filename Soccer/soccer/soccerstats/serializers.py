from rest_framework import serializers
from .models import *

class ShotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shot
        read_only_fields = ['id']
        fields = ["match", "team", "player", "time", "position_x", "position_y", "on_target", "is_goal"]

class PassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pass
        read_only_fields = ['id']
        fields = ["match", "team", "player", "target", "position_x", "position_y", "is_successful"]


class PlayerSerializer(serializers.ModelSerializer):
    shots = ShotSerializer(many=True, read_only=True)
    class Meta:
        model = Player
        read_only_fields = ['id']
        fields = ["first_name", "last_name", "team", "number", "position", "shots_count", "passes_count", "goals_count", "shots"]



class TeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)
    class Meta:
        model = Team
        read_only_fields = ['id',]
        fields = ["name", "abbreviation", "country", "stadium_name","players"]

class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["name", "abbreviation", "country", "stadium_name"]
        read_only_fields = ['id']


class MatchSerializer(serializers.ModelSerializer):
    shots = ShotSerializer(many=True, read_only=True)
    passes = PassSerializer(many=True, read_only=True)
    goals = ShotSerializer(many=True, read_only=True)
    class Meta:
        model = Match
        read_only_fields = ['id']
        fields = ["home_team", "home_team_name", "away_team", "away_team_name", "match_date", "home_score", "away_score", 'shots', 'passes', 'goals']


class MatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        read_only_fields = ['id']
        fields = ["home_team", "away_team", "match_date", "home_score", "away_score"]