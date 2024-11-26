from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class FlareList(models.Model):
    date = models.DateField()
    num_flare = models.PositiveIntegerField(null=True)
    diagram = models.FileField(upload_to="img/", null=True)
    csv_file = models.FileField(upload_to="csv/", null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")
    
    def get_absolute_url(self):
        dt = self.date.strftime("%Y%m%d")
        return reverse("catalogue:flare_list", args=[dt])
