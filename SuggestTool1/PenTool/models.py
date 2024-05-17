from django.db import models

# Create your models here.
class Pentest(models.Model):
   goal = models.IntegerField(choices=[(1,'Web-application'),(2,'Network'),(3,'Cloud')])
   typeS = models.IntegerField(choices=[(1,'Web-based'),(2,'Mobile'),(3,'Network')])
   toolsC = models.IntegerField(choices=[(1,'Web-application'),(2,'Network'),(3,'Code-analysis'),(4,'Password-Cracking')])
   platform = models.IntegerField(choices=[(1,'Windows'),(2,'Linux'),(3,'MacOS'),(4,'Cloud')])
   
   def __str__(self):
     return f'Pentest: {self.id}'