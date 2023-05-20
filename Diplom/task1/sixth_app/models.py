from django.db import models
from datetime import date
from datetime import timedelta
# Create your models here.
class GameModel(models.Model):
    name = models.CharField(max_length=64)
    platform = models.CharField(max_length=64)
    year = models.DateField()
    genre = models.CharField(max_length=64)
    publisher = models.CharField(max_length=64)
    na_sales = models.FloatField()
    eu_sales = models.FloatField()
    jp_sales = models.FloatField()
    other_sales = models.FloatField()
    global_sales = models.FloatField()
    def __str__(self):
        return f"{self.id}_{self.name}"
class JSon(models.Model):
    MatchNumber = models.DecimalField(decimal_places=2, max_digits=100, default=0)
    RoundNumber = models.DecimalField(decimal_places=2, max_digits=100, default=0)
    DateUtc = models.DateTimeField()
    Location = models.CharField(max_length=100)
    HomeTeam = models.CharField(max_length=100)
    AwayTeam = models.CharField(max_length=100)
    Group = models.CharField(max_length=100,null=True,blank=True)
    HomeTeamScore = models.DecimalField(decimal_places=2, max_digits=100, default=0)
    AwayTeamScore = models.DecimalField(decimal_places=2, max_digits=100, default=0)
    def __str__(self):
        return f"{self.id}_{self.Location}"