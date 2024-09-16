from django.db import models

# Create your models here.
class Catalogue(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.FileField(upload_to="img/", blank=True)

    def __str__(self) -> str:
        return self.title

