from django.db import models


class CO2Data(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    co2_level = models.FloatField()
    temperature = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.timestamp}: {self.co2_level} ppm"
