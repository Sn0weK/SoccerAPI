from django.db import models

# Create your models here.


class Team(models.Model):
    name            =   models.CharField(max_length=200)
    abbreviation    =   models.CharField(max_length=3)
    country         =   models.CharField(max_length=3)
    stadium_name    =   models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
    def __str__(self):
        return "{} ({})".format(self.name, self.country)
    @property
    def players(self):
        return self.player_set.all()
    @property
    def last_five_matches(self):
        return self.match_set.all().orderBy('-id')[5:]

class Player(models.Model):
    first_name  = models.CharField(max_length=70, blank=True)
    last_name   = models.CharField(max_length=100, blank=True)
    team        = models.ForeignKey(Team, on_delete=models.CASCADE)
    number      = models.IntegerField()
    position    = models.CharField(max_length=3)
    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'
        ordering = ["team__abbreviation", "number"]
    def __str__(self):
        return "{} {}({}) - {} {}".format(self.team.abbreviation, self.number, self.position, self.first_name, self.last_name, self.number)
    @property
    def goals_count(self):
        return self.shot_set.filter(is_goal=True).count()
    @property
    def shots_count(self):
        return self.shot_set.all().count()
    @property
    def shots(self):
        return self.shot_set.all()
    @property
    def passes(self):
        return self.pass_player.all()
    

class Match(models.Model):
    home_team   =   models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    away_team   =   models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team')
    match_date  =   models.DateTimeField()
    home_score  =   models.IntegerField()
    away_score  =   models.IntegerField()
    class Meta:
        verbose_name = 'Match'
        verbose_name_plural = 'Matches'
    def __str__(self):
        return "{} {}-{} {} ({})".format(self.home_team.abbreviation, self.home_score, self.away_score, self.away_team.abbreviation, self.match_date)
    @property
    def passes(self):
        return self.pass_set.all()
    @property
    def shots(self):
        return self.shot_set.all()
    @property
    def goals(self):
        return self.shot_set.filter(is_goal = True)
    @property
    def home_team_name(self):
        return self.home_team.name
    @property
    def away_team_name(self):
        return self.away_team.name


class Pass(models.Model):
    match           = models.ForeignKey(Match, on_delete=models.CASCADE)
    team            = models.ForeignKey(Team, on_delete=models.CASCADE)
    player          = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='pass_player')
    target          = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='pass_target')
    position_x      = models.FloatField()
    position_y      = models.FloatField()
    is_successful   = models.BooleanField()
    class Meta:
        verbose_name = 'Pass'
        verbose_name_plural = 'Passes'
    def __str__(self):
        return "Pass to {} (Success: {})".format(self.target.last_name, self.is_successful)

class Shot(models.Model):
    match           = models.ForeignKey(Match, on_delete=models.CASCADE)
    team            = models.ForeignKey(Team, on_delete=models.CASCADE)
    player          = models.ForeignKey(Player, on_delete=models.CASCADE)
    position_x      = models.FloatField()
    position_y      = models.FloatField()
    period          = models.IntegerField()
    time            = models.IntegerField()
    on_target       = models.BooleanField()
    is_goal         = models.BooleanField()
    class Meta:
        verbose_name = 'Shot'
        verbose_name_plural = 'Shots'
    def __str__(self):
        return "{} vs.{} - {} ({}' - Goal: {}) [{}])".format(self.match.home_team.abbreviation, self.match.away_team.abbreviation, self.player.last_name, self.time, self.is_goal, self.match.match_date)

