from rest_framework import serializers
from .models import *

class ShotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shot
        read_only_fields = ['id']
        fields = ["id","match", "team", "player", "time", "period", "position_x", "position_y", "on_target", "is_goal"]

class PassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pass
        read_only_fields = ['id']
        fields = ["id","match", "team", "player", "target", "position_x", "position_y", "is_successful"]


class PlayerSerializer(serializers.ModelSerializer):
    shots = ShotSerializer(many=True, read_only=True)
    passes = PassSerializer(many=True, read_only=True)
    class Meta:
        model = Player
        read_only_fields = ['id']
        fields = ['id','first_name', 'last_name', 'team', 'number', 'position', 'shots_count', 'goals_count', 'shots', 'passes',]



class TeamSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(many=True, read_only=True)
    class Meta:
        model = Team
        read_only_fields = ['id',]
        fields = ["id","name", "abbreviation", "country", "stadium_name","players"]

class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["id","name", "abbreviation", "country", "stadium_name"]
        read_only_fields = ['id']


class MatchSerializer(serializers.ModelSerializer):
    shots = ShotSerializer(many=True, read_only=True)
    passes = PassSerializer(many=True, read_only=True)
    goals = ShotSerializer(many=True, read_only=True)
    class Meta:
        model = Match
        read_only_fields = ['id']
        fields = ["id","home_team", "home_team_name", "away_team", "away_team_name", "match_date", "home_score", "away_score", 'shots', 'passes', 'goals']


class MatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        read_only_fields = ['id']
        fields = ["id","home_team", "home_team_name", "away_team", "away_team_name", "match_date", "home_score", "away_score"]