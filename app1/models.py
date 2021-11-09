from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models import Avg, Count, Sum, Min, Max
from django.utils.timezone import now

class zbdoor(models.Model):
    topic = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    battery = models.IntegerField(default = None)
    battery_low = models.BooleanField(default= None)
    contact = models.BooleanField(default= None)
    linkquality = models.IntegerField(default = None)
    voltage = models.IntegerField(default = None)

    def __str__(self):
        return f'{[self.topic, self.created_date, self.contact]!r}'

class zbbtn(models.Model):
    topic = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    battery = models.IntegerField(default = None)
    action = models.CharField(max_length=10, default = None)
    linkquality = models.IntegerField(default = None)
    voltage = models.IntegerField(default = None)

    def __str__(self):
        return f'{self.topic}  {self.created_date.strftime("%Y-%m-%d %H:%M")} {self.action}'
        #self.created_date.strftime("%d %b %Y %H:%M:%S")

class zbtmphum(models.Model):
    topic = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    battery = models.IntegerField(default = None)
    humidity =models.DecimalField(max_digits=5, decimal_places=2)
    temperature =models.DecimalField(max_digits=5, decimal_places=2)
    linkquality = models.IntegerField(default = None)
    voltage = models.IntegerField(default = None)

    def __str__(self):
        return f'{[self.topic, self.created_date, self.temperature, self.humidity]!r}'