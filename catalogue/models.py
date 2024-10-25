from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class YearMonth(models.Model):
    year = models.IntegerField(validators=[MinValueValidator(2023)])
    month = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])

    def __str__(self):
        if self.month // 10 == 0:
            return f"{self.year}-0{self.month}"
        else:
            return f"{self.year}-{self.month}"

    
    def get_absolute_url(self):
        return reverse(f"catalogue/{self.year}/{self.month}")
    

class SummaryDay(models.Model):
    year_month = models.ForeignKey(YearMonth, on_delete=models.CASCADE)
    day = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)])
    flare_num = models.IntegerField(null=True)
    diagram = models.FileField(upload_to="img/", blank=True)

    def __str__(self) -> str:
        if self.day // 10 == 0:
            return f"{self.year_month}-0{self.day}"
        else:
            return f"{self.year_month}-{self.day}"      


# class EventList(models.Model):
#     dt = models.ForeignKey(YearMonth, on_delete=models.CASCADE)
#     start_event = models.TimeField()
#     end_event = models.TimeField()
#     max_event = models.TimeField()
#     min_freq = models.FloatField()
#     max_freq = models.FloatField()

#     class Meta:
#         verbose_name_plural = "events"
#         ordering = 'date'
    
#     def __str__(self):
#         return f'{self.date}T{self.start_event}'
    
    # def get_absolute_url(self):
    #     return reverse(f"catalogue/{self.year}/{self.month}", kwargs={"pk": self.pk})
    
