from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=30)
    part = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Publication(models.Model):
    authors = models.TextField()
    title   = models.TextField()
    journal = models.TextField()
    doi = models.CharField(max_length=20)

    def __str__(self):
        return self.title

# class Proceedings(models.Model):

class Conference(models.Model):
    name_conf = models.TextField()
    date  = models.CharField(max_length=20)
    place = models.TextField()
    url_abstract = models.URLField(null=True)

    def __str__(self):
        return self.name_conf


class Presentation(models.Model):
    type = models.CharField(max_length=20)
    name = models.TextField()
    first_author = models.CharField(max_length=30)
    authors = models.TextField()
    conf = models.ForeignKey(Conference, on_delete=models.CASCADE, null=True)
    page = models.IntegerField(null=True)
    
    class  Meta:
        ordering = ['-type', 'first_author']

    def __str__(self):
        return f"{self.first_author} {self.name}"

