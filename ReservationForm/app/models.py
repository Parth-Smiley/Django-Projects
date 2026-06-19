from django.db import models

# Create your models here.
class Reservations(models.Model):
    FirstName = models.CharField(max_length = 255)
    LastName = models.CharField(max_length = 255)
    no_of_people = models.IntegerField()
    date = models.DateTimeField(auto_now=True)