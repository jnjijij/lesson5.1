from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=100)
    year = models.IntegerField()
    seats = models.IntegerField()
    body_type = models.CharField(max_length=100)
    engine_volume = models.FloatField()

    def __str__(self):
        return f"{self.id}, {self.brand}, {self.year}"
