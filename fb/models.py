from django.db import models

# Create your models here.
class Players(models.Model):
    class Position(models.TextChoices):
        ATT = 'ATT', 'Attacker'
        MID = 'MID', 'Midfielder'
        DEF = 'DEF', 'Defender'
        GK  = 'GK',  'Goalkeeper'

    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', 'Active'
        RETIRED = 'RETIRED', 'Retired'
        DECEASED = 'DECEASED', 'Deceased'

    name = models.CharField(max_length=50,null=False)
    age = models.IntegerField(null=False)
    country = models.CharField(max_length=60,null=False)
    club = models.CharField(max_length=50,null=True)
    position = models.CharField(max_length=3,choices=Position.choices)
    goals = models.IntegerField(default=0)
    matches = models.IntegerField(default=0)
    status = models.CharField(max_length=10,choices=Status.choices,default=Status.ACTIVE)
    rating = models.IntegerField(default=50)
    


    
