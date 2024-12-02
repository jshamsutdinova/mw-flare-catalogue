from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class FlareList(models.Model):
    date = models.DateField()
    num_flare = models.PositiveIntegerField(null=True)
    diagram = models.ImageField(upload_to="img/", null=True)
    csv_file = models.FileField(upload_to="csv/", null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")
    
    def get_absolute_url(self):
        dt = self.date.strftime("%Y%m%d")
        return reverse("catalogue:flare_list", args=[dt])


class Flare(models.Model):
    date = models.ForeignKey(FlareList, on_delete=models.CASCADE)
    start_event = models.TimeField()
    maximum_event = models.TimeField()
    finish_event = models.TimeField()
    min_freq = models.FloatField()
    max_freq = models.FloatField()

    def __str__(self):
        title = f"{self.date.date.strftime("%Y-%m-%d")} \
            {self.start_event.strftime("%H:%M:%S")}-{self.finish_event.strftime("%H:%M:%S")}"
        return title
