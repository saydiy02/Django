from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pentest(models.Model):
    GOAL_CHOICES = [
        (1, 'Web-application'),
        (2, 'Network'),
        (3, 'Cloud')
    ]
    TYPE_CHOICES = [
        (1, 'Web-based'),
        (2, 'Mobile'),
        (3, 'Network')
    ]
    TOOLS_CHOICES = [
        (1, 'Web-application'),
        (2, 'Network'),
        (3, 'Code-analysis'),
        (4, 'Password-Cracking')
    ]
    PLATFORM_CHOICES = [
        (1, 'Windows'),
        (2, 'Linux'),
        (3, 'MacOS'),
        (4, 'Cloud')
    ]
    goal = models.IntegerField(choices=GOAL_CHOICES)
    typeS = models.IntegerField(choices=TYPE_CHOICES)
    toolsC = models.IntegerField(choices=TOOLS_CHOICES)
    platform = models.IntegerField(choices=PLATFORM_CHOICES)
    
    def __str__(self):
        return f'Pentest: {self.id}'

    def get_goal_display(self):
        return dict(self.GOAL_CHOICES).get(self.goal, 'Unknown')

    def get_typeS_display(self):
        return dict(self.TYPE_CHOICES).get(self.typeS, 'Unknown')

    def get_toolsC_display(self):
        return dict(self.TOOLS_CHOICES).get(self.toolsC, 'Unknown')

    def get_platform_display(self):
        return dict(self.PLATFORM_CHOICES).get(self.platform, 'Unknown')
