from tkinter import CASCADE
from django.db import models
import uuid
from django.contrib.auth.models import User

class PsgPredictor(models.Model):
    competition = models.IntegerField(blank=False, null=False, default=0)
    day = models.IntegerField(blank=False, null=False, default=0)
    venue = models.IntegerField(blank=False, null=False, default=0)
    opponent = models.IntegerField(blank=False, null=False, default=0)
    captain = models.IntegerField(blank=False, null=False, default=0)
    formation = models.IntegerField(blank=False, null=False, default=0)
    stamp = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True,editable=False,unique=True)

    def __str__(self) -> str:
        if self.competition == 3:
            return 'PSG Champions League match'
        elif self.competition == 2:
            return 'PSG League 1 match'
        elif self.competition == 1:
            return 'PSG Coup de France'
        return self.competition

    def namme(self) -> str:
        if self.competition == 3:
            return 'PSG Champions League match'
        elif self.competition == 2:
            return 'PSG League 1 match'
        elif self.competition == 1:
            return 'PSG Coup de France'
        return 'Competition'

        TODO
        # create a databse of fottball teams and a function to convert opponent to string
        TODO

class Result(models.Model):
    competition = models.CharField(max_length=200, blank=False,null=False)
    win_or_lose = models.IntegerField(blank=False,null=False)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True,editable=False,unique=True)
    
    def __str__(self) -> str:
        result = ""
        if self.win_or_lose == 0:
            result += "Draw!"
        elif self.win_or_lose ==1:
            result += "Win!"
        else:
            result +=  "Lose!"

        return result