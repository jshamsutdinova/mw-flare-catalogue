import os
from django.db import models
from django.urls import reverse


class Flare(models.Model):
    
    class Tag(models.IntegerChoices):
        FLARE = 0, 'flare'
        BACKGROUND = 1, 'background'
        ARTIFACT = 2, 'artifact'

    date = models.DateField()
    start_event = models.DateTimeField()
    maximum_event = models.DateTimeField()
    end_event = models.DateTimeField(null=True)
    min_freq  = models.FloatField()
    max_freq  = models.FloatField()
    tag = models.IntegerField(default=Tag.ARTIFACT, choices=Tag.choices)

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        title = f"{self.date.strftime("%Y-%m-%d")} \
            {self.start_event.strftime("%H:%M:%S")}-{self.end_event.strftime("%H:%M:%S")}"
        return title
    
    def get_absolute_url(self):
        dt = self.date.strftime("%Y%m%d")
        return reverse("catalogue:flare_list",
                       args=[
                           self.date.year,
                           self.date.month,
                           self.date.day
                       ])
