from django.db import models

# Create your models here.
class Room(models.Model):
    room_code = models.CharField(max_length=8, default = "", unique = True)