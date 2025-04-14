from django.db import models
from datetime import datetime
# Create your models here.
now = datetime.now()
value = now.strftime("%H:%M:%S")

class pmsReadings(models.Model):
    time = models.TimeField(default=value)
    pm10 = models.IntegerField(default=1)
    pm25 = models.IntegerField(default=1)
    pm100 = models.IntegerField(default=1)
